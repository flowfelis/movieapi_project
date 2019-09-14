from rest_framework import serializers

from movieapi.models import Movie, Comment


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

        # {
        #     "id": 2,
        #     "total_comments": 6,
        #     "rank": 1
        # },


class TopSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    total_comments = serializers.IntegerField()
    rank = serializers.IntegerField()
