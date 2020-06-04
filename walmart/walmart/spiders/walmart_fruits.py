# -*- coding: utf-8 -*-
import scrapy
from ..items import WalmartItem


class WalmartFruitsSpider(scrapy.Spider):
    name = 'walmart_fruits'
    # allowed_domains = ['walmart.ca']
    start_urls = ['https://www.walmart.ca/en/grocery/fruits-vegetables/fruits/N-3852'
                  ]


    def parse(self, response):
        items = WalmartItem()

        barcode = response.css('.e1cuz6d14+ .e1cuz6d11 .e1cuz6d13').css('::text').extract()
        sku = response.css('.e1cuz6d11:nth-child(6) .e1cuz6d13').css('::text').extract()
        brand = response.css('.e1cuz6d11:nth-child(3) .e1cuz6d13').css('::text').extract()
        name = response.css('.thumb-header::text').extract()
        package = response.css('.description').css('::text').extract()
        description = response.css('.e1mpbtcv2').css('::text').extract()
        image_URL = response.css('.centered-img-wrap::attr(src)').extract()
        # URL = 'https://www.walmart.ca/en/ip/banana/875805'.extract()
        price = response.css('.price-current div::text').extract()

        items['barcode'] = barcode
        items['sku'] = sku
        items['brand'] = brand
        items['name'] = name
        items['description'] = description
        items['package'] = package
        items['image_URL'] = image_URL
        # items['URL'] = URL
        items['price'] = price

        yield items
