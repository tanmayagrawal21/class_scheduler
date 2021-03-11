from django.db import models

# Create your models here.
class Day(models.Model):
    day= models.CharField(max_length=64)

    def __str__(self):
        return self.day


class Teacher(models.Model):
    first= models.CharField(max_length=64)
    last= models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.first} {self.last}"

class Time(models.Model):
    time= models.IntegerField()

    def __str__(self):
        if(self.time>12):
            return f"{self.time-12} PM"
        else:
            return f"{self.time} AM"

class Schedule(models.Model):
    teacher= models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="session")
    time= models.ForeignKey(Time, on_delete=models.CASCADE, related_name="slot")
    day= models.ForeignKey(Day, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.teacher}      {self.day}      {self.time}"