from django.contrib.auth.models import User
from rest_framework import serializers
from .filters import FilteredQuestionSerializer, FilteredAnswerSerializer, FilteredVotingSerializer
from .models import Voting, Question, Answer


# СЕРИАЛИЗАЦИЯ ОТВЕТА К ОПРОСУ
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer_text', 'question', 'user',)
        read_only_fields = ('id',)


# CЕРИАЛИЗАЦИЯ ВОПРОСА К ОПРОСУ
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'voting', 'question_text', 'question_type',)
        read_only_fields = ('id',)


# СЕРЕАЛИЗАЦИЯ ОПРОСА
class VotingSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(format="%H:%M:%S || %d-%m-%Y", read_only=True)

    class Meta:
        model = Voting
        fields = ('id', 'name', 'desc', 'start_date', 'end_date')
        read_only_fields = ('id', 'start_date')


class DetailAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer_text', 'question', 'user',)
        read_only_fields = ('id',)
        list_serializer_class = FilteredAnswerSerializer


class DetailQuestionSerializer(serializers.ModelSerializer):
    answers = DetailAnswerSerializer(many=True)

    class Meta:
        model = Question
        list_serializer_class = FilteredQuestionSerializer
        fields = ('id', 'voting', 'question_text', 'question_type', 'answers')
        read_only_fields = ('id', 'voting', 'question_text', 'question_type', 'answers')


# СЕРИАЛИЗАЦИЯ СТАТИСТИКИ ОТВЕТОВ НА ВОПРОСЫ К ОПРОСАМ ПО ПОЛЬЗОВАТЕЛЮ
class VotingStatisticSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    questions = DetailQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Voting
        list_serializer_class = FilteredVotingSerializer
        fields = ('id', 'name', 'start_date', 'end_date', 'desc', 'questions', 'user_id')
        read_only_fields = ('id', 'name', 'start_date', 'end_date', 'desc', 'questions', 'user_id')
