#! /usr/bin/python

import getopt, sys
from pyPdf import PdfFileWriter, PdfFileReader

def usage ():
    print """sjvr767\'s PDF Cropping Script.
Example:
my_pdf_crop.py -s -p 0.5 -i input.pdf -o output.pdf
my_pdf_crop.py --skip --percent 0.5 -input input.pdf -output output.pdf
\n
REQUIRED OPTIONS:
-p\t--percent
The factor by which to crop. Must be positive and less than or equal to 1.

-i\t--input
The path to the file to be cropped.
\n
OPTIONAL:
-s\t--skip
Skip the first page. Ouptut file will not contain the first page of the input file.

-o\t--output
Specify the name and path of the output file. If none specified, the script appends \'cropped\' to the file name.
"""
    sys.exit(0)

def cut_length(dictionary, key, factor):
	cut_factor = 1-factor
	cut = dictionary[key]*cut_factor
	cut = cut / 4
	return cut
	
def new_coords(dictionary, key, cut):
	return abs(dictionary[key]-cut)

try:
	opts, args = getopt.getopt(sys.argv[1:], "sp:i:o:s", ["skip", "percent=", "input=", "output="])
except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

skipone = 0

for a in opts[:]:
	if a[0] == '-s' or a[0]=='--skip':
		skipone = 1

factor = 0.8 #default scaling factor

for a in opts[:]:
	if a[0] == '-p' or a[0]=='--factor':
		if a[1] != None:
			try:
				factor = float(a[1])
			except TypeError:
				print "Factor must be a number."
				sys.exit(2) #exit if no appropriate input file

input_file = None #no defualt input file
		
for a in opts[:]:
	if a[0] == '-i' or a[0]=='--input':
		if a[1] != None:
			try:
				if a[1][-4:]=='.pdf':
					input_file = a[1]
				else:
					print "Input file must be a PDF."
					sys.exit(2) #exit if no appropriate input file
			except TypeError:
				print "Input file must be a PDF."
				sys.exit(2) #exit if no appropriate input file
			except IndexError:
				print "Input file must be a PDF."
				sys.exit(2) #exit if no appropriate input file
		else:
			print "Please speicfy an input file."
			sys.exit(2) #exit if no appropriate input file

output_file = "%s_cropped.pdf" %input_file[:-4] #default output

for a in opts[:]:
	if a[0] == '-o' or a[0]=='--output': 
		if a[1]!= None:
			try:
				if a[1][-4:]=='.pdf':
					output_file = a[1]
				else:
					print "Output file must be a PDF."
			except TypeError:
				print "Output file must be a PDF."
			except IndexError:
				print "Output file must be a PDF."


input1 = PdfFileReader(file(input_file, "rb"))

output = PdfFileWriter()
outputstream = file(output_file, "wb")

pages = input1.getNumPages()

top_right = {'x': input1.getPage(1).mediaBox.getUpperRight_x(), 'y': input1.getPage(1).mediaBox.getUpperRight_y()}
top_left = {'x': input1.getPage(1).mediaBox.getUpperLeft_x(), 'y': input1.getPage(1).mediaBox.getUpperLeft_y()}
bottom_right = {'x': input1.getPage(1).mediaBox.getLowerRight_x(), 'y': input1.getPage(1).mediaBox.getLowerRight_y()}
bottom_left = {'x': input1.getPage(1).mediaBox.getLowerLeft_x(), 'y': input1.getPage(1).mediaBox.getLowerLeft_y()}

cut = cut_length(top_right, 'x', factor)

new_tr = (new_coords(top_right, 'x', cut), new_coords(top_right, 'y', cut))
new_br = (new_coords(bottom_right, 'x', cut), new_coords(bottom_right, 'y', cut))
new_tl = (new_coords(top_left, 'x', cut), new_coords(top_left, 'y', cut))
new_bl = (new_coords(bottom_left, 'x', cut), new_coords(bottom_left, 'y', cut))

if skipone == 0:
	for i in range(0, pages):
		page = input1.getPage(i)
		page.mediaBox.upperLeft = new_tl
		page.mediaBox.upperRight = new_tr
		page.mediaBox.lowerLeft = new_bl
		page.mediaBox.lowerRight = new_br
		output.addPage(page)
else:
	for i in range(1, pages):
		page = input1.getPage(i)
		page.mediaBox.upperLeft = new_tl
		page.mediaBox.upperRight = new_tr
		page.mediaBox.lowerLeft = new_bl
		page.mediaBox.lowerRight = new_br
		output.addPage(page)

output.write(outputstream)
outputstream.close()
