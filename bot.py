def parse_unput(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, *args
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Contact updated.'
    else:
        return 'Contact not found.'
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return 'Contact not found.'
def show_all(contacts):
    if contacts:
        return 'No contacts saved.'
    result = []
    for name, phone in contacts.items():
        result.append(f'{name}: {phone}')
    return '\n'.join(result)
def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter command: ')
        try:
            command, *args = parse_unput(user_input)
            if command in ['close', 'exit']:
                print('Goodbye!')
                break
            elif command == 'hello':
                print('How can i help you?')
            elif command == 'add':
                if len(args) != 2:
                    print('Invalid command.')
                else:
                    print(change_contact(args, contacts))
            elif command == 'change':
                if len(args) != 1:
                    print('Invalid command.')
                else:
                    print(show_phone(args, contacts))
            elif command == 'all':
                if args:
                    print('Invalid command.')
                else:
                    print(show_all(contacts))
            else:
                print('Invalid command.')

        except ValueError:
            print('Invalid command.')
if __name__ == '__main__':
    main()