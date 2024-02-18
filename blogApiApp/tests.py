from django.test import TestCase
import requests


# Create your tests here.

requests = requests.get('http://localhost:8000')

print(requests.json())