# Invoice Sender
Made to send invoices to students of a piano teacher.
## Setup
```
Input appropriate data into owner.xlsx and customers.xlsx

For the owner email, it is recommended to use a new gmail account, because the "Allow less secure apps" setting has to be turned on during use. Alternatively, turn the setting on ONLY during usage.

Edit message using tags found in tags section (They will be replaced with appropriate data)
Anything within the subject tags will be the subject of the email
```
## Tags
```
<customer.first_name>
<customer.full_name> 
<customer.number_of_students>
<customer.monthly_rate> - This is actually the per lesson cost
<customer.num_of_lessons> - How many lessons each student from customer took
<owner.full_name> - All of the owner tags give your information
<owner.cell_number>
<owner.address>
<owner.city_state_zip>
<date> - Current date
<month> - Current month
<next_month>
<due_date> - See owner excel sheet for these last 3
<header>
<title>
```
## Usage
```
Install dependencies
cd main
python main.py
Enter password for gmail account
Check info and enter 'y' to the console
Name the backup file (for record keeping)
```
