filename=input("Enter the file name to open: ")

try:
    with open("input.txt", "r") as file:
        content=file.read()

        words=content.split()
        word_count=len(words)


        upperCasing=content.upper()    

    with open("output.txt", "w") as file:
        file .write("Processed text: \n\n")
        file.write(upperCasing)
        file.write("\n\n Word count: " + str(word_count))

    print("output.txt created successfully!")  
      
except FileNotFoundError:
    print("The file does not exist") 
except PermissionError:
    print("You donot have permissions to read this file")    
except Exception as e:
    print("Unexpected error occured")    