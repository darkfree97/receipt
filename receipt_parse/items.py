# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReceiptItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    ingredients = scrapy.Field()
    steps = scrapy.Field()

    def __str__(self):
        return self['title']


class IngredientItem(scrapy.Item):
    name = scrapy.Field()
    quantity = scrapy.Field()
    unit = scrapy.Field()

    def __str__(self):
        return f"{self['name']} - {self['quantity']} {self['unit']} "


class StepItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    priority = scrapy.Field()

    def __str__(self):
        return self['title']
