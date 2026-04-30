import json

import scrapy
from scrapy.http.response import Response

from receipt_parse.items import ReceiptItem, StepItem, IngredientItem


class RecipesSpider(scrapy.Spider):
    name = "recipies"

    def start_requests(self):
        yield scrapy.Request(
            "https://sf-ecom-api.silpo.ua/v1/recipes?limit=10&offset=0",
            callback=self.parse,
            meta={"offset": 0}
        )

    def parse(self, response: Response):
        data = json.loads(response.body.decode())
        for item in data["items"]:
            yield scrapy.Request(
                f"https://sf-ecom-api.silpo.ua/v1/recipe/{item['slug']}",
                callback=self.parse_item
            )

        current_offset = response.meta["offset"]
        next_offset = current_offset + 10

        if current_offset <= data["total"]:
            yield scrapy.Request(
                f"https://sf-ecom-api.silpo.ua/v1/recipes?limit=10&offset={next_offset}",
                callback=self.parse,
                meta={"offset": next_offset},
            )

    @staticmethod
    def parse_item(response: Response):
        data = json.loads(response.body.decode())
        yield ReceiptItem(
            title=data["title"],
            description=data["description"],
            ingredients=[
                IngredientItem(
                    name=ingredient["name"],
                    quantity=ingredient["measure"]["quantity"],
                    unit=ingredient["measure"]["unit"],
                )
                for ingredient in data["ingredients"]
            ],
            steps=[
                StepItem(
                    title=step["title"],
                    description=step["description"],
                    priority=step["priority"],
                )
                for step in data["steps"]
            ],
        )
