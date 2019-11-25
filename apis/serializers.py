from rest_framework import serializers
from accounts.models import CustomUser
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'bio', 'telephone', 'avatar' )
        