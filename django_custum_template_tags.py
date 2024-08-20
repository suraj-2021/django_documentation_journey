import datetime
from django import template

register = template.Library()

@register.simpletag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


