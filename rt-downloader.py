import urllib
import time

class RTDownloader(object):
    """
    Real-time downloader of financial data in a continuous loop, with 10 minute waiting interval
    """

    symbol_file_name = "NYSE.txt"

    url_fmt = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s"
    output_file_fmt = '''/media/gerardsimons/WD/Documents/Big Stock
                        /downloader/data/realtime/out%d.csv'''

    def __init__(self, interval, symbols, special_tags):
        self.counter = 0
        self.sleep_interval = interval
        self.symbols = symbols
        self.special_tags = special_tags

    def start():
        self.start_time = time.time()

        while True:
            self.download_stock_data()
            sleep(self.sleep_interval)


    # Download most current stock data available
    def download_stock_data(self):
        """
        Download the latest stock data for the given symbols, with the given special tags.
        :param symbol: A list of stock symbols of which we want the financial data
        :param special_tags: The special tags string, see
        https://greenido.wordpress.com/2009/12/22/yahoo-finance-hidden-api/
        for more information
        """
        print "Downloading round %d. Elapsed time = %f" % (self.counter,time.time() - self.start_time)
        print "Attempting to download real-time stocks with special tags '%s' interval = %s" % (special_tags)

        symbol_string = ""
        for symbol in symbols:
            symbol_string += symbol + "+"

        symbol_string = symbol_string[:-1] # remove last '+'
        url = url_fmt % (symbol_string,special_tags)

        output = output_file_fmt % self.counter

        print "Fetching from '%s'" % (url)
        print "Writing to file '%s'" % (output_path)

        urllib.urlretrieve (url, output_path + "/" + symbol + "_" + interval + ".csv")

        self.counter += 1

    def main():
        # Load the symbols list, each line is a symbol
        symbols = list()
        with open(symbol_file_name,'r') as f:
            for line in f:
                symbols.append(line)

        specialtags = "snd1l1yr"
        symbols = ["MSFT","GOOG","GE"] # Microsoft, Google and General Electric

        RTDownloader()








if __name__ == '__main__':
    main()
