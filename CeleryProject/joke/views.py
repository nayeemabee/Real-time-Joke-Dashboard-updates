from django.shortcuts import render
from django.http import JsonResponse
from .tasks import get_jokes

def indexpage(request):
    return render(request, 'index.html')

def fetch_joke(request):
    joke = get_jokes.delay().get()  # Trigger the Celery task and get the joke
    return JsonResponse({'joke': joke})
