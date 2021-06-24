from django import template

register = template.Library()


@register.simple_tag(name='profile_create_or_display')
def profile_create_or_display(user):
    print(user)
    profile_set = user.userprofile_set.all()
    print(profile_set)
    return not profile_set.exists()
