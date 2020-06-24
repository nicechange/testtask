from rest_framework import serializers
from .models import Answer, Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['pk', 'title', 'lock_other', ]

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, source='choice_set', )
    class Meta:
        model = Question
        fields = ['pk', 'title', 'choices', ]

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_set', )
    class Meta:
        model = Question
        fields = ['pk', 'title', 'questions', ]

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['pk', 'question', 'choices', 'answr',  ]


class AnswerSerializer(serializers.Serializer):
    answers = serializers.JSONField()
    def validate_answers(self, answers):
        if not answers:
            raise serializers.Validationerror("Answers must be not null.")
        return answers

    def save(self):
        answers = self.data['answers']
        for answr in answers:
            question = Question.objects.get(pk=answr['question'])
            try:
                choices = answr['choices']
            except:
                pass
            user_code = answr['user_code']
            if question.type == 'text':
                Answer(user_code=user_code, question=question, answr=answr['answr']).save()
            elif (question.type == 'one_choice') or (question.type == 'many_choices'):
                answ = Answer(user_code=user_code, question=question)
                answ.save()
                answ.choices.set(choices)
                for choice in choices:
                           answ.answr += ' ' + Choice.objects.get(pk=choice).title
                           answ.save()

