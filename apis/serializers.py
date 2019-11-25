from rest_framework import serializers
from accounts.models import CustomUser
from sites.models import Site


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'bio', 'telephone', 'avatar' )
        

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('id', 'title', 'author', 'description', 'cover', 'link','tags', 'created_at' )
        