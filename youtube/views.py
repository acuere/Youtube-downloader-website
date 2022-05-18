from django.shortcuts import render
from django.views.generic import View
from pytube import *


# Create your views here.

class HomePageView(View):
    def index(request):
        template_name = 'index.html'
        return render(request, template_name)

    success_url = '/'


class DownloadView():
    def download(request):
        if request.method == 'POST':
            link = request.POST['link']
            video = YouTube(link)

            stream = video.streams.get_highest_resolution()
            stream.download()

            return render(request, 'download.html')
        return render(request, 'download.html')


class ErrorView():
    def error(request):
        return render(request, 'error.html')
