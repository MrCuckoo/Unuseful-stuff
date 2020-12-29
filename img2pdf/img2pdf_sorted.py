#coding=utf-8
#!/usr/bin/env python

#本脚本原用于windows环境，Linux环境未测试

import img2pdf 
import os
from openpyxl import load_workbook
#import xlrd

def topdf(imgpath):
	#pdfpath = r"root\path\to\img\pdffiles"
	pdfpath = os.path.join(imgpath, 'pdffiles')
	pdfname = pdfpath

	g = os.walk(imgpath)
	for root, _, file_list in g:
		fname = []
		### 使用openpyxl库
		xlsfname = os.path.join(root, 'sort.xlsx')
		### 使用xlrd库, 更新后的xlrd库不支持xlsx格式, 因此需要将后缀改为.xls
		# xlsfname = os.path.join(root, 'sort.xls')
		if not os.path.exists(xlsfname):
			for i in range(len(file_list)):
				if os.path.splitext(file_list[i])[-1] in ['.jpg', 'jpeg', 'png']:
					fname.append(os.path.join(root, file_list[i]))
		else:
			### 使用openpyxl库
			wb = load_workbook(xlsfname, read_only = True)
			sheet = wb.worksheets[0]
			for row in sheet.rows:
				fname.append(os.path.join(root, row[1].value))
			wb.close()

			### 使用xlrd库
			# sheet = xlrd.open_workbook(xlsfname).sheet_by_index(0)
			# for id in range(sheet.nrows):
			# 	fname.append(os.path.join(root, sheet.cell_value(id, 1)))

		if fname == []:
			continue
		
		pdfname = root.replace(imgpath, pdfpath) + '.pdf'
		if pdfname == pdfpath + '.pdf':
			pdfname = os.path.join(pdfpath, os.path.split(pdfname)[-1])
		pdffpath = os.path.split(pdfname)[0]
		if not os.path.exists(pdffpath):
			os.makedirs(pdffpath)
		
		if os.path.exists(pdfname) and os.path.getsize(pdfname):
			continue

		### A4纸规格设置
		### 强制将图片按比例缩放到A4纸规格(不建议使用该设置)
		a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
		layout_fun = img2pdf.get_layout_fun(a4inpt)

		with open(pdfname, 'wb') as f:
			f.write(img2pdf.convert(fname, layout_fun = layout_fun))
			# f.write(img2pdf.convert(fname))
			print(pdfname, 'Created')

def main():
	imgpath = r"root\path\to\img"
	topdf(imgpath)

if __name__ == "__main__":
	main()
