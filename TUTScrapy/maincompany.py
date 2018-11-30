from scrapy import cmdline
cmdline.execute("scrapy crawl company -o company-new.json".split())