from django.db import models

class Option(models.Model):
    OPTION_TYPES = (
        ('call', 'Call'),
        ('put', 'Put'),
    )

    option_type = models.CharField(max_length=4, choices=OPTION_TYPES)
    underlying_price = models.FloatField()
    strike_price = models.FloatField()
    volatility = models.FloatField()
    time_to_maturity = models.FloatField()
    risk_free_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.option_type.capitalize()} Option"

