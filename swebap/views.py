from django.shortcuts import render
from .models import Products

# Create your views here.'
def indexpage(request):
    
    #prodone = Products()
    #prodone.name = "Chennai"
    #prodone.desc = "Chennai is the capital of tamilnadu. City with busy peope"
    #prodone.image = "image_1.jpeg"
    #prodone.musttry = False
    
    #prodtwo = Products()
    #prodtwo.name = "Pondicherry"
    #prodtwo.desc = "City of enjoyment"
    #prodtwo.image = "image_2.jpeg"
    #prodtwo.musttry = False
     
    #prodthree = Products()
    #prodthree.name = "Madurai"
    #prodthree.desc = "City of culture. Good tamil people"
    #prodthree.image = "image_3.jpeg"
    #prodthree.musttry = True
    
    #prodfour = Products()
    #prodfour.name = "Tirunelveli"
    #prodfour.desc = "This is talented city"
    #prodfour.image = "image_4.jpeg"
    #prodfour.musttry = False
    
    #products = [prodone, prodtwo, prodthree, prodfour]
    
    products = Products.objects.all()
    
    return render(request, 'index.html', {'prods': products})
