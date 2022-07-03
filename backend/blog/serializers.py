from rest_framework.serializers import ModelSerializer, IntegerField
from django.contrib.auth.models import User
from .models import Post, Category


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = UserSerializer(read_only=True)
    category_id = IntegerField(write_only=True)
    author_id = IntegerField(write_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'category', 'body', 'post_date', 'author_id', 'category_id']



    #def create(self, validated_data):
    #    author_id = validated_data.pop('author_id')
    #    category_id = validated_data.pop('category_id')
    #    post = Post.objects.create(author_id=author_id, category_id=category_id, **validated_data)
    #    return post