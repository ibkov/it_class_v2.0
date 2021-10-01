from django.apps import AppConfig


class DaytaskConfig(AppConfig):
    name = 'daytask'

    def ready(self):
        from daytask import checkActiveTask
        checkActiveTask.start()
