import scrapy
import logging
import re

logger = logging.getLogger(__name__)


class AddressSpider(scrapy.Spider):
    name = "address"

    def start_requests(self):
        urls = open("/home/ralph/Udemy/scrapy_assignment/url_list.txt")
        for address in urls:
            yield scrapy.Request(url=address, callback=self.parse)

    def parse(self, response, **kwargs):
        address_pattern = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
        address = response.xpath("//a/@href").get()
        address_match = re.match(address_pattern, address)
        if address_match is not None:
            yield {"website": address}
        else:
            logger.warning("Unable to scrap website URL")
