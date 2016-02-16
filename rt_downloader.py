"""
Download real-time stock data from the Yahoo Finance API
"""
import urllib
import time

SYMBOL_FILE_NAME = "NYSE.txt"
URL_FMT = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s"
OUTPUT_FILE_FMT = '/media/gerardsimons/WD/Documents/Big Stock/downloader/data/realtime/out%d.csv'
MAX_SYMBOLS = 10

class RTDownloader(object):
    """
    Real-time downloader of financial data in a continuous loop, with 10 minute waiting interval
    """

    start_time = None

    def __init__(self, interval, symbols, special_tags):
        self.counter = 0
        self.sleep_interval = interval
        self.symbols = symbols
        self.special_tags = special_tags

    def start(self):
        '''
        Commence downloading. Downloading will be done in an infinite while loop,
        requring manual interruption to stop.
        '''
        if self.start_time is not None:
            raise Exception("Downloader already started!")
        self.start_time = time.time()

        while True:
            self.download_stock_data()
            time.sleep(self.sleep_interval)

    def download_stock_data(self):
        """
        Download the latest stock data for the given symbols, with the given special tags.
        The data is returned in CSV format, where each row is a stock symbol.
        Each special tag becomes a column
        :param symbol: A list of stock symbols uniquely identifying a listed stock
        :param special_tags: The special tags string, that indicate the data types
        https://greenido.wordpress.com/2009/12/22/yahoo-finance-hidden-api/
        for more information.
        """

        interval = time.time() - self.start_time
        print "Downloading round %d. Elapsed time = %f" % (self.counter, interval)
        print "Download real-time stocks with special tags '%s'" % (self.special_tags)

        # Create a plus sign separated string from all the symbols
        symbol_string = "+".join(self.symbols)

        url = URL_FMT % (symbol_string, self.special_tags)

        output_path = OUTPUT_FILE_FMT % self.counter

        print "Fetching from '%s'" % (url)
        print "Writing to file '%s'" % (output_path)

        urllib.urlretrieve(url, output_path)

        self.counter += 1



def main():
    """
    Main function
    """

    # Load the symbols list, each line is a symbol
    symbols = list()
    with open(SYMBOL_FILE_NAME, 'r') as symbol_file:
        for line in symbol_file:
            # print line.split('\t')
            symbols.append(line.split('\t')[0])

    print "Read %d symbols." % len(symbols)

    # specialtags = "snd1l1yr"
    # Use ALL the special tags!
    special_tags = """sa2a5bb2b3b4b6cc1c3c6c8dd1d2ee1e7e8e9f6ghjkg1
    g3g4g5g6ii5j1j3j4j5j6k1k2k3k4k5ll1l2l3mm2m3m4m5m6m7m8nn4opp1p
    2p5p6qrr1r2r5r6r7s1s7t1t6t7t8vv1v7ww1w4xy"""

    # symbols = ["MSFT", "GOOG", "GE"] # Microsoft, Google and General Electric

    # Start downloading data for the symbols at 10 minute intervals
    # downloader = RTDownloader(6000, symbols, special_tags)
    # downloader.start()


# When explicitly calling this script
if __name__ == '__main__':
    main()
