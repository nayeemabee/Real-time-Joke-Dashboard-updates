from celery import shared_task
import random
import requests

@shared_task
def generate_random_number():
    number = random.randint(1, 100)
    print(f'Generated number: {number}')
    return number

@shared_task
def get_jokes():
    raw_data = requests.get('https://official-joke-api.appspot.com/random_joke').json()
    print(raw_data)
    joke = raw_data["setup"] + raw_data["punchline"]
    print('generated joke:', joke)
    return joke