from celery import shared_task
from .models import Stock

@shared_task
def check_stock_levels():
    low_stocks = Stock.objects.filter(quantity__lt=models.F('min_quantity'))
    for stock in low_stocks:
        print(f"Запас товара {stock.product.name} ниже минимального уровня! Количество: {stock.quantity}.")
