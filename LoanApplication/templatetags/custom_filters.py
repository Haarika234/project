# templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Add a class to a form field."""
    return field.as_widget(attrs={'class': css_class})
