from fpdf import FPDF
# creat FPDF object
# Layout ('p' , 'L')
# Unit('mm','cm','in')
# format ('A3','A4'(default), 'A5' ,'Letter' ,'Legal' ,(100,150))
pdf =FPDF('P' , 'mm' , 'Letter')
# Add a page
pdf.add_page()
# specify font
# fonts('times' , courier' , helvetica' , 'symbol' , 'zpdfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular) , combination (i.e., ('BU'))
pdf.set_font('helvetica','' ,16)
# Add text
# w = width
# h= height
#
pdf.cell(40,10, 'Hello World!')
pdf.output('pdf_1.pdf')

