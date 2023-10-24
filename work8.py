class M:
    def __str__(self):
        return 'Member("{}", "{}", "{}")'.format(self.last_name, self.name, self.phone_number)

    def __init__(self, last_name=None, name=None, phone_number=None, from_line=None):
        if from_line is None:
            self.last_name = last_name
            self.name = name
            self.phone_number = phone_number
        else:
            self.last_name, self.name, self.phone_number = str(from_line).replace(" ", '').split("|")

    def input_characters(self):
        self.last_name = input("Введите фамилию: ").capitalize()
        self.name = input("Введите имя: ").capitalize()
        self.phone_number = input("Введите номер телефона: ").capitalize()

    def __str__(self):
        return '{0:10} | {1:10} | {2}'.format(self.last_name, self.name, self.phone_number) + '\n'


class Contacts:
    def find_member(self, query=None):
        with open('phone.txt') as file:
            for line in file:
                member = Member(from_line=line)
                print(member)
                if member.last_name == query:
                    return member

    def add_member(self):
        m = Member()
        m.input_characters()
        if c.find_member(query=(m.last_name, m.name)) is None:
            f = open('phone.txt', 'a')
            f.write('{0:10} | {1:10} | {2}'.format(m.last_name, m.name, m.phone_number) + '\n')
            print('\nКонтакт {lastName} {name} успешно добавлен\n'.format(lastName=m.last_name, name=m.name))
            f.close()
        else:
            print('Такой контакт уже есть')

    def delete_member(self, query):
        objects = []
        f = open('phone.txt', 'r+')
        for line in f.readlines():
            member = Member(from_line=line)
            objects.append(member)
        for object in objects:
            if (member.last_name, member.name) != query:
                f.write(object.__str__())


    def show_all_contacts(self):
        with open('phone.txt') as file:
            for line in file:
                member = Member(from_line=line)
                print(member)


def choice():
    selector = None
    try:
        selector = int(input('Введите "1" если хотите найти контакт\n' + \
                             'Введите "2" если хотите добавить новый контакт\n' + \
                             'Введите "3" если хотите удалить контакт\n' + \
                             'Введите "4" если хотите просмотреть всю адресную книгу\n' + \
                             'Ввести здесь ------->:'))
    except ValueError:
        print('\n\nНе корректный ввод!!!\n')
        print('Необходимо ввести целое число!!!\n\n')
    return selector


c = Contacts()
while True:
    selector = choice()
    if selector == 1:
        query = ((input('Для поиска контакта введите его фамилию: ').capitalize(),
                  input('Для поиска контакта введите его имя: ').capitalize()))
        print(c.find_member(query))
    elif selector == 2:
        c.add_member()
    elif selector == 3:
        query = ((input('Для удаления контакта введите его фамилию: ').capitalize(),
                  input('Для удаления контакта введите его имя: ').capitalize()))
        c.delete_member(query)
    elif selector == 4:
        c.show_all_contacts()