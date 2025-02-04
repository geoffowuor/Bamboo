from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.admin),
    path('book/', views.booking, name="book"),
    path('reserve/', views.reserve, name="reserve"),
    path('reserved!/', views.reservation_success, name="reservation_success"),
    path('booked!/', views.booking_success, name="booking_success"),
    
    
]









#media handler 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    