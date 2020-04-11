import scrapy
from ..items import QuotestutorialItem
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        all_div = response.css('div.quote')
        for div in all_div:
            title = div.css(".text::text").extract()
            author = div.css('.author::text').extract()
            tags = div.css('.tag::text').extract()
            item = QuotestutorialItem(title=title, author=author, tags=tags)

            # yield {
            #     'title': title,
            #     'author': author,
            #     'tags': tags
            # }
            yield item

        next_page = response.css("li.next a::attr(href)").get()
        print(next_page)

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


