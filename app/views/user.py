from app.models.user import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..serializers import UserSerializer

# jwt 토근 인증 확인용 뷰셋
# Header - Authorization : Bearer <발급받은토큰>

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer