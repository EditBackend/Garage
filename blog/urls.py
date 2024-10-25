from django.urls import path
from .views import index,contact,detail
urlpatterns = [
    path('', index,name='index'),
    path('contact/', contact, name = 'contact'),
    path('detail/<int:id>', detail, name='detail')

]




