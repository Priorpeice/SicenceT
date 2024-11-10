import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from urllib.parse import unquote
class GoogleOAuthCallbackView(APIView):
    def get(self, request):
        # URL에서 'code' 파라미터 추출
        if code := request.GET.get("code"):
            response = self.forward_code_to_google_login_view(code)
            if response.status_code == 200:
                return Response(response.json(), status=status.HTTP_200_OK)
            return Response(
                {"error": "Failed to process with GoogleLoginView"},
                status=response.status_code,
            )

        return Response(
            {"error": "Code not provided"}, status=status.HTTP_400_BAD_REQUEST
        )

    def forward_code_to_google_login_view(self, code: str):
        url = "http://localhost:8000/api/user/google/login/"  # 실제 Google 로그인 처리 API
        decoded_code = unquote(code)
        payload = {"code": decoded_code}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        return response
