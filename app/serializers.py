from dj_rest_auth.registration.serializers import RegisterSerializer as DefaultRegisterSerializer
from rest_framework import serializers

class UserRegisterSerializer(DefaultRegisterSerializer):
    name = serializers.CharField(max_length=50, write_only=True, required=True)  # 커스텀 필드 추가

    def custom_signup(self, request, user):
        # 커스텀 필드 처리
        name = self.validated_data.pop("name")
        if name:
            user.name = name
            user.save()
