from django.shortcuts import render
from django.views.generic import ListView, DetailView

from notice.models import Notice


class NoticeListView(ListView):
    model = Notice

class NoticeDetailView(DetailView):
    model = Notice


