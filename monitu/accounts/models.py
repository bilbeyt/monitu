from django.db import models
from django.contrib.auth.models import User


GRADES = (
    (4.0, 'AA'),
    (3.5, 'BA'),
    (3.0, 'BB'),
    (2.5, 'CB'),
    (2.0, 'CC'),
    (1.5, 'DC'),
    (1.0, 'DD'),
    (0.0, 'FF')
)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    terms_passed = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.user.email


class Term(models.Model):
    year = models.PositiveSmallIntegerField()
    semester = models.CharField(max_length=15)
    total_credit = models.FloatField()
    given_credit = models.FloatField()
    average = models.FloatField()

    def __str__(self):
        return str(self.year) + " " + self.semester


class Course(models.Model):
    owner = models.OneToOneField(Account, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    course_id = models.CharField(max_length=7)
    course_name = models.CharField(max_length=50)
    course_credits = models.FloatField()
    course_grade = models.FloatField(choices=GRADES)
    course_comments = models.TextField()

    def __str__(self):
        return self.course_id + " " + self.course_name
