# encoding: utf-8
import scrapy
from TUTScrapy.candidate import CandidateItem
from scrapy.http import FormRequest, Request
from scrapy.spiders.init import InitSpider


class CandidateSpider(InitSpider):
    name = "candidate"
    crawl = [
        'https://vieclam24h.vn/tim-kiem-ung-vien-nhanh/?hdn_tu_khoa=&hdn_nganh_nghe_cap1=&hdn_dia_diem=&gioi_tinh_ntd=&ngoai_ngu_ntd=&thoi_gian_ntd=',
    ]

    login_page = ('https://vieclam24h.vn/taikhoan/login?referral_url=aHR0cHM6Ly92aWVjbGFtMjRoLnZuL25oYS10dXllbi1kdW5n')
    start_urls = [
        'https://vieclam24h.vn/tim-kiem-ung-vien-nhanh/?hdn_tu_khoa=&hdn_nganh_nghe_cap1=&hdn_dia_diem=&gioi_tinh_ntd=&ngoai_ngu_ntd=&thoi_gian_ntd=',
    ]

    def init_request(self):
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        print
        "Preparing Login"
        return FormRequest.from_response(
            response,
            formdata={'password': 'Vanhuy96',
                      'username': 'vanhuy.hust@gmail.com',
                      'loai_tai_khoan': '1',
                      'is_change_pass': '0'},
            callback=self.after_login,
            dont_filter=True,
        )

    def after_login(self, response):
        print("alo",response.cookies.values())

        self.initialized()


    # def parse(self, response):
    #     return FormRequest.from_response(response,
    #                                      formdata={'password': 'Vanhuy96',
    #                                                'username': 'vanhuy.hust@gmail.com',
    #                                                'loai_tai_khoan': '1',
    #                                                'is_change_pass': '0'},
    #                                      callback=self.scrape_pages)
    #
    # def scrape_pages(self, response):
    #     print("alo", response)
    #     return Request(
    #         url='https://vieclam24h.vn/tim-kiem-ung-vien-nhanh/?hdn_tu_khoa=&hdn_nganh_nghe_cap1=&hdn_dia_diem=&gioi_tinh_ntd=&ngoai_ngu_ntd=&thoi_gian_ntd=',
    #         callback=self.parse_page)

    def parse(self, response):
        for tn in response.xpath('//div[@class="list-items "]/div/div/span'):
            src = tn.xpath('a/@href').extract_first()
            src = response.urljoin(src)
            yield scrapy.Request(src, callback=self.parse_src)

        next_pages = response.xpath('//li[@class="next"]/a/@href').extract()
        next_page = next_pages[len(next_pages) - 1]
        print("LOG")
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_page)

    def parse_src(self, response):
        self.item = CandidateItem()
        self.item["url"] = response.request.url

        title = response.xpath(
            '//div[@class="col-xs-12"]/h1[@class="text_blue font28 mb_10 mt_20 fws title_big"]/text()').extract()
        if len(title) > 0:
            self.item["title"] = title[0]
        else:
            self.item["title"] = ""

        salary = response.xpath(
            '//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/div[2]/div/div[2]/p[4]/span[2]/text()').extract()
        if len(salary) > 0:
            self.item["salary"] = salary[0]

        experience = response.xpath(
            '//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/div[2]/div/div[1]/p[2]/span[2]/text()').extract()
        if len(experience) > 0:
            self.item["experience"] = experience[0]

        diploma = response.xpath(
            '//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/div[2]/div/div[1]/p[3]/span[2]/text()').extract()
        if len(diploma) > 0:
            self.item["diploma"] = diploma[0]

        career = response.xpath(
            '//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/div[2]/div/div[2]/p[3]/a/text()').extract()
        if len(career) > 0:
            self.item["career"] = career[0]

        address = response.xpath(
            '//*[@id="cols-right"]/div/div[2]/div[1]/div/div/div[2]/div[2]/span[2]/text()').extract()
        if len(address) > 0:
            self.item["address"] = address[0]

        position = response.xpath(
            '//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/div[2]/div/div[2]/p[1]/span[2]/text()').extract()
        if len(position) > 0:
            self.item["position"] = position[0]

        category = response.xpath(
            '//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/div[2]/div/div[2]/p[5]/span[2]/text()').extract()
        if len(category) > 0:
            self.item["category"] = category[0]

        language = response.xpath(
            '//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/div[2]/div/div[1]/p[4]/span[2]/text()').extract()
        if len(language) > 0:
            self.item["language"] = language[0].strip()

        objective = response.xpath('//*[@id="cols-right"]/div/div[2]/div[4]/div[2]/text()').extract()
        if len(objective) > 0:
            self.item["benefits"] = objective[0].strip()

        sex = response.xpath(
            '//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/div[2]/div/div[1]/p[5]/span[2]/text()').extract()
        if len(sex) > 0:
            self.item["require_skill"] = sex[0].strip()

        if self.item["title"] != "":
            yield self.item

