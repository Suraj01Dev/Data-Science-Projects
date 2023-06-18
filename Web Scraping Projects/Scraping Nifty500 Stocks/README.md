# **Web Scraping Nifty 500 Stocks using Scrapy Python**
- Scraped Nifty 500 Stock Ratios for Fundamental Analysis.
- Created a Spider in Scrapy to Crawl [Moneycontrol](https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7) Webpage to get the Ratios.
- Parsed and tabulated `500 rows x 176 cols` into the `nifty500.csv`.

## **How to download the project ?**
- Copy the project [link](https://github.com/Suraj01Dev/Data-Science-Projects/tree/main/Web%20Scraping%20Projects/Scraping%20Nifty500%20Stocks/nifty500_scraper).
- Head to the https://download-directory.github.io/ to download a particular project inside a repo.
- Paste the link and download the zip.

## **Prerequisites to run the project**
- Python3 should be installed.
- Scrapy should be installed.
  
  ```
  pip install scrapy 
  ```
## **How to run the project ?**
- After downloading the project unzip the archive.
- Navigate inside the nifty500_scraper directory.
- Open a terminal session and execute the below command to start scraping.
  
  ```
  scrapy crawl niftyspider -o nitfy500.csv
  ```
- The data will be scraped and will be stored in nifty500.csv which can be used for further analysis.
