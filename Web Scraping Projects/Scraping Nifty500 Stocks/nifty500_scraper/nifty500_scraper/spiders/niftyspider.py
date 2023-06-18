import scrapy


class NiftyspiderSpider(scrapy.Spider):
    name = "niftyspider"
    allowed_domains = ["www.moneycontrol.com"]
    start_urls = ["https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7"]

    def parse(self, response):
        stocks=response.css('div.MT10 table.tbldata14 tr')
        stocks.pop(0)

        for stock in stocks:
            stock_link="moneycontrol.com"+stock.css("td.brdrgtgry a")[0].attrib["href"]
            yield response.follow(stock_link, callback=self.ratio_link_find)

    def ratio_link_find(self,response):
        ratio_link=response.css('div.financials_container div.sub2menu_content div.right_block div.quick_links li a')[7].attrib['href']
        yield response.follow(ratio_link, callback=self.ratio_stat_find)

    def ratio_stat_find(self,response):
        ratios={}
        stock_name=response.css('h1.pcstname::text').get()
        stage1=response.css('table.mctable1  tr')
        stage2=stage1.css('tr')


        ratios['stock_name']=stock_name


        for ratio in stage2:
            
            un_class_name=ratio.css('tr').attrib['class']


            if un_class_name=='lightbg' or un_class_name=='darkbg':
                continue
            else:
                values=ratio.css('td::text').getall()[:-1]

                ratio_name=values[0]
                for i in range(1,6):
                    if i <len(values):
                        ratios[ratio_name+"_yr"+str(i)]=values[i]
                    else:
                        ratios[ratio_name+"_yr"+str(i)]=None

        yield ratios


        



                







                         
                    


            








            

