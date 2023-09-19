from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.

#homepage
@csrf_exempt
def home(request):
    all_location = Hotels.objects.values_list('location','id').distinct().order_by()
    if request.method == 'POST':
        
        try:
            hotel = Hotels.objects.all().get(id=int(request.POST['search_location']))
            print(hotel)
            return HttpResponse(hotel)
        except Exception as e:
            print(e,'kkkkkkkkk')
    response = 'lll'
    return HttpResponse(response)

    
