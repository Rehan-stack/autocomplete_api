from django.shortcuts import render
from .models import Name
from django.http import JsonResponse
# Create your views here.

def get_names(request):
    search = request.GET.get('search')

    payload = []
    if search:
        objs = Name.objects.filter(name__startswith = search)


        for obj in objs:
          payload.append(
            {'name':obj.name}
        )

    return JsonResponse({
        'status':True,
        'payload':payload
    })




