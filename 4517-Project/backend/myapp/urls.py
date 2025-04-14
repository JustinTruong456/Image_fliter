from django.urls import path
from . import views
from .views import upload_image
from .views import update_filtered_image

urlpatterns = [
    path("", views.home, name="home"),  
    path('upload/', upload_image, name='upload_image'),
    path('update_filtered_image/', update_filtered_image, name='update_filtered_image')
]

