from questions.models import Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('title', 'questionID','question', 'image', 'hint1', 'hint2', 'hint3', 'hint4')
