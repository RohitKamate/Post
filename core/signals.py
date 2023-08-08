# blog/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Post

@receiver(post_save, sender=Post)
def send_notification_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Post Created'
        message = f'Hello {instance.author},\n\nA new post titled "{instance.title}" has been created.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [instance.author.email]
        send_mail(subject, message, from_email, recipient_list)
