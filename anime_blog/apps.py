from django.apps import AppConfig


class AnimeBlogConfig(AppConfig):
    """
    Configures the 'anime_blog' application.

    Sets the default auto_field type for models in this app to
    'django.db.models.BigAutoField'.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anime_blog'
