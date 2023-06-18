from rest_framework import serializers
from news.models import Article, AppUser, Comment
from datetime import datetime, date
from django.utils.timesince import timesince

class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['article']

class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    time_since_pub = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.publication_date
        if object.active == True:
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return 'Not active!'
    
    def validate_publication_date(self, datevalue):
        today = date.today()
        if datevalue > today:
            raise serializers.ValidationError('Publication date can not be a future date!')
        return datevalue
    
class AppUserSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='article-detail',
    )
    class Meta:
        model = AppUser
        fields = '__all__'





