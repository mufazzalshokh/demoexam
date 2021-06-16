from django.urls import path

from detail.views import HomeListView

app_name = 'detail'

urlpatterns = [
    path('', HomeListView.as_view(), name='list')
]
