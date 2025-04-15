from behave import *
from app.main import app

def before_all(context):
    context.app = app.test_client()

def after_all(context):
    pass
