from django import template

register = template.Library()

@register.simple_tag
def calc_total_duration(shifts):  # here 'shifts' is the 'user.list' in the template
    total = 0.0
    for shift in shifts:
        total += shift.duration
    return total
    