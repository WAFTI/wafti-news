from django.test import Client
from lettuce import before, world


@before.all
def set_browser():
    world.browser = Client()

