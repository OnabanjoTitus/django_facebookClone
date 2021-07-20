from django.urls import path

from Posts.views import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view()),
]
