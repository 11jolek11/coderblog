from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



@receiver(post_save, User)
def set_permissions():
    pass
