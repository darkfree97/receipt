from django.db import models


class MeasurementUnit(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Одиниці вимірювання"
        verbose_name = "Одиниця вимірювання"


class Product(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    measurement_unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Продукти"
        verbose_name = "Продукт"


class Receipt(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Рецепти"
        verbose_name = "Рецепт"


class StockItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    out_of_stock = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.title} - {self.amount}"

    class Meta:
        verbose_name_plural = "Запаси"
        verbose_name = "Запас"


class Purchase(models.Model):
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(StockItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Purchase on {self.date} - Total: ${self.total_price}"

    class Meta:
        verbose_name_plural = "Покупки"
        verbose_name = "Покупка"


class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Магазини"
        verbose_name = "Магазин"
