import translate
import re


class InvoiceEmail():

    def __init__(self, owner, customer):
        self.owner = owner
        self.customer = customer
        body_file_name = "../data/message.txt"
        with open(body_file_name, 'r') as f:
            self.body = f.read()
        self.body = translate.translate(self.body, self.customer.data, self.owner.data)
        self.subject = self.find_tag("subject")
        self.remove_tagged("subject")
        self.remove_tags("subject")
        if self.remove_tags("attach_invoice"):
            self.announcement = False
        else:
            self.announcement = True


    def find_tag(self, tag):
        re_start = re.escape("<%s/>" % tag)
        re_end = re.escape("<\%s>" % tag)
        search = "%s(.*?)%s" % (re_start, re_end)
        result = re.search(search, self.body, re.S)
        return result.group(1)


    def remove_tagged(self, tag):
        to_remove = self.find_tag(tag)
        self.body = self.body.replace(to_remove, "")


    def remove_tags(self, tag):
        start = "<%s/>" % tag
        if tag != "subject":
            start = "\n" + start
        end = "<\%s>\n" % tag
        new = self.body
        for t in (start, end):
            new = new.replace(t, "")
        if new != self.body:
            self.body = new
            return True
        else:
            return False
