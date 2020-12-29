#coding=utf-8
#!/usr/bin/env python

import img2pdf 
import os

def topdf(imgpath):
	pdfpath = os.path.join(imgpath, 'pdffiles')
	#pdfpath = r'root\path\to\img\pdffiles'

	g = os.walk(imgpath)
	for root, dir_list, file_list in g:
		for fname in file_list:
			if fname.endswith(('.jpg', '.jpeg', '.png')):
				imgfname = os.path.join(root, fname)
				
				pdffname = imgfname.replace(imgpath, pdfpath)
				pdffname = pdffname.replace(os.path.splitext(pdffname)[-1], '.pdf')

				pdffpath = os.path.split(pdffname)[0]
				if not os.path.exists(pdffpath):
					os.makedirs(pdffpath)
				
				with open(pdffname, 'wb') as f:
					f.write(img2pdf.convert(imgfname))
					print(imgfname, "to", pdffname, " Done")

def main():
	imgpath = r"root\path\to\img"
	topdf(imgpath)

if __name__ == "__main__":
	main()