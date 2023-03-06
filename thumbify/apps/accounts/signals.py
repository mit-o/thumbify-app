from django.contrib.auth import get_user_model
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from django.core.management import call_command
from .models import AccountTier

User = get_user_model()


@receiver(pre_delete, sender=AccountTier)
def set_basic_tier(sender, instance, **kwargs):
    basic_tier = AccountTier.objects.get(name="Basic")
    instance.user_set.update(tier=basic_tier)


@receiver(post_save, sender=User)
def set_default_tier(sender, instance, created, **kwargs):
    try:
        basic_tier = AccountTier.objects.get(name="Basic")
    except AccountTier.DoesNotExist:
        call_command("generate_tiers")
    finally:
        if created and not instance.tier:
            basic_tier = AccountTier.objects.get(name="Basic")
            instance.tier = basic_tier
            instance.save()
