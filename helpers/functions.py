def loadFormFile(fileName):
    try:
        with open(fileName,"r") as file:
            print(file.read())
        """Then parse file to get something nice"""
    except FileNotFoundError:
        print("hi")
        exit()



