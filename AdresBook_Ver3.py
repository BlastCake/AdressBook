class Member:
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
		return '{0:10} | {1:10} | {2}'.format(self.last_name, self.name, self.phone_number)


class Contacts:
	def find_member(self, query):
		with open('data.txt') as file:
			for line in file:
				member = Member(from_line=line)
				if (member.last_name, member.name) == query:
					return member

	def add_member(self):
		member = Member()
		member.input_characters()
		if contacts.find_member(query=(member.last_name, member.name)) is None:
			f = open('data.txt', 'a')
			f.write('{0:10} | {1:10} | {2}'.format(member.last_name, member.name, member.phone_number) + '\n')
			print('\nКонтакт {lastName} {name} успешно добавлен\n'.format(lastName=member.last_name, name=member.name))
			f.close()
		else:
			print('Такой контакт уже есть')

	def delete_member(self, query):
		objects = []
		contacts = Contacts()
		with open('data.txt') as file:
			for line in file:
				try:
					member = Member(from_line=line)
					if contacts.validation(query, member):
						objects.append(member)
				except:
					continue
		with open('data.txt', 'w') as file:
			for object in objects:
				file.write(object.__str__())
		print('\nТелефонная книга успешно обновлена\n')

	def show_all_contacts(self):
		with open('data.txt') as file:
			for line in file:
				member = Member(from_line=line)
				print(member)

	def validation(self, query, member):
		if (member.last_name, member.name) != query:
			return True


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


contacts = Contacts()
while True:
	selector = choice()
	if selector == 1:
		query = ((input('Для поиска контакта введите его фамилию: ').capitalize(),
				  input('Для поиска контакта введите его имя: ').capitalize()))
		print(contacts.find_member(query))
	elif selector == 2:
		contacts.add_member()
	elif selector == 3:
		query = ((input('Для удаления контакта введите его фамилию: ').capitalize(),
				  input('Для удаления контакта введите его имя: ').capitalize()))
		contacts.delete_member(query)
	elif selector == 4:
		contacts.show_all_contacts()
