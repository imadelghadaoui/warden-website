from django.db import models

# Create your models here.
class StudentClass(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Classes(models.Model):
    name=models.CharField(max_length=50)
    nombre=models.IntegerField(default=0)
    id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)