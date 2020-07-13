#поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
import re
from pprint import pprint
from itertools import groupby
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def make_correct_names(contacts_list):
    formated_name_list = []
    pattern = re.compile(r'^([аА-яЯ]+)[\s|,]([аА-яЯ]+)[\s|,]([аА-яЯ]+|)')
    replace_names = r'\1, \2, \3'
    for people in contacts_list:
        people = ",".join(people)
        result = [pattern.sub(replace_names, people)]
        formated_name_list.append(result)
    return formated_name_list

def make_correct_phone_numbers(contacts_list):
    formated_phone_list = []
    pattern = re.compile(
      r'(\+7|8)\s*\(?(\d{3})\)?(\s*|-)(\d{3})(\s*|-*)(\d{2})-?(\d{2})\s*(\(?(доб\.)\s*(\d+)\)?)?')
    replace_phone_numbers = r'+7(\2)\4-\6-\7 \9\10'
    for people in contacts_list:
      people = ",".join(people)
      result = pattern.sub(replace_phone_numbers, people)
      formated_phone_list.append(result)
    return formated_phone_list

formated_phone_book = make_correct_phone_numbers(make_correct_names(contacts_list))


def delete_duplicates(contacts_list):
  new_list_contact = []
  for contact in contacts_list:
    contact = ''.join(contact)
    contact = contact.split(',')
    new_list_contact.append(contact)

  for contact in new_list_contact:
    while contact[3] == '':
      del (contact[3])
# print(delete_duplicates(formated_phone_book))
  name_list = []
  set_list_contact = []
  for contact in new_list_contact:
    if contact[0] not in name_list:
      name_list.append(contact[0])
      set_list_contact.append(contact)
  return set_list_contact
# #
# #
contacts_list = delete_duplicates(formated_phone_book)
pprint(contacts_list)
# print(delete_duplicates(contacts_list))
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
