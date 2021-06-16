from django.urls import path

from home.views import NewsListView, NewsDetailView

app_name = 'home'

urlpatterns = [
    path('', NewsListView.as_view(), name='news'),
    path('detail/<int:pk>/', NewsDetailView.as_view(), name='detail'),
]
