import sys
sys.path.append('..')

from sample.html_to_pdf_converter import get_pdf_from_html

if len(sys.argv) != 3:
  print ("usage: converter.py <html_page_sourse> <filename_to_save>")
  exit()

result = get_pdf_from_html(sys.argv[1], chromedriver='../chromedriver')
with open(sys.argv[2], 'wb') as file:
  file.write(result)
