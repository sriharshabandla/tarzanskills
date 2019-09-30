 with open("filehandling.txt",'r') as f:
    print(f.read())

with open("filehandling1.txt",'r') as f:
    contents = f.readlines()
    for line in contents:
        print(line,end='*')


with open("filehandling1.txt",'r') as f:
    content=f.readline()
    print(content)


with open("filehandling1.txt",'r') as f:
    content=f.readline()
    print(content)
    content = f.readline()
    print(content)

with open("filehandling1.txt",'r') as f:
    for line in f:
        print(line,end='*')


with open ("filehandling1.txt",'r')as f:
    content=f.readlines(100)
    print(content)


with open ("filehandling1.txt",'r') as f:

    f.seek(20)
    print(f.readline(10))


with open ("filehandling1.txt",'r') as f:
    size=10
    content=f.read(size)
    while len(content)>0:
          print(content,end='**')
          content=f.read(size)

with open ("varun.txt",'w') as f:
    f.write("hello")


with open("varun.txt",'w') as f:
    f.write("test")
    f.seek(0)
    f.write("r")


with open("abc.jpg",'rb') as rf:
 with open("varun2.jpg",'wb') as wf:
     for lines in rf:
         wf.write(lines)


with open("abc.png",'rb') as rf:
    with open("varun2.png",'wb') as wf:
        chunk_size=4096
        rf_chunk=rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk=rf.read(chunk_size)
