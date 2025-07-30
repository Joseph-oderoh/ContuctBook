contacts = []
name_set = set()
def add_contact():
    name = input("Enter a name: ").strip
    if name in name_set:
        print("Name already Exists! ")
        return
    phone = input("Enter Phone number: ").strip()
    contact = {
        "name": name,
        "phone": phone  
    }
    contacts.append(contact)
    name_set.add(name)
    print(f"{name} added successfull!")


def veiw_contact():
    if not contacts:
        print("No contacs found!")
        return
    print("\n--  All Contacts --")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
