import urllib
import time

class HistoricalDownloader(object):
    """
    Historical Financial EOD (end-of-day) stock data downloader from Yahoo
    """

    symbol_file_name = "NYSE.txt"

    url_fmt = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s"
    output_file_fmt = '''/media/gerardsimons/WD/Documents/Big Stock
                        /downloader/data/realtime/out%d.csv'''

    # sleep_interval = 6000 # = 10 minutes
    sleep_interval = 6 # seconds

    counter = 0
    start_time = None

    def add_param(url,paramName,paramValue):
        return url + paramName + ""

    # Download historical EOD (end-of-day) financial data at set intervals
    def download(symbol,interval):
        print "Attempting to download stock '%s' interval = %s" % (symbol,interval)
        url = base_url % (symbol,interval)
        urllib.urlretrieve (url, output_path + "/" + symbol + "_" + interval + ".csv")

    def main():
        # Load the symbols list, each line is a symbol
        interval = 'd'
        with open(symbol_file_name,'r') as f:
            for line in f:




if __name__ == '__main__':
    main()
