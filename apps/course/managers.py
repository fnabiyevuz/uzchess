from django.db import models


class CourseQueryset(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def top(self):
        return self.active().filter(is_top=True)


class CourseManager(models.Manager.from_queryset(CourseQueryset)):  # type: ignore
    pass
