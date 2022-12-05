from django.conf import settings


def get_api_url(url: str) -> str:
    return f"api/v{settings.API_VERSION}/{url}/"
