# ----------------------------
# MyPipeline class defined by 
# pipelines.py
# ----------------------------
# location in directory structure:
# sads_exhibit_11_1/scrapy_application/pipelines.py

class MyPipeline(object):
    def process_item(self, item, spider):
        return item
