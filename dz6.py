import pickle
from datetime import datetime, timedelta

class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phone = phone
        self.birthday = birthday  

    

class Birthday:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth  

    

class AddressBook:
    def __init__(self):
        self.records = {}  
    def add_record(self, record):
        self.records[record.name] = record

    
    @staticmethod
    def load_from_file(filename="addressbook.pkl"):
        """Завантажує AddressBook із файлу."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("Файл не знайдено. Створено нову адресну книгу.")
            return AddressBook()  
    def save_to_file(self, filename="addressbook.pkl"):
        """Зберігає AddressBook у файл."""
        with open(filename, "wb") as f:
            pickle.dump(self, f)
            print("Дані успішно збережено у файл.")


def main():
   
    book = AddressBook.load_from_file()

    
    book.save_to_file()