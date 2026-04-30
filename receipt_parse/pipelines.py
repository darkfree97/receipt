import os
import django
from core.models import MeasurementUnit, Product
from receipt_parse.items import ReceiptItem

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "receipt.settings")
django.setup()


class DjangoWriterPipeline:
    def process_item(self, item: ReceiptItem, spider):
        for ingredient in item['ingredients']:
            measurement, created = MeasurementUnit.objects.get_or_create(
                name=ingredient['unit'],
                short_name=ingredient['unit']
            )
            product, created = Product.objects.get_or_create(
                name=str(ingredient['name']).lower().capitalize(),
                measurement=measurement
            )
        return item