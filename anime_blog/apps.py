from django.apps import AppConfig


class AnimeBlogConfig(AppConfig):
    """
    Provides primary key type for blog app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anime_blog'
