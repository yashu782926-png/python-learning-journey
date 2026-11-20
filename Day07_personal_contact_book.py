contacts = {
    "Anu": "9876543210",
    "Ravi": "9876543211",
    "Ananya": "9876543210",
    "Rahul": "8765432109",
    "Priya": "9988776655",
    "Kiran": "9090909090",
    "Arjun": "7894561230"
}
running=True
while running :
    print(" CONTACT BOOK ")
    print ("1.Add contact ")
    print("2.View Contacts ")
    print("3. Search contact ")
    print("4. Update contact ")
    print("5.Delete contact  ")
    print("6.Exit")

    choice=input("Enter your choice: ")
    if choice=="1":
     add_contact = input("Do you want to add a new contact? (yes/no): ")
     if add_contact.lower() == 'yes':
       new_name = input("Enter the name of the new contact: ")
       if new_name.strip()=="":
        print("Name cannot be empty! Enter a propper name:")
       elif new_name in contacts:
        print(f"contact {new_name} is already in contats!")
       else: 
        new_phone = input("Enter the phone number of the new contact: ")
      
        if len(new_phone)==10 and new_phone.isdigit():
         contacts[new_name] = new_phone 
         print(f"Contact {new_name} added successfully.")
        
        else:
         print("Invalid phone number! Enter exactly 10 digits.")
     elif add_contact.lower()== "no":
           print("OK")
    
     else:
      print("Please enter yes or no.") 
    elif choice=="2":
     view_contacts = contacts.items()
     for name, phone in view_contacts:
      print(f"Name: {name}, Phone: {phone}")

    elif choice=="3":
         search_contact = input("Do you want to search for a contact? (yes/no): ")
         if search_contact.lower() == 'yes':
            search_name = input("Enter the name of the contact to search: ")
            if search_name.strip()=="":
              print("Name cannot be empty! Enter a propper name: ") 
            elif search_name in contacts:
               print(f"Contact found: Name: {search_name}, Phone: {contacts[search_name]}")
            else:
               print("Contact not found.")
         elif search_contact.lower()== "no":
                print("OK")
         else:
             print("Please enter yes or no.") 
    elif choice=="4":
        update_contact = input("Do you want to update a contact? (yes/no): ")
        if update_contact.lower() == 'yes': 
           update_name = input("Enter the name of the contact to update: ")
      
           if update_name.strip()=="": 
              print("Name cannot be empty!")
     
           elif update_name in contacts:
                new_phone = input("Enter the new phone number: ")
       
                if len(new_phone)==10 and new_phone.isdigit(): 
                   contacts[update_name] = new_phone 
                   print(f"Contact {update_name} updated successfully.")
                else:
                   print("Invalid phone number! Enter exactly 10 digits.")
     
           else:
               print("Contact not found.")
           for name, phone in contacts.items():
               print(f"Name: {name}, Phone: {phone}")
        elif update_contact.lower()== "no":
               print("OK")
        else:
            print("Please enter yes or no.") 
    
    elif choice=="5":  
     
     delete_contact = input("Do you want to delete a contact? (yes/no): ")
     
     if delete_contact.lower() == 'yes':
      
        delete_name = input("Enter the name of the contact to delete: ")
      
        if delete_name.strip()=="": 
         print("Name cannot be empty!")
        elif delete_name in contacts:
          del contacts[delete_name]
          print(f"Contact {delete_name} deleted successfully.")
        else:
         print("Contact not found.")
     elif delete_contact.lower()== "no":
       print("OK")

     else:
      print("Please enter yes or no.")
   
   
    elif choice=="6":
      print("Thank you!")
      break

    else:
      print("Invalid choice!Please enter 1-6.")
    
 
 