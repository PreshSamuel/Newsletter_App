from django.urls import path
from .views import HomePage, NewsletterView, NewsList

app_name = 'newsletter'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add_news/', NewsletterView.as_view(), name='newsletter_view'),
    path('news_list/', NewsList.as_view(), name='news_list'),
]