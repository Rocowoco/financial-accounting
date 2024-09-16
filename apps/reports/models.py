from django.db import models
from django.conf import settings
from apps.transactions.models import Transaction

class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transactions = models.ManyToManyField(Transaction)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Отчет для {self.user} с {self.start_date} по {self.end_date}"
