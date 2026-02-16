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
