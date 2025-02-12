import os
folders = input("Please provide list of the folders name with spaces between them: ").split()
for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please enter the correct folder name "+folder+" doesn't exists")
        continue
    print("The list of files present in the "+folder)
    for file in files:
        print(file)
    