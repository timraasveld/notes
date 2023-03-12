from django.contrib.auth.models import User
from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'body', 'updated_at']
