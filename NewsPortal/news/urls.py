from django.urls import path
#имортируем созданное нами представление
from .views import NewsList, NewsDetail


urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('<int:pk>/', NewsDetail.as_view(), name='post_detail'),
]
