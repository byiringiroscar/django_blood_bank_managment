from django.shortcuts import render
from camps.models import Hospital_service
# Create your views here.


def livebloodcamps(request):
    hospital_service = Hospital_service.objects.all()
    context = {
        'hospitals': hospital_service
    }
    return render(request, 'camps/livebloodcamps.html', context)
