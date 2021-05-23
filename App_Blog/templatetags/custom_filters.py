from django import template

register = template.Library() # Registering the template

def range_filter(value):
    return value[0:600] + ("....")

# Now register the filter
register.filter('range_filter', range_filter)