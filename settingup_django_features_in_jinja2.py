from jinja2 import Environment as Jinja2Environment
from jinja2.ext import Extension
from django.templatetags.static import static
from django.urls import reverse

class Environment(Jinja2Environment):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.globals.update({
            'static': static,
            'url': reverse,
        })
