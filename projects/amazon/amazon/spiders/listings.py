import scrapy


class ListingsSpider(scrapy.Spider):
    name = 'listings'
    start_urls = ['https://quotes.toscrape.com/']

    # return the source code of the website
    def parse(self, response):
        title = response.css('title').extract()
        yield {'titleText': title}
