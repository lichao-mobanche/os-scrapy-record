# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy


class ExampleSpider(scrapy.Spider):
    """ ExampleSpider
    Auto generated by os-scrapy-cookiecuter

    Run:
        scrapy crawl example
    """

    name = "example"

    start_urls = ["http://example.com/"]
