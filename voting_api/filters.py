from rest_framework import serializers


class FilteredAnswerSerializer(serializers.ListSerializer):
    def to_representation(self, answers_list):
        user_id = self.context['request'].data['user_id']
        filtered = answers_list.filter(user_id=user_id)
        return super(FilteredAnswerSerializer, self).to_representation(filtered)


class FilteredQuestionSerializer(serializers.ListSerializer):
    def to_representation(self, questions_list):
        user_id = self.context['request'].data['user_id']
        filtered = questions_list.filter(answers__user_id=user_id)
        return super(FilteredQuestionSerializer, self).to_representation(filtered)


class FilteredVotingSerializer(serializers.ListSerializer):
    def to_representation(self, voting_list):
        user_id = self.context['request'].data['user_id']
        if not user_id:
            raise serializers.ValidationError('Пользователь с ид равному {} не найден'.format(user_id))
        filtered = voting_list.filter(questions__answers__user_id=user_id).distinct()
        return super(FilteredVotingSerializer, self).to_representation(filtered)
