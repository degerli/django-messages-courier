from django.apps import AppConfig


class OnesignalEmailConfig(AppConfig):
    name = 'courier.emails.providers.onesignal'
    label = 'onesignal-email'

    def ready(self):
        import courier.emails.providers.onesignal.signals
