from rest_framework import serializers


from .models import *
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


    def validate(self,value):
            slug = value.get('slug')
            if ' ' in slug:
                raise serializers.ValidationError('Slug Url should not contain spaces instead use -')
            return value
