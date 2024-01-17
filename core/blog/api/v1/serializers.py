from rest_framework import serializers
from ...models import Post, Category
# from ....accounts.models import Profile


# class PostSerializer(serializers.Serializer):
#     id = serializers.ImageField()
#     title = serializers.CharField(max_length=255)
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['author']


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'snippet', 'status', 'relative_url', 'created_date',
                  'published_date']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        rep.pop('snippet', None)
        return rep

    # def create(self, validated_data):
    #     validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
    #     return super().create(validated_data)
