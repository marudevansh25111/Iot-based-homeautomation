from django.db import models

# Create your models here.
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    class Meta:
        db_table="firstdbtest_student"
    