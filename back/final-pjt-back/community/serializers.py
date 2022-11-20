from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie
# from movies.serializers import MovieListSerializer

class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie','user',)

class ChildCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)

class CommentSerializer(serializers.ModelSerializer):
    childcomment = ChildCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review','movie',)

class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('comment_set', 'comment_count',)
        # read_only_fields = (

class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('reviews', )

# class CommentListSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Comment
#         fields = '__all__'
