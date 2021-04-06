from django import template
from blood import views as v

register = template.Library()

@register.filter
def decrypt(value):
    return v.decrypt(
        full_name=value
    )