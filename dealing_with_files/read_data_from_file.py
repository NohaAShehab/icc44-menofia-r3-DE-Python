

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

try:
    fileobj = open('names.txt','r') # io.TextIOWrapper
except Exception as e:
    print(e)
else:
    print(fileobj)
    "# to read data"
    # data = fileobj.read() # read data into one string
    # print(data, type(data))
    "# read data line by line ?"
    # lines = fileobj.readlines() # list
    # print(lines)
    """ read file line by line ?"""
    mylines = []
    for line in fileobj:
        mylines.append(line)
    print(mylines)

    """ check this """
    print(fileobj.readlines())
    """ reset file pointer """
    fileobj.seek(10)
    print(fileobj.readlines())
    fileobj.close()