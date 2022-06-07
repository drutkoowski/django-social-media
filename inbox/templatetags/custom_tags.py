from django import template

from accounts.models import UserProfile
from ..models import Notification

register = template.Library()

@register.inclusion_tag('inbox/show_notifications.html', takes_context=True)
def show_notifications(context):
	request_user = context['request'].user
	user_profile = UserProfile.objects.filter(user=request_user).first()
	notifications = Notification.objects.filter(to_user=user_profile).exclude(user_has_seen=True).order_by('-date')
	return {'notifications': notifications}