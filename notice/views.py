from django.shortcuts import render
from django.views.generic import ListView

from notice.models import Notice


class NoticeListView(ListView):
    model = Notice

