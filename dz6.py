import pickle

class AddressBook:
    
    @staticmethod
    def load_from_file(filename="addressbook.pkl"):
        
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("Файл не знайдено. Створено нову адресну книгу.")
            return AddressBook()  

    def save_to_file(self, filename="addressbook.pkl"):
        
        with open(filename, "wb") as f:
            pickle.dump(self, f)
            print("Дані успішно збережено у файл.")