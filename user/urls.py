from django.urls import path
from .views import home, LogoutView
from user.login.views import LoginView
from user.register.views import RegisterView, activate
from user.resetpassword.views import forgotPassword, resetpassword_validate, resetPassword

urlpatterns = [
    path('', home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('forgotPassword/', forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', resetPassword, name='resetPassword'),
]
