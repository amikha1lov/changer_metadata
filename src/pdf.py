from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

class PDF():

    def __init__(self, fp:str):
        self.__file_path = fp
        with open(fp, 'rb') as f:
            self.file = PdfFileReader(f)
            self.__info = self.file.getDocumentInfo()
        self.keys = ['/Author', '/Keyword', '/Title', '/Subject']



    def author(self):
        return str(self.__info[self.keys[0]])

    def keyword(self):
        return str(self.__info[self.keys[1]])

    def title(self):
        return str(self.__info[self.keys[2]])

    def subject(self):
        return str(self.__info[self.keys[3]])


    def update_metadata(self, metadata:dict):
        write_file = PdfFileWriter()
        with open(self.__file_path, 'r+b') as f:
            pdf = PdfFileReader(f)
            for i in range(0, pdf.getNumPages()):
                write_file.addPage(pdf.getPage(i))
            write_file.addMetadata(metadata)
            write_file.write(f)
            f.close()
