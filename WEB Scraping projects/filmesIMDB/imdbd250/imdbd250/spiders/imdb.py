import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for filme in response.css('.titleColumn'):
            yield {
                'nomeFilme': filme.css('.titleColumn a::text').get(),
                'anoFilme': filme.css('.secondaryInfo::text').get()[1:-1],
                'avaliacaoFilme': response.css('strong::text').get()
            }

        pass
