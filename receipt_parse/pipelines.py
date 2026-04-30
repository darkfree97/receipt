import logging
import os
import django
from receipt_parse.items import ReceiptItem

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "receipt.settings")
django.setup()
from core.models import MeasurementUnit, Product, Receipt, ReceiptProduct, ReceiptStep  # noqa


logger = logging.getLogger(__name__)


class DjangoWriterPipeline:
    async def process_item(self, item: ReceiptItem, spider):
        receipt = await Receipt.objects.acreate(
            title=item['title'],
            description=item['description']
        )

        # create receipt products
        products = []
        for ingredient in item['ingredients']:
            # create measurement unit
            measurement, created = await MeasurementUnit.objects.aget_or_create(
                name=ingredient['unit'],
                short_name=ingredient['unit']
            )
            if created:
                logger.info(f"Created measurement unit: {measurement}")

            # create product
            product, created = await Product.objects.aget_or_create(
                title=str(ingredient['name']).lower().capitalize(),
                measurement_unit=measurement
            )
            if created:
                logger.info(f"Created product: {product}")

            products.append(ReceiptProduct(
                receipt=receipt,
                product=product,
                quantity=float(ingredient['quantity'])
            ))
        await ReceiptProduct.objects.abulk_create(products)

        # create receipt steps
        steps = []
        for step in item['steps']:
            steps.append(ReceiptStep(
                receipt=receipt,
                title=step['title'],
                description=step['description'],
                priority=int(step['priority'])
            ))
        await ReceiptStep.objects.abulk_create(steps)
        logger.info(f"Created receipt: {receipt}")

        return item
