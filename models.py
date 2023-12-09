from django.db import models

class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    course_title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=50)
    capacity = models.IntegerField(default=30)
    open_seats = models.IntegerField(default=30)

    def _str_(self):
        return self.course_id + " - " + self.course_title