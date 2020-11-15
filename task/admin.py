from django.contrib import admin
from .models import Company, Worker

# Models in AdminPage
admin.site.register(Company)
admin.site.register(Worker)