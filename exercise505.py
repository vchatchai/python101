import hashlib  


def md5value(file):
    print(file.name, end=" ")
    md5 = hashlib.md5()
    try: 
        while True :
            data = file.read(1000)
            if not data:
                break
            md5.update(data.encode('utf-8'))
        md5file1 = md5.hexdigest()
        print(md5file1)
        return md5file1
    finally: 
        file.close() 



file1 = open("exercise101.py","r")
file2 = open("exercise102.py","r")


md51 = md5value(file1)
md52 = md5value(file2)

if md51 == md52 : 
    print("File is equal")

else: 
    print("File not equal")