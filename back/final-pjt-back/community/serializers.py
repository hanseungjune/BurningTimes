from rest_framework import serializers
from .models import Review, Comment

class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'

class ChildCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)

class CommentSerializer(serializers.ModelSerializer):
    childcomment = ChildCommentSerializer(many=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)

class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='commentst.count', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('comment_set', 'comment_count',)

# class CommentListSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Comment
#         fields = '__all__'
