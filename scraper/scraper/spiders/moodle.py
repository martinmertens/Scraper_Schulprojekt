import scrapy


class MoodleSpider(scrapy.Spider):
    name = 'moodle'
    allowed_domains = ['moodle']
    start_urls = ['http://moodle/']

    def parse(self, response):
        pass
