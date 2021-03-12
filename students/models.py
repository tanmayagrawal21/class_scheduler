from django.db import models
from teachers.models import Day, Time
# Create your models here.
'''
class Day(models.Model):
    day= models.CharField(max_length=64)

    def __str__(self):
        return self.day

class Time(models.Model):
    time= models.IntegerField()

    def __str__(self):
        if(self.time>12):
            return f"{self.time-12} PM"
        else:
            return f"{self.time} AM"
'''
class Student(models.Model):
    first= models.CharField(max_length=64)
    last= models.CharField(max_length=64)
    standard= models.IntegerField(default=0)
    board= models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.first} {self.last} ({self.standard} {self.board})"



class StudentSchedule(models.Model):
    student= models.ForeignKey(Student, on_delete=models.CASCADE, related_name="session")
    time= models.ManyToManyField(Time)
    day= models.ManyToManyField(Day)

    def __str__(self):
        retval=f"{self.student}--->"
        retval+="Timings: "
        for thistime in self.time.all():
            retval+=f"{thistime} "
        retval+="\t ;"
        for thisday in self.day.all():
            retval+=f"{thisday} "
        return retval
