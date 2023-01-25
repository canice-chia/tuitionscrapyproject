from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst


class TuitionAssignmentLoader(ItemLoader):
    default_output_processor = TakeFirst()
    level_subject_in = MapCompose(lambda x: x.strip())