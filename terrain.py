from django.test import Client
from lettuce import before, world, after
from django.core.management import call_command
from splinter import Browser


@before.harvest
def initial_setup(server):
    call_command('syncdb', interactive=False, verbosity=0)


@before.all
def set_browser():
    world.browser = Browser('phantomjs')

@after.all
def close_browser(_):
    world.browser.quit()
