from rest_framework import generics, status, viewsets, mixins, permissions
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

from voting_api.premissions import AnswerEditingPermission
from voting_api.serializers import VotingSerializer, QuestionSerializer, AnswerSerializer, VotingStatisticSerializer
from voting_api.models import Voting, Question, Answer


class VotingGenericView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, BasicAuthentication, SessionAuthentication)
    queryset = Voting.objects.all()
    serializer_class = VotingSerializer
    auth_methods = ('POST', 'PUT', 'DELETE', 'PATCH')

    def get_permissions(self):
        if self.request.method in self.auth_methods:
            permission_classes = [IsAdminUser, IsAuthenticated]
            return [permission() for permission in permission_classes]
        return [AllowAny()]


class QuestionGenericView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, BasicAuthentication, SessionAuthentication)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    auth_methods = ('POST', 'PUT', 'DELETE', 'PATCH')

    def get_permissions(self):
        if self.request.method in self.auth_methods:
            permission_classes = [IsAdminUser, IsAuthenticated]
            return [permission() for permission in permission_classes]
        return [AllowAny()]


class AnswerGenericView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, BasicAuthentication, SessionAuthentication)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    auth_methods = ('POST', 'PUT', 'DELETE', 'PATCH')

    def get_permissions(self):
        if self.request.method not in permissions.SAFE_METHODS:
            permission_classes = [AnswerEditingPermission]
            return [permission() for permission in permission_classes]
        return [AllowAny()]


class StatisticByUserGenreticView(viewsets.GenericViewSet):
    serializer_class = VotingStatisticSerializer

    def get_queryset(self):
        return Voting.objects.all()

    def create(self, request):
        serializer = VotingStatisticSerializer(self.get_queryset(), many=True, context={'request': request}).data
        return Response(serializer, status=status.HTTP_200_OK)

    def get(self, request):
        return Response({"message": "выберите ид пользователя для статистики по опросам"}, status=status.HTTP_200_OK)
