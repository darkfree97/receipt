import os
import django
from core.models import Receipt
from receipt_parse.items import ReceiptItem

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "receipt.settings")
django.setup()


class DjangoWriterPipeline:
    def process_item(self, item: ReceiptItem, spider):
        print(item)
        return item