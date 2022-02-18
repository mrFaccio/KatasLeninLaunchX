# def main():
#     open("/path/to/mars.jpg")
    
# if __name__ == '__main__':
#     main()

# try:
#     open("mars.jpg")
# except FileNotFoundError as err:
#     print("got a problem trying to read the file:", err)

try:
    open("config.txt")
except OSError as err:
    if err.errno == 2:
        print("Couldn't find the config.txt file!")
    elif err.errno == 13:
        print("Found config.txt but couln't read it")