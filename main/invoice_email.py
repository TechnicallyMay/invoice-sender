import translate
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class InvoiceEmail():

    def __init__(self, customer, owner):
        self.owner = owner
        self.customer = customer
        body_file_name = "../data/message.txt"
        with open(body_file_name, 'r') as f:
            self.body = f.read()
        self.body = translate.translate(self.body, self.owner.data, self.customer.data)
        self.subject = self.find_tag("subject")
        self.remove_tagged("subject")
        self.announcement = not self.remove_tags("attach_invoice")


    def find_tag(self, tag):
        re_start = re.escape("<%s/>" % tag)
        re_end = re.escape("<\%s>" % tag)
        search = "%s(.*?)%s" % (re_start, re_end)
        result = re.search(search, self.body, re.S)
        return result.group(1)


    def remove_tagged(self, tag):
        to_remove = self.find_tag(tag)
        self.body = self.body.replace(to_remove, "")
        self.remove_tags(tag)


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


    def send(self):
        fromaddr = self.owner.data["Email"]
        toaddr = self.customer.data["Email"]
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = self.subject
        body = self.body
        msg.attach(MIMEText(body, 'plain'))
        if not self.announcement:
            attachment = open(self.customer.invoice.file_name, "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= Invoice.docx")
            msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        logged_in = False
        while not logged_in:
            try:
                s.login(fromaddr, self.owner.password)
                logged_in = True
            except:
                print("Incorrect password, or account security too high.")
                self.owner.get_pass()
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()
