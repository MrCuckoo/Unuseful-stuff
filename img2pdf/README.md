# img2pdf
图片批量转换成PDF


img2pdf_sorted.py  
	根据图片同级目录下的sort.xlsx中图片顺序排序，将排序后的图片合并到以文件夹名命名的同一张PDF文件里，如果转换图片文件夹目录下有图片，合并后的PDF默认为转换文件夹(pdffiles)下的pdffiles.pdf
	如果sort.xlsx文件不存在，将以图片默认排序进行pdf生成  
	# 已知问题  
		合并后的图片会被强制缩放到A4尺寸，两张尺寸差异较大的图片合并到一张PDF文件里之后会导致有大面积留白

img_to_pdf.py  
	将文件夹及其子文件夹下的图片转换成以图片名命名的PDF文件
