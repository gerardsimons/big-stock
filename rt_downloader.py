"""
Download real-time stock data from the Yahoo Finance API
"""
import urllib
import time
import os
import datetime

# SYMBOL_FILE_NAME = "NYSE.txt"
DATA_ROOT = "/media/pi/WD/Documents/Big Stock/downloader/data/"
SYMBOL_FILE_NAME = DATA_ROOT + "historical/proper/symbols.txt"
URL_FMT = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s"
OUTPUT_DIR = DATA_ROOT + "realtime/"
OUTPUT_FILE_FMT = "round=%d_chunk=%d.csv"
MAX_SYMBOLS = 10

class RTDownloader(object):
    """
    Real-time downloader of financial data in a continuous loop, with 10 minute waiting interval
    """

    start_time = None

    def __init__(self, interval, symbols, special_tags):
        ''':param symbol: A list of stock symbols uniquely identifying a listed stock
        :param special_tags: The special tags string, that indicate the data types
        https://greenido.wordpress.com/2009/12/22/yahoo-finance-hidden-api/
        for more information.
        '''
        self.counter = 0
        self.sleep_interval = interval
        self.symbols = symbols
        self.special_tags = special_tags

	timestamp = str(int(time.time()))
	self.dir = OUTPUT_DIR + timestamp + "/"
	os.mkdir(self.dir)

    def download_stock_data(self, max_symbols = 400):
        """
        Download the latest stock data for the given symbols, with the given special tags.
        The data is returned in CSV format, where each row is a stock symbol.
        Each special tag becomes a column
        :param max_symbols: The maximum number of symbols to download at once, necessary to avoid too long URLs
        """

        steps = len(self.symbols) / max_symbols
        remainder = len(self.symbols) - steps * max_symbols
        symbol_chunks = [self.symbols[i*max_symbols:(i+1)*max_symbols] for i in range(steps)]

        # print out
        symbol_chunks.append(self.symbols[(steps * max_symbols):])
        chunk = 0

        print "Start download real-time stocks with special tags '%s'" % (self.special_tags)
        print "Chunks = %d x %d." % (len(symbol_chunks), len(symbol_chunks[0]))
	print "-" * 50

        start_time = time.time()

        while True:
	    chunk = 0
            for symbol_chunk in symbol_chunks:
                #print len(symbol_chunk)
                interval = time.time() - start_time

                # Create a plus sign separated string from all the symbols
                symbol_string = "+".join(symbol_chunk)
                url = URL_FMT % (symbol_string, self.special_tags)
                output_path = self.dir + OUTPUT_FILE_FMT % (self.counter, chunk)
		
		try:
                	urllib.urlretrieve(url, output_path)
		except IOError:
			time.sleep(60) # Wait a minute 
		else: # If everything went ok
			print "%s: Chunk %d.%d fetched." % (datetime.datetime.fromtimestamp(int(time.time())), self.counter, chunk)
			print "Elapsed time = %f" % interval
			print "Chunk size = %d" % len(symbol_chunk)
	                print "File path = %s" % (output_path)

        	        chunk += 1

            time.sleep(self.sleep_interval)
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
            # symbols.append(line.split('\t')[0])
            symbols.append(line[:-1])

    print "Read %d symbols." % len(symbols)

    # specialtags = "snd1l1yr"
    # Use ALL the special tags!
    special_tags = """sa2a5bb2b3b4b6cc1c3c6c8dd1d2ee1e7e8e9f6ghjkg1
    g3g4g5g6ii5j1j3j4j5j6k1k2k3k4k5ll1l2l3mm2m3m4m5m6m7m8nn4opp1p
    2p5p6qrr1r2r5r6r7s1s7t1t6t7t8vv1v7ww1w4xy"""

    # symbols = ["MSFT", "GOOG", "GE"] # Microsoft, Google and General Electric

    # Start downloading data for the symbols at 10 minute intervals
    downloader = RTDownloader(600, symbols, special_tags)
    downloader.download_stock_data()


# When explicitly calling this script
if __name__ == '__main__':
    # main()

    main()

