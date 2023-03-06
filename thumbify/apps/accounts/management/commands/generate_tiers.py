from django.core.management.base import BaseCommand
from apps.accounts.models import AccountTier


class Command(BaseCommand):
    help = "Generates account tiers"

    def handle(self, *args, **options):
        tiers = [
            {
                "name": "Basic",
                "thumbnail_sizes": "200",
                "include_original_link": False,
                "generate_expiring_link": False,
            },
            {
                "name": "Premium",
                "thumbnail_sizes": "200,400",
                "include_original_link": True,
                "generate_expiring_link": False,
            },
            {
                "name": "Enterprise",
                "thumbnail_sizes": "200,400",
                "include_original_link": True,
                "generate_expiring_link": True,
            },
        ]

        for tier in tiers:
            AccountTier.objects.get_or_create(name=tier["name"], defaults=tier)

        self.stdout.write(self.style.SUCCESS("Tiers created successfully!"))
