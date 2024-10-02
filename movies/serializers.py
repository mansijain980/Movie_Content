# movies/serializers.py
from rest_framework import serializers
from .models import Moviescontent

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moviescontent
        fields = '__all__'  # This will include all fields from the Movie model

