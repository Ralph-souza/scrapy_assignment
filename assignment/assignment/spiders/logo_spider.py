import os
import scrapy
import logging
import re

dirname = os.path.dirname(__name__)
filename = os.path.join(dirname, "/scrapy_assignment/assignment")

logger = logging.getLogger(__name__)


class LogoSpider(scrapy.Spider):
    name = "logo"

    def start_requests(self):
        urls = open("/home/ralph/Udemy/scrapy_assignment/url_list.txt")
        for logo in urls:
            yield scrapy.Request(url=logo, callback=self.parse)

    def parse(self, response, **kwargs):
        logo_pattern = r"(https?:\/\/.*\.(?:svg))"
        for logo in response.css("img").xpath("@src").getall():
            logo_match = re.match(logo_pattern, logo)
            if logo_match is not None:
                yield {"logo": logo}
            else:
                logger.warning("Unable to scrap website Logo URL")
