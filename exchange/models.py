from django.db import models

class ExchangePrice(models.Model):
    data=models.DateTimeField('Дата публікації')
    company=models.CharField('Ціна',max_length=230)
    typeOfProposition = models.CharField('Тип пропозиції', max_length=20)
    culture = models.CharField('Культура', max_length=20)
    volume= models.CharField("Об'єм", max_length=20)
    price = models.CharField('Ціна', max_length=230)
    condition = models.CharField("Умови", max_length=20)
    idcheck = models.CharField('ID:', max_length=230, blank=True)

    def __str__(self):
        return self.company

