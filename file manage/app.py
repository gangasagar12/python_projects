import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"filename {filename} : created sucessfully!")
    except FileExistsError :
        print(f"filename {filename} already exits")
    except exception as e:
        print("an error occured!")


def view_all_files():
    files=os.listdir()
    if not files:
        print("no files found")
    else:
        print("file in directory")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted: ")
    except FileNotFoundError:
        print('file not found')
    except exception as e:
        print('an erroor occured: ')

def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content=f.read()
            print(f"content of {filename}: \n{content}")
    
    except FileNotFoundError:
        print("filename doestnot exits")

    except exception as e:
        print('an error occured')

def edit_file(filename):
    try:
        with open('sample.txt' ,'a') as f:
            content=input("enter data to add=")
            f.write(content+ "\n")
            print("content addded to {filename} sucessfully !")
    except FileNotFoundError:
        print(f"{filename} does not exits")

    except exception as e:
        print("an error occured")

def main():
    while True:
        print('file  management app')
        print("1: create a file")
        print("2: view all files")
        print("3. delete files")
        print("4. read file")
        print("5: edit files")
        print("6: exit")

        choice=input("enter your choice(1-6):")
        if choice=="1":
            filename=input("enter the filename to creeate=")
            create_file(filename)

        elif choice=="2":
            view_all_files()

        elif choice=="3":
            filename=input("enter the name of file you want to delete=")
            deletefile(filename)
        
        elif choice=="4":
            filename=input("enter file name to read=")
            read_file(filename)
        elif choice=="5":
            filename=input("enter file name to edit=")
            edit_file(filename)
        elif choice=="6":
            print("closing the app...")
            break

        else:
            print("invalid syntax")


if __name__=="__main__":
    main()



