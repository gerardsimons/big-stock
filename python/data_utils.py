import os
import sys

def concat_csv(args):
	if not len(args) or len(args) > 2:
		print "Usage : concat_csv root_path [out_path]"
		return
	root_path = args[0]
	if len(args) == 1:
		out_path = root_path + "/out.csv"
	else:
		out_path = args[1]
	os.system("cat %s/*.csv > %s" % (root_path, out_path))

methods = ['concat_csv']

def main():
	if len(sys.argv) < 1:
		print "No input arguments given"
	elif sys.argv[1] == 'concat_csv':
		concat_csv(sys.argv[2:])




if __name__ == '__main__':
	main()