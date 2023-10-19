from PyPDF2 import PdfWriter, PdfReader

########## Split all pages in pdf #################
# inputpdf = PdfReader(open("result.pdf", "rb"))
# for i in range(len(inputpdf.pages)):
#     output = PdfWriter()
#     output.add_page(inputpdf.pages[i])
#     with open("document-page%s.pdf" % i, "wb") as outputStream:
#         output.write(outputStream)

###################### Split required pages #####################


# pages = [0,1,3]
# inputpdf = PdfReader(open("result.pdf", "rb"))
# output = PdfWriter()
# for page_num in pages:
#     output.add_page(inputpdf.pages[page_num])
# with open("required_pages.pdf", "wb") as outputStream:
#         output.write(outputStream)