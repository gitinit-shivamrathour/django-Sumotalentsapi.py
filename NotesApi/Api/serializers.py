from rest_framework import serializers
from .models import *

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id','title','desc','audio','video']

    def __str__(self):
        return self.title