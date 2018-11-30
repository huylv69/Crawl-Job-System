# encoding: utf-8
import scrapy
from TUTScrapy.job import JobItem
import re


class ViecLam24hSpider(scrapy.Spider):
    name = "vieclam24h"
    start_urls = [
        'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh/?hdn_nganh_nghe_cap1=&hdn_dia_diem=&hdn_tu_khoa=&hdn_hinh_thuc=&hdn_cap_bac=',
    ]

    def parse(self, response):
        for tn in response.xpath('//div[@class="list-items "]/div/div/span'):
            src = tn.xpath('a/@href').extract_first()
            src = response.urljoin(src)
            yield scrapy.Request(src, callback=self.parse_src)

        next_pages = response.xpath('//li[@class="next"]/a/@href').extract()
        next_page = next_pages[len(next_pages) - 1]
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_src(self, response):
        self.item = JobItem()
        self.item["url"] = response.request.url

        title = response.xpath(
            '//div[@class="col-xs-12"]/h1[@class="text_blue font28 mb_10 mt_20 fws title_big"]/text()').extract()
        if len(title) > 0:
            self.item["title"] = title[0]
        else:
            self.item["title"] = ""

        salary = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/p[1]/span/span/text()').extract()
        if len(salary) > 0:
            self.item["salary"] = salary[0]

        experience = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/p[2]/span/span/text()').extract()
        if len(experience) > 0:
            self.item["experience"] = experience[0]

        diploma = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/p[3]/span/span/text()').extract()
        if len(diploma) > 0:
            self.item["diploma"] = diploma[0]

        amount = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/p[4]/span/span/text()').extract()
        if len(amount) > 0:
            self.item["amount"] = amount[0]

        career = response.xpath('//*[@id="cols-right"]/div/div[1]/div[2]/ul/li[4]/a/span/text()').extract()
        if len(career) > 0:
            self.item["career"] = career[0]

        address = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[2]/p[1]/span/a/text()').extract()
        if len(address) > 0:
            self.item["address"] = address[0]

        position = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[2]/p[2]/span/span/text()').extract()
        if len(position) > 0:
            self.item["position"] = position[0]

        category = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[2]/p[3]/span/span/text()').extract()
        if len(category) > 0:
            self.item["category"] = category[0]

        month = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[2]/p[4]/span/text()').extract()
        print(month)
        if "gian thử việc" in month[0]:
            time = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[2]/p[4]/span/span/text()').extract()
            if len(time) > 0:
                self.item["time_trial"] = time[0]

            sex = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[2]/p[5]/span/span/text()').extract()
            if len(sex) > 0:
                self.item["sex"] = sex[0]

            age = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[2]/p[6]/span/span/text()').extract()
            if len(age) > 0:
                self.item["age"] = age[0]
        else:
            sex = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[2]/p[4]/span/span/text()').extract()
            if len(sex) > 0:
                self.item["sex"] = sex[0]

            age = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[2]/p[5]/span/span/text()').extract()
            if len(age) > 0:
                self.item["age"] = age[0]

        description = response.xpath('//*[@id="ttd_detail"]/div[1]/div[2]/div[1]/p/text()').extract()
        if len(description) > 0:
            # self.item["description"] = description[0].strip()
            des = ' '.join(description).strip()
            self.item["description"] = "\n".join(des.splitlines())

        benefits = response.xpath('//*[@id="ttd_detail"]/div[1]/div[2]/div[2]/p/text()').extract()
        if len(benefits) > 0:
            des = ' '.join(benefits).strip()
            self.item["benefits"] = "\n".join(des.splitlines())

        require_skill = response.xpath('//*[@id="ttd_detail"]/div[1]/div[2]/div[3]/p/text()').extract()
        if len(require_skill) > 0:
            des = ' '.join(require_skill).strip()
            self.item["require_skill"] = "\n".join(des.splitlines())

        person = response.xpath('//*[@id="ttd_detail"]/div[2]/div[2]/p/text()').extract()
        addre = response.xpath('//*[@id="ttd_detail"]/div[2]/div[3]/p/text()').extract()
        self.item["contact"] = "NGƯỜI LIÊN HỆ: " + person[0].strip() + " \n " + "ĐỊA CHỈ LIÊN HỆ: " + addre[0].strip()

        company = response.xpath('//*[@id="cols-right"]/div/div[2]/div[1]/div/p/a/text()').extract()
        if len(company) > 0:
            self.item["company"] = company[0]

        created = response.xpath('//*[@id="cols-right"]/div/div[2]/div[2]/div[1]/p/span[3]/text()').extract()
        if len(created) > 0:
            self.item["created"] = created[0][14:]

        expired = response.xpath('//*[@id="cols-right"]/div/div[2]/div[2]/div[1]/span/span/span/span/text()').extract()
        if len(expired) > 0:
            self.item["expired"] = expired[0]

        if self.item["title"] != "":
            yield self.item
