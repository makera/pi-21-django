from datetime import datetime

from django.db import models


class Course(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    date_start = models.DateField(verbose_name='Дата начала', default=datetime.today)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Theme(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='themes', verbose_name='Курс')
    name = models.CharField(verbose_name='Название', max_length=100)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['course', 'id']

    def __str__(self):
        return "{} - {}".format(self.course.name, self.name)

# Create your models here.
