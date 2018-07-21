# * args - arguments - typeof is tuple
# ** kwargs - keyword arguments - typeof is dictionary

# def emp(id,name,age,*address):
#     print("Id : {}".format(id))
#     print("Name : {}".format(name))
#     print("Age : {}".format(age))
#     print("Address : {}".format(address))
#
# emp(101,'Ram',30,'Delhi','Noida')
# emp(102,'Shyam',32,'Delhi','Noida','Pune')

def emp(**details):
    # print(details)
    for i in details.items():
        print(i)

emp(name='Ram',age=30,company='HCL')
emp(name='Shyam',company='TCS',salary=25000)
emp(name='Mohan',company='TCS', address = 'Delhi')