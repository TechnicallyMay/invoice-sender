from docx import Document
import translate


class Invoice():

    def __init__(self, customer, owner):
        self.customer = customer
        self.owner = owner
        self.template = Document("../data/invoice_template.docx")
        self.total = 0
        self.add_charges(self.customer.charges)
        self.replace_key_words()
        self.template.save("../data/temp.docx")


    def replace_key_words(self):
        for paragraph in self.template.paragraphs:
            paragraph.text = self.translate(paragraph.text)
        for table in self.template.tables:
            for i in range(len(table.rows)):
                for cell in table.row_cells(i):
                    for paragraph in cell.paragraphs:
                        paragraph.text = self.translate(paragraph.text)


    def translate(self, text):
        text = translate.translate(text, self.customer.data, self.owner.data)
        return text


    def add_charges(self, charges):
        charge_table = self.template.tables[1]
        for i in range(1, len(charge_table.rows) - 1):
            try:
                charge = charges.pop(i)
                charge_total = int(charge[0]) * int(charge[2])
                self.total += charge_total
                charge.append(charge_total)
            except IndexError:
                charge = ("", "", "", "")
            cells = charge_table.row_cells(i)
            qty = str(charge[0])
            description = str(charge[1])
            unit_price = str(charge[2])
            total_charge = str(charge[3])
            if unit_price != "":
                unit_price = "$" + unit_price
                total_charge = "$" + total_charge
            cells[0].paragraphs[0].text = qty
            cells[1].paragraphs[0].text = description
            cells[2].paragraphs[0].text = unit_price
            cells[3].paragraphs[0].text = total_charge
        final_row = charge_table.row_cells(len(charge_table.rows) - 1)
        final_row[3].paragraphs[0].text = "$" + str(self.total)
