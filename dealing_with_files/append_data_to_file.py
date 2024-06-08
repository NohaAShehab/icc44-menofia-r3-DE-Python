
"""

    python provide function to open file ?
    --> define open file // read /// write /// append
    ---> file mode ? r --> read , w--> write , a-->append

    2- do operation ?
        read
        write

    3- close file
"""

# fileobj = open('names.txt', 'r')
# print(fileobj)


# any dealing with file --> wrap content between try and except
""" when you try to open file with a mode 
if file doesn't exist ? python will try to create it ?

if file exists ? --> python will open file for writing 
started from the end for the file ?
keep old content """
try:
    fileobj = open('mycv.txt' ,'a') # io.TextIOWrapper
except Exception as e:
    print(e)
else:
    print(fileobj)
    fileobj.write("My name is Noha\n")
    fileobj.write("I works at ITI \n")
    fileobj.write("I lives in Cairo")
    fileobj.writelines(['noha\n', 'iti\n', 'cairo\n'])
    fileobj.write("-------------------------\n\n")
    fileobj.close()