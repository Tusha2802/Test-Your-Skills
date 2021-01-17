from django.db import models

# Create your models here.
class Student(models.Model):
     test_cat=(('1','CS'),('2','MATHS'),('3','GK'))
     ans_cat=(('1','1'),('2','2'),('3','3'),('4','4'))
     
     question =models.CharField(max_length=100)
     category=models.CharField(max_length=1,choices=test_cat)
     ans1=models.CharField(max_length=20)
     ans2=models.CharField(max_length=20)
     ans3=models.CharField(max_length=20)
     ans4=models.CharField(max_length=20)
     corrans=models.CharField(max_length=1,choices=ans_cat)
     class Meta:
          db_table="Student";
          
class User(models.Model):
     name=models.CharField(max_length=20)
     email=models.EmailField()
     password=models.CharField(max_length=20)
     class Meta:
          db_table="User"
          
class Login(models.Model):
     username=models.CharField(max_length=20)
     password=models.CharField(max_length=20)
     class Meta:
          db_table="Login"


class Result(models.Model):
     userid=models.CharField(max_length=3)
     date=models.DateField()
     stream=models.CharField(max_length=20)
     result=models.CharField(max_length=5)
     class Meta:
          ordering=('-date',)
          db_table="Result";
