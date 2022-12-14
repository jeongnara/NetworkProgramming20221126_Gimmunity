from django.urls import path

from notice.views import NoticeListView, NoticeDetailView

app_name = 'notice'

urlpatterns = [
    path('', NoticeListView.as_view(), name='list'),
    path('detail/<int:pk>/', NoticeDetailView.as_view(), name='detail')
]