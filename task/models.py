from django.db import models


# связи между компаниями

class Company(models.Model):
    # Name of the company
    company_name = models.CharField('Название компании', max_length=128)

    def __str__(self):
        return self.company_name

class Worker(models.Model):
    # Information about worker
    worker_name = models.CharField('Имя', max_length=128)
    worker_position = models.TextField('Занимаемая должность', blank=True, null=True)
    worker_age = models.CharField('Возраст', max_length=3)
    name_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.worker_name