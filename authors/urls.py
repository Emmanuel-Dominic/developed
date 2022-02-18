from django.urls import path
from .views import CreateCompanyAPIView

urlpatterns = [
    path('company/', CreateCompanyAPIView.as_view()),
    # path('company/<name>', CreateCompanyAPIView.as_view()),
]
