from django.core.management.base import BaseCommand
import requests
import json

class Command(BaseCommand):
    help = 'Loads data from the API'

    def handle(self, *args, **options):
        response = requests.get('https://data.calgary.ca/resource/99yf-6c5u.json')

        if response.status_code == 200:
            data = json.loads(response.text)

            for item in data:
                print(item)
        else:
            self.stdout.write(self.style.ERROR(f'API request failed with status code {response.status_code}'))
