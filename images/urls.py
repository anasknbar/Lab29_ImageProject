from django.urls import path
from .views import indexView,detailsView

urlpatterns = [
  path('',indexView,name='index'),
  path('<int:pk>',detailsView,name='image_details')
]