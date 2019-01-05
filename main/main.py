import customer
from invoice_email import InvoiceEmail
from owner import Owner


owner = Owner()
email = InvoiceEmail(owner)
print(email.find_key_words())
