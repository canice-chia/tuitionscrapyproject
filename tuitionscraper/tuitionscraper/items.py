# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TuitionAssignment(scrapy.Item):
    job_id = scrapy.Field()
    time_posted = scrapy.Field()
    level_subject = scrapy.Field()
