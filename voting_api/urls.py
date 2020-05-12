from django.conf.urls import url
from django.urls import path, include
from .views import VotingGenericView, QuestionGenericView, AnswerGenericView, StatisticByUserGenreticView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('votings', VotingGenericView, basename='votings')
router.register('questions', QuestionGenericView, basename='questions')
router.register('answers', AnswerGenericView, basename='answers')
router.register('statistic', StatisticByUserGenreticView, basename='statistic')

urlpatterns = [
    url('', include(router.urls))
]
