from django.db import models


class Weather(models.Model):
    location = models.TextField()
    description = models.TextField()
    temperature = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"LOCATION: {self.location}, "
            f"DESCRIPTION: {self.description}, "
            f"TEMPERATURE: {self.temperature}, "
            f"DATE: {self.created_at}; "
        )
