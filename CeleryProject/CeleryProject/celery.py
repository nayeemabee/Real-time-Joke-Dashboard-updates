from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryProject.settings')

app = Celery('CeleryProject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    

from celery.schedules import crontab

app.conf.beat_schedule = {
    'generate-number-every-3-seconds': {
        'task': 'joke.tasks.generate_random_number',
        'schedule': 5.0,
    },
    
    'generate-joke-every-30-seconds': {
        'task': 'joke.tasks.get_jokes',
        'schedule': 30.0,
    },
}

