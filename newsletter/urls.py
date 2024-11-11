from django.urls import path
from .views import HomePageView, News2, Main_news, Newslist

app_name = 'newsletter'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add_news/', News2.as_view(), name='news'),
    path('detail_/<int:pk>/', Main_news.as_view(), name='det'),
    path('done/', Newslist.as_view(), name='new'),
]