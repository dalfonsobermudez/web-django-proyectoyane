from django.conf import settings
from django.urls import reverse


def site_contact(request):
    """Expose the public contact channels to every template."""
    whatsapp_number = settings.WHATSAPP_NUMBER
    return {
        "site_contact": {
            "whatsapp_url": (
                f"https://wa.me/{whatsapp_number}"
                if whatsapp_number
                else reverse("Contact")
            ),
            "facebook_url": settings.FACEBOOK_URL,
            "instagram_url": settings.INSTAGRAM_URL,
            "store_address": settings.STORE_ADDRESS,
            "google_maps_url": settings.GOOGLE_MAPS_URL,
            "google_maps_embed_url": settings.GOOGLE_MAPS_EMBED_URL,
        }
    }
