from datetime import datetime


class InvoiceEmail():

    def __init__(self, owner, customer):
        self.owner = owner
        self.customer = customer
        self.body_file_name = "../data/message.txt"
        with open(self.body_file_name, 'r') as f:
            self.body = f.read()
        self.replace_key_words()


    def find_key_words(self):
        #This is used to find all tags in text, so user can
        #use variables in each message
        body = self.body.split()
        key_words = [word for word in body if '<' in word]
        for i, word in enumerate(key_words):
            for j, letter in enumerate(word):
                if letter == '<':
                    key_words[i] = word[j:]
                    word = word[j:]
                if letter == '>':
                    key_words[i] = word[:j + 1]
        return key_words


    def replace_key_words(self):
        c = self.customer.data
        o = self.owner.data
        translations = [("<customer.first_name>", c["First"]),
                        ("<customer.number_of_students>", c["Students"]),
                        ("<customer.monthly_rate>", c["Rate"]),
                        ("<customer.num_of_lessons>", c["Lessons"]),
                        ("<owner.full_name>", o["Name"]),
                        ("<owner.cell_number>", o["Cell"]),
                        ("<date>", datetime.now().strftime("%B %d, %Y")),
                        ("<month>", datetime.now().strftime("%B"))]
        for translation in translations:
            self.body = self.body.replace(translation[0], str(translation[1]))
