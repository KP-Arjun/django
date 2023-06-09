from . import views
from django.urls import path,include

urlpatterns = [
    
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('bookings', views.booking,name="bookings"),
    path('doctors', views.doctors,name="doctors"),
    path('contact', views.contact,name="contact"),
    path('department',views.department,name="dep"),
]