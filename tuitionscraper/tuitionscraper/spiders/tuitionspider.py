import json

import scrapy

from tuitionscraper.itemloaders import TuitionAssignmentLoader
from tuitionscraper.items import TuitionAssignment


class TuitionspiderSpider(scrapy.Spider):
    name = 'tuitionspider'
    allowed_domains = ['smiletutor-carlos.appspot.com']
    start_urls = ['https://smiletutor-carlos.appspot.com/public/v2/tuition_assignments/0']

    def parse(self, response, **kwargs):
        data = json.loads(response.text)

        for element in data['data']:
            loader = TuitionAssignmentLoader(item=TuitionAssignment(), selector=element)

            loader.add_value('job_id', element['job_id'])
            loader.add_value('time_posted', element['t'])
            loader.add_value('level_subject', element['level_subjects'])

            yield loader.load_item()

