contacts = [
    {
        'first_name': 'John',
        'last_name': 'Doe',
        'phone': '123-456-7890',
        'email': 'john.doe@email.com',
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'state': 'CA',
            'zip_code': '12345'
        }
    },
    {
        'first_name': 'Joe',
        'last_name': 'Doe',
        'phone': '234-567-8901',
        'email': 'joe.doe@email.com',
        'address': {
            'street': '123 Elm St',
            'city': 'Anycity',
            'state': 'NY',
            'zip_code': '23456'
        }
    },
    {
        'first_name': 'Jay',
        'last_name': 'Joe',
        'phone': '345-678-9012',
        'email': 'jay.joe@email.com',
        'address': {
            'street': '123 Oak St',
            'city': 'Anyville',
            'state': 'TX',
            'zip_code': '34567'
        }
    }
]


print("Complete Contact Information:")
#print(('First', 'Last', 'Phone', 'Email', 'Address', 'City/State'))
for contact in contacts:
    full_name = contact['first_name'] + ' ' + contact['last_name']
    address_str = contact['address']['street'] + ', ' + contact['address']['city'] + ', ' + contact['address']['state'] + ' ' + contact['address']['zip_code']
    print((contact['first_name'], contact['last_name'], contact['phone'], contact['email'], address_str, contact['address']['city'] + ', ' + contact['address']['state']))

print("\nPhone Numbers:")
#print(('Name', 'Phone'))
for contact in contacts:
    full_name = contact['first_name'] + ' ' + contact['last_name']
    print("{:<10} {:<15}".format(full_name, contact['phone']))


name = input("\nEnter a name to lookup phone number: ")
for contact in contacts:
    full_name = contact['first_name'] + ' ' + contact['last_name']
    if name == full_name:
        print("Phone number for {} is {}".format(full_name, contact['phone']))


first_name = input("\nEnter a first name to lookup address: ")
for contact in contacts:
    if first_name == contact['first_name']:
        address_str = contact['address']['street'] + ', ' + contact['address']['city'] + ', ' + contact['address']['state'] + ' ' + contact['address']['zip_code']
        print("Address for {} is {}".format(first_name, address_str))

print("\nCities and States:")
for contact in contacts:
    print("{}, {}".format(contact['address']['city'], contact ['address']['state']))
