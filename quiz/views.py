from .serializers import QuestionSerializer, AnswerSerializer, QuizSerializer, AnswersSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Question, Quiz, Answer
from datetime import date

class GetQuiz(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuizSerializer

    def get(self, request, format=None):
        quizs = Quiz.objects.filter(date_end__gte=date.today())
        quiz_s = QuizSerializer(quizs, many=True)
        return Response(quiz_s.data)

    def get_queryset(self):
        pass

class GetAnswer(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswersSerializer

    def get(self, request, user_code, format=None):
        answers = Answer.objects.filter(user_code=user_code)
        answers_s = AnswersSerializer(answers, many=True)
        return Response(answers_s.data)

    def get_queryset(self):
        pass

class QuestionAnswer(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswerSerializer

    def post(self, request, format=None):
        answer = AnswerSerializer(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer.save()
            return Response({'result': 'OK'})