from django.db import models


class MeasurementUnit(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва")
    short_name = models.CharField(max_length=10, verbose_name="Коротка назва")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Одиниці вимірювання"
        verbose_name = "Одиниця вимірювання"


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва")
    code = models.CharField(max_length=255, verbose_name="Код")
    measurement_unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE, verbose_name="Одиниця вимірювання")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Продукти"
        verbose_name = "Продукт"


class Receipt(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    products = models.ManyToManyField(Product, verbose_name="Продукти")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Рецепти"
        verbose_name = "Рецепт"


class StockItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Ціна")
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Кількість")
    expiration_date = models.DateField(null=True, blank=True, verbose_name="Термін придатності")
    out_of_stock = models.BooleanField(default=False, verbose_name="Відсутність")
    purchase = models.ForeignKey("Purchase", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Покупка")

    def __str__(self):
        return f"{self.product.title} - {self.amount}"

    class Meta:
        verbose_name_plural = "Запаси"
        verbose_name = "Запас"


class Purchase(models.Model):
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Магазин")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Загальна ціна")
    date = models.DateField(verbose_name="Дата")

    def __str__(self):
        return f"Purchase on {self.date} - Total: ${self.total_price}"

    class Meta:
        verbose_name_plural = "Покупки"
        verbose_name = "Покупка"


class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Адреса")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Магазини"
        verbose_name = "Магазин"
