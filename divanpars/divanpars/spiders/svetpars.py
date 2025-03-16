import scrapy


class SvetparsSpider(scrapy.Spider):
    name = "svetpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://divan.ru/category/svet"]

    def parse(self, response):
        lamps = response.css("div._Ud0k")
        for lamp in lamps:
            yield {
                "name": lamp.css('span[itemprop="name"]::text').get(),
                "price": lamp.css('meta[itemprop="price"]::attr(content)').get(),
                "url": lamp.css("a").attrib["href"]
            }
