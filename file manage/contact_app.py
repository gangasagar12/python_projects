contact={}
 
while True:
    print("\n contact book  app")
    print("1.create contact")
    print("2.view contacts")
    print("3.delete contact")
    print("4.update contact")
    print("5.search contact")
    print("6.count contacts")
    print("7.exit app")

    choice=input("enter your choice=")

    if choice==1:
        name=input("enter contact name=")
        if name in contacts:
            print(f"contact name {name} already exits")
        else:
            age=input("enter age=")
            phone=input("enter phone number=")
            mobile=input("enter mobile number=")
            email=input("enter email address=")
            contacts[name]={"age":age,"phone":phone,"mobile":mobile,"email":email}
            print(f"contact {name} created successfully")

    elif choice==2:
        name=input("enter contact name to view=")
        if name in contacts:
            contact=contacts[name]
            print(f"Name: {name},Age: {contact['age']}, Mobile: {contact['mobile']}, Email: {contact['email']}")
        else:
            print(f"contact not found with the name { name}")