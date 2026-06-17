import os
class journalmanager:
    def __init__(self,filename="journal.txt"):
        self.filename=filename
    def create_file(self):
        try:
            with open(self.filename,"x") as file:
                print("journal file created successfully")
        except FileExistsError:
            pass
    def add_entry(self):
        try:
            entry = input("Enter your journal entry: ")
            with open(self.filename, "a") as file:
             file.write(entry + "\n")
            print("Journal entry entered successfully")
        except PermissionError:
            print("premission is not granted")
    def view_entry(self):
        try:
            with open(self.filename,"r") as file:
                content=file.read()
                if content:
                    print(content)
                else:
                    print("journal is empty")
        except FileNotFoundError:
            print("journal file not founded")
    def search_entry(self):
        keyword=input("entre keyword")
        try:
            found=False
            with open(self.filename,"r") as file:
                lines=file.readlines()
            print("\nsearch result:")
            for line in lines:
                if keyword.lower()in line.lower():
                    print(line.strip())
                    found=True
            if not found:
                    print("no journal entry is founded")
        except Exception as e:
            print(e)
    def delete_entries(self):
        try:
            confrim=input("you are sure to delete the entries")
            if confrim.lower()=="yes":
                os.remove(self.filename)
                print("entries are deleted")
            else:
                print("entries can't be deleted")
        except PermissionError:
            print("premission can't given")
def main():
    journal=journalmanager()
    journal.create_file()
    while True:
        print("press 1 for add new entry")
        print("press 2 for view all entries")
        print("press 3 for search for an entry")
        print("press 4 for delete all entry")
        print("press 5 to exit the programm")
        try:
            choice=int(input("entre your choice;"))
            if choice==1:
                journal.add_entry()
            elif choice==2:
                journal.view_entry()
            elif choice==3:
                journal.search_entry()
            elif choice==4:
                journal.delete_entries()
            elif choice==5:
                print("thank you for using personal journal entry")
                break
            else:
                print("invailed choice")
        except ValueError:
            print("please entre vailed number")
main()
    
                
