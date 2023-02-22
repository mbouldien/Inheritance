import PersonClass as pc

name = 'Mallory Bouldien'
address = '1722 S 11th Street'
phone = '123-456-7890'
cust_number = 120
mail_list = False


person = pc.Person(name, address, phone)
customer = pc.Customer(name, address, phone, cust_number, mail_list)

person.print_person()
print()
print()
customer.print_person()
