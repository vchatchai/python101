infile = open('exercise101.py','r')
lines = infile.readlines() 
for line in range(len(lines)-1,0,-1) :
    print(lines[line])