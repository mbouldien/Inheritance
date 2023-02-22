class Person:

    def __init__(self, name, address, phone_no):
        self.__name = name
        self.__address = address
        self.__phone_no = phone_no
    
    def get_name():
        return self.__name()
    
    def get_addres():
        return self.__address()

    def get_phone_no():
        return self.__phone_no()
    
    def print_person(self):

        print('Name: ', self.__name)
        print('Address: ', self.__address)
        print('Phone Number: ', self.__phone_no)


class Customer(Person):

    def __init__(self, name, address, phone_no, cust_no, mail_list):
        
        Person.__init__(self, name, address, phone_no)
        self.__cust_no = cust_no
        self.__mail_list = mail_list
    
    def print_person(self):
        Person.print_person(self)
        print('Customer Number: ', self.__cust_no)
        if self.__mail_list:
            print('On Mailing List: Yes')
        else:
            print('On Mailing List: No')