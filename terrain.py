from django.test import Client
from lettuce import before, world
from django.core.management import call_command


@before.harvest
def initial_setup(server):
    call_command('syncdb', interactive=False, verbosity=0)


@before.all
def set_browser():
    world.browser = Client()

