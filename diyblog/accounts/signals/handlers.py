from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission



@receiver(post_save, sender=User)
def set_permissions(sender, instance, **kwargs):
    can_publish = Permission.objects.get(codename="can_publish")
    can_comment = Permission.objects.get(codename='can_comment')

    instance.user_permissions.add(can_publish)
    instance.user_permissions.add(can_comment)
