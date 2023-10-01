from django.db import models

class card(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=300)

    def __str__(self):
        return self.name+ " "+ self.description


