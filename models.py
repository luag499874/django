from pro_gol.db import models

# Create your models here.
class Task(models.Model):
    title = models.ChardField(max_length=100)
    description = models.models.TextField(black=True)