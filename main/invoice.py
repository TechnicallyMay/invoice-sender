from docx import Document
import translate


class Invoice():

    def __init__(self, customer, owner):
        self.customer = customer
        self.owner = owner
        self.template = Document("../data/invoice_template.docx")
        self.translations = []


    def test(self):
        for paragraph in self.template.paragraphs:
            paragraph.text = self.translate(paragraph.text)


        for shape in self.template.inline_shapes:
            print("SHAPE")

        for table in self.template.tables:
            for i in range(len(table.rows)):
                for cell in table.row_cells(i):
                    for paragraph in cell.paragraphs:
                        paragraph.text = self.translate(paragraph.text)

        self.template.save("../data/test.docx")


    def translate(self, text):
        text = translate.translate(text, self.customer.data, self.owner.data)
        return text
