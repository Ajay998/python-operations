import glob
from pypdf import PdfMerger
pdf_files = glob.glob('*.{}'.format('pdf'))

print(pdf_files)
print(len(pdf_files))

merger = PdfMerger()
for pdf in pdf_files:
    merger.append(pdf)
merger.write("result.pdf")
merger.close()