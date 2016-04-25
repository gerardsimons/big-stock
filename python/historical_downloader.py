'''
Downloading historical financial data using finance Yahoo API
'''
import urllib
import os

import time

#### THIS IS NOT WORKING ANYMORE....... check URL below,
##   s is symbol, b,c and d are start date, efg is end date, g is interval (d is daily)

URL_FMT = "http://ichart.finance.yahoo.com/table.csv?s=WU&a=01&b=19&c=2010&d=01&e=28&f=2010&g=d&ignore=.csv"
OUTPUT_DIR = '/media/gerardsimons/WD/Documents/Big Stock/downloader/data/historical/'
# OUTPUT_DIR = '/home/gerardsimons/Desktop/test/'
OUTPUT_FILE_FMT = '%s_%s.csv'

class HistoricalDownloader(object):
    """
    Historical Financial EOD (end-of-day) stock data downloader from Yahoo
    """

    def __init__(self, symbol_file_name, interval):
        self.interval = interval
        self.symbols = list()
        with open(symbol_file_name,'r') as symbol_file:
            for line in symbol_file:
                symbol = line.split("\t")[0]
                print symbol
                self.symbols.append(symbol)

    # Download historical EOD (end-of-day) financial data at set intervals
    def download(self):
        raise Exception("This ")
        for symbol in self.symbols:
            print "Attempting to download stock '%s' interval = %s" % (symbol, self.interval)
            url = URL_FMT % (symbol, self.interval)
            output_path = OUTPUT_DIR + OUTPUT_FILE_FMT % (symbol, self.interval)
            urllib.urlretrieve (url, output_path)

def verify(path):
    ''' Verify the downloaded data and reported on invalid CSV files '''

    proper_csvs = list()
    improper_csvs = list()

    for _, _, files in os.walk(path):
        for file_name in files:
            if file_name[-4:] == '.csv':
                with open(path + file_name,'r') as csv_file:
                    print "Opened file " + file_name
                    first_line = csv_file.readline().lower()
                    if first_line.find("<!doctype html") == 0:
                        # print file_name + " is not a proper CSV, but an HTML file."
                        pass
                    else:
                        print file_name + " IS a proper CSV."
                        # os.rename(path + file_name, path + "/proper/" + file_name)




def main():
    # start_time = time.time()
    # interval = 'd'
    # downloader = HistoricalDownloader("NYSE.txt", interval)
    # downloader.download()
    # end_time = time.time()
    # print "Finished downloading historical data (%f s.)" % (end_time - start_time)

    verify(OUTPUT_DIR)


if __name__ == '__main__':
    main()
