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
    start_urls = [
        'https://vieclam24h.vn/tim-kiem-ung-vien-nhanh/?hdn_tu_khoa=&hdn_nganh_nghe_cap1=&hdn_dia_diem=&gioi_tinh_ntd=&ngoai_ngu_ntd=&thoi_gian_ntd=',
    ]

    def request(self, url, callback):
        """
         wrapper for scrapy.request
        """
        request = scrapy.Request(url=url, callback=callback)
        request.cookies['PHPSESSID'] = "aj2v61sti9p5ugpu4to21i08n1"
        request.cookies['SVID'] = "w61"
        request.cookies['USER'] = "a%3A5%3A%7Bs%3A11%3A%22pk_taikhoan%22%3Bs%3A7%3A%225116530%22%3Bs%3A16%3A%22c_loai_tai_khoan%22%3Bs%3A1%3A%221%22%3Bs%3A15%3A%22c_ten_dang_nhap%22%3Bs%3A21%3A%22vanhuy.hust%40gmail.com%22%3Bs%3A16%3A%22c_chuoi_xac_nhan%22%3Bs%3A8%3A%22verified%22%3Bs%3A19%3A%22c_chuoi_xac_nhan_mk%22%3Bs%3A10%3A%22WIN5be2fc2%22%3B%7D"
        request.cookies['USER_REMEMBER'] = "374819b2bd6f2215e12f5f71ce773f82%2F5bf1283e"
        request.cookies['_ga'] = "GA1.2.822880323.1536126275"
        request.cookies['gate'] = "ntd"
        request.cookies['uid'] = 5116530
        request.headers['User-Agent'] = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
        return request

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield self.request(url, self.parse)

    def parse(self, response):
        for tn in response.xpath('//*[@id="cols-right"]/div[1]/div[2]/div/div[1]/div/div'):
            src = tn.xpath('div/div[2]/span[1]/a/@href').extract_first()
            src = response.urljoin(src)
            yield self.request(src, callback=self.parse_src)
        next_pages = response.xpath('//li[@class="next"]/a/@href').extract()
        next_page = next_pages[len(next_pages) - 1]
        print("LOG")
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_src(self, response):
        self.item = CandidateItem()
        self.item["url"] = response.request.url

        title = response.xpath(
            '//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/div[1]/div/div/h2/text()').extract()
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
            self.item["objective"] = objective[0].strip()

        sex = response.xpath(
            '//*[@id="cols-right"]/div/div[2]/div[4]/div[1]/div[2]/div/div[1]/p[5]/span[2]/text()').extract()
        if len(sex) > 0:
            self.item["sex"] = sex[0].strip()

        if self.item["title"] != "":
            yield self.item