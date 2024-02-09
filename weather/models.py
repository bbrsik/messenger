from django.db import models


class Weather(models.Model):
    location = models.TextField()
    description = models.TextField()
    temperature = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"LOCATION: {self.location}\n"
            f"DESCRIPTION: {self.description}\n"
            f"TEMPERATURE: {self.temperature}\n"
            f"DATE: {self.created_at}\n"
        )
