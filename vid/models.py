from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=200)
    video=models.FileField(upload_to='video/%y')
    demo=models.BooleanField(default=False)
    cat=models.CharField(max_length=300)
    def __str__(self):
        return self.name
    