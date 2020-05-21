from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    # sending static content
    #dest1 = Destination()
    #dest1.name = 'Mumbai'
    #dest1.price = 800
    #dest1.des = 'The city of dreams !'
    #dest1.img = 'destination_1.jpg'
    #dest1.offer = False

    #dest2 = Destination()
    #dest2.name = 'Delhi'
    #dest2.price = 400
    #dest2.des = 'The city that never sleeps'
    #dest2.img = 'destination_2.jpg'
    #dest2.offer = True

    #dest3 = Destination()
    #dest3.name = 'Jaipur'
    #dest3.price = 600
    #dest3.des = 'The city of nawabs'
    #dest3.img = 'destination_3.jpg'
    #dest3.offer = False

    #dests = [dest1, dest2, dest3]

    #for dynamic content from admin page
    dests = Destination.objects.all()

    return render(request, "index.html", {'dests' : dests})