from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movies
# Create your views here.
def index(request):
    webpages_list = Movies.objects.order_by('expectation').reverse()
    date_dict = {'Movies':webpages_list}
    return render(request,'index.html',context=date_dict)