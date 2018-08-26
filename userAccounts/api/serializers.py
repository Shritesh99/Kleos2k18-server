from rest_framework import serializers

from userAccounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
                'username',
                'email',
                'first_name',
                'last_name',
                'profile',
                'college',
                'rank',
                'level'
                )
