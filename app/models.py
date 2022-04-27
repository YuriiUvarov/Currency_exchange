from django.db import models


class Rate(models.Model):
    current_time = models.DateTimeField(auto_now_add=True)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)

    class PossibleSource(models.IntegerChoices):
        PRIVATBANK = 1, 'Privatbank'
        MONOBANK = 2, 'Monobank'
        VKURSE = 3, 'Vkurse'

    source = models.PositiveIntegerField(default=PossibleSource.PRIVATBANK, choices=PossibleSource.choices)

    class PossibleCurrency(models.IntegerChoices):
        UAH = 1, 'UAH'
        USD = 2, 'USD'
        EUR = 3, 'EUR'
        YUAN = 4, 'CNY'
        GOLD = 5, 'XAU'

    currency_type = models.PositiveIntegerField(default=PossibleCurrency.USD, choices=PossibleCurrency.choices)
