import scrapy
from ..items import AmazonItem


class ListingsSpider(scrapy.Spider):
    name = 'listings'
    start_urls = ['https://quotes.toscrape.com/']

    # return the source code of the website
    def parse(self, response):
        # title = response.css('title::text').extract()
        # yield {'titleText': title}  # yeild is a type of return here

        all_listings = response.css('div.quote')

        # instance of items class
        items = AmazonItem()

        for x in all_listings:  # for loop to organise the data of all listings
            title = x.css('span.text::text').extract()
            author = x.css('.author::text').extract()
            tag = x.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
