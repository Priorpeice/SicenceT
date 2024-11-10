from django.urls import path , include

from config import settings
from oauth.views.googleLogin import GoogleLogin
from .views import google_login, google_callback
from .views.googleOauthCallbackView import GoogleOAuthCallbackView

urlpatterns = [
    # path('google/login/', google_login, name='google_login'),
    path("google/callback/", GoogleOAuthCallbackView.as_view(), name="api_accounts_google_oauth_callback"),
    path('google/login/', GoogleLogin.as_view(), name='google_login_todjango'),
]
