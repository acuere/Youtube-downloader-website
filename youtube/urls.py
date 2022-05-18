from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.index, name='index'),
    path('download', DownloadView.download, name='download'),
    path('error', ErrorView.error, name='error'),
]
