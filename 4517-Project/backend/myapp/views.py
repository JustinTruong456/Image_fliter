from django.shortcuts import get_object_or_404, render, HttpResponse

from.models import Oringal
from.models import Fliter
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, "index.html")

@csrf_exempt  # Only use this if you're skipping CSRF for now
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('myFile'):
        image = request.FILES['myFile']
        Oringal_img = Oringal(image=image)
        Oringal_img.save()
        return JsonResponse({'message': 'Upload successful'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def update_filtered_image(request):
    if request.method == 'POST' and request.FILES.get('filtered_image'):
        image_fliter = request.FILES['filtered_image']
        Fliter_img = Fliter(image_fliter=image_fliter)
        Fliter_img.save()
        return JsonResponse({'message': 'Download successful'})
    return JsonResponse({'error': 'Invalid request'}, status=400)