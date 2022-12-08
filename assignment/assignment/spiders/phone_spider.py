import scrapy
import logging

logger = logging.getLogger(__name__)


class PhoneSpider(scrapy.Spider):
    name = "phone"

    def start_requests(self):
        urls = open("/home/ralph/Udemy/scrapy_assignment/url_list.txt")
        for phone in urls:
            yield scrapy.Request(url=phone, callback=self.parse)

    def parse(self, response, **kwargs):
        search = response.xpath('//span/text()').re(r"\+?\d{0,9}\s?\(?\+?\d{0,9}?\)?\s?[-., \s]?\d{0,9}[-., \s]?\d{0,9}?")
        print(search)
        for phone in search:
            if phone:
                yield {"phone": phone}
