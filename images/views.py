from django.shortcuts import render
import requests
from django.http import HttpResponse,JsonResponse
from .models import Image
import random
# Create your views here.

data = requests.get("https://pixabay.com/api/?key=14050053-dcccfba7708bef01bd85af3e8&per_page=200&q=food")

class_list_width = ['w-1','w-2','w-3']
class_list_height = ['h1','h-2','h-3']

def indexView(request):
  json_data = data.json()

  for image in json_data['hits']:

    Image.objects.update_or_create(image_type=image['type'],tag=image['tags'],webformatURL=image['webformatURL'],views=image['views'],downloads=image['downloads'],likes=image['likes'],user=image['user'],userimageURL=image['userImageURL'])
     
  
  images = Image.objects.all()
  for image in images:
    image.width_class = random.choice(class_list_width)
    image.height_class = random.choice(class_list_height)
    
  return render(request,'images/index.html',context={
    "images" : images,

    
  })


def detailsView(request,pk):
  image = Image.objects.filter(id=pk).values()
  image = list(image)
  return render(request,'images/details.html',context= {'image':image})
  

  