from django.urls import path
from .views import PostView

app_name = 'post'
urlpatterns = [
    path('<int:pk>/', PostView.as_view(), name='blog_post'),
]
