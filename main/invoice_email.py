class InvoiceEmail():

    def __init__(self, owner):
        self.owner = owner
        self.body_file_name = "../data/message.txt"
        with open(self.body_file_name, 'r') as f:
            self.body = f.read()


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
