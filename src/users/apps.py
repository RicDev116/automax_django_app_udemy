from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    #this methos is called when the app is ready
    #this ensure that the signals are imported when the app is ready
    #this avoid circular imports
    #this is a good practice to import signals in the ready method of the app config
    def ready(self):
        import users.signals
