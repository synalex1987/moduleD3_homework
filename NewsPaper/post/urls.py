from django.urls import path
from .views import PostList, PostDetail, NewsList, NewsDetail

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('news/', NewsList.as_view()),
    path('news/<int:pk>', NewsDetail.as_view()),
]
