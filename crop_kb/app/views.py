from django.shortcuts import render, redirect, HttpResponse
from django.core import serializers
from .models import Crop, Ftime, Ftype, Farming

# Create your views here.

def index(request):
    if request.method == 'POST':
        crop = request.POST.get('crop')
        ftime = request.POST.get('time')
        ftype = request.POST.get('type')
        print(crop, ftime, ftype)
        keys = {}
        if crop:
            keys['crop__crop'] = crop
        if ftime:
            keys['ftime__ftime'] = ftime
        if ftype:
            keys['ftype__ftype'] = ftype
        farmings = Farming.objects.filter(**keys)
        message = crop+ftime+ftype
        return render(request, 'index.html', {'farmings': farmings, 'message':message})
    else:
        farmings = Farming.objects.all()
        # json_data = serializers.serialize("json", farmings)
        # return HttpResponse(json_data, content_type="application/json")
        return render(request, 'index.html', {'farmings':farmings, 'message':'所有农事'})