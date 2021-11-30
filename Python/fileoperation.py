with open("customer.txt", 'r+') as file:
#file = open("customer.txt", "r+")
    content = file.readline()
    writecontent = file.write("0.David,David@jj.com")
    print(f"Content of the file \n{content}", end='')
#file.close()