# Q-1: execute the following module

a = 0
def b():
    global a
    a = c(a)
    
def c(a):
    return a + 2

print(b())        # it adds +2 value in a----> a=0 so, a = 0+2=2
print(b())        # it again adds +2 in a so, ---->  a = 2+2 = 4   
print(b())        # it again adds +2 in a so, ---->  a = 4+2 = 6
print(a)          # now it print a value of a which is 6

#Q-2:Function fileLength(), given to you, takes the name of a file as input and returns 
    #the length of the file:

def file_length(midterm):
        file = open("midterm.py","r")
        contents = file.read()
        print("length of the midterm.py file is ",len(contents))
        file.close()

print(file_length("midterm.py"))
try:                              #this is to [print a massege for file not found]
    file = open("idterm.py")
except:
    print("given file does not exist")

#Q-3: 
class Marsupial():        #parent class ,Marsupial
    def __init__(self,x,y):
        self.pouch = []
    def put_in_pouch(self,objects):
        self.pouch.append(objects)
    def pouch_content(self):
        return self.pouch

m =Marsupial(0,0)
print(m)
m.put_in_pouch("doll")   
m.put_in_pouch("firetruk")
m.put_in_pouch("kitten")
print(m.pouch_content())

class Kangaroo(Marsupial):         #to create a child class Kangaroo
    def __init__(self,x,y) -> None:
        super().__init__(x,y)
        self.dx =0
        self.dy =0
    def jump(self,x,y):
        self.dx =self.dx +x
        self.dy = self.dy +y

    def __str__(self) -> str:
        return ("i am kangaroo located at coordinates ({},{})" .format(self.dx,self.dy))
k =Kangaroo(0,0)
print(k)
k.put_in_pouch("doll")   
k.put_in_pouch("firetruk")
k.put_in_pouch("kitten")
print(k.pouch_content())

k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)

#Q-4:
def collatz(number):
    print(number)
    if number ==1:
        return "done"
    if number %2==0:       # for an even integer
        return collatz(number//2)
    if number %2 !=0:                   # for an odd integer
        return collatz((3*number)+1)
    else:
        return
number=int(input("enter the number here: "))    #allow user input
print(collatz(number))

#Q-5:
def binary(n):
    if n>= 1:
        binary(n//2)
    print (n%2 ,end ="")
n=int(input("enter the positive integer here: \n")) 
binary(n)
print()

#Q-6:

from html.parser import HTMLParser
f1 = False
f2 = False
class HeadingParser(HTMLParser):
        #inheading =False
    def handel_starttag(self,tag):
        if tag =="h1":
            global f1
            f1 = "True"
        if tag =="h2":
            global f2
            f2 = "True"
    def handle_endtag(self,tag):
        if f1 == "False":
            pass
        if f2 == "False":
            pass
    def handle_data(self,content):
        global f1,f2
        if f1 == "True":
            print(content)
            f1 ="False"
        if f2 =="True":
            print("",end ="")
            print(content)
            f2 ="False"

file= open("w3c.html")
data = file.read()
file.close()
hp =HeadingParser()
hp.feed(data)

#Q-7:

from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

class Url(HTMLParser):
    def __init__(self, provide_URL):
        HTMLParser.__init__(self)
        self.providedURL =provide_URL
        self.availablelinks = []
    def catchlinks(self):
        return self.availablelinks
    def handle_starttag(self,tag,attrs):
        if tag =="a":
            for attr in attrs:
                if attr[0]=="href":
                    absolute=urljoin(self.providedURL,attr[1])
                if absolute[:4] =="http":
                    self.availablelinks.append(absolute)

all_links =[]
def webdir(provide_URL,depth,indent):
    global all_links
    o= urlopen(provide_URL)
    cont = o.read().decode()
    p =Url(provide_URL)
    p.feed(cont)
    all_links = p.catchlinks()
    print(indent* " " + provide_URL)
    if depth == 0:
        return
    for i in all_links:
        print(i, depth-1, indent+1)
webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test1.html',2,0)
        
#Q-8:
import sqlite3
connection = sqlite3.connect("trial.database")
connection.execute('''
CREATE TABLE IF NOT EXISTS seasonal_data(city text, 
                      country text, 
                      season integer, 
                      temperature integer,
                      rainfall integer);''')

connection.commit()
my_cur= connection.cursor()
connection.execute("mumbai","india","winter",24.8,5.9)
connection.execute("mumbai","india","spring",28.4,16.2)
connection.execute("mumbai","india","summer",27.9,1549.4)
connection.execute("mumbai","india","fall",27.6,346.0)
connection.execute("london","UK","winter",4.2,207.7)
connection.execute("london","UK","spring",8.3,169.6)
connection.execute("london","UK","summer",15.4,157.0)
connection.execute("london","UK","fall",10.7,5.9)
connection.execute("cairo","egypt","winter",13.6,16.5)
connection.execute("cairo","egypt","spring",20.7,6.5)
connection.execute("cairo","egypt","summer",27.7,0.1)
connection.execute("cairo","egypt","fall",22.2,4.5)


my_cur.execute("choose temprature from given data")
result =my_cur.fetchall()                   # for Q-a
for i in result:
    print(i, end ="")
print()

my_cur.execute("choose different cities from given data")
result =my_cur.fetchall()         #for Q-b
for i in result:
    print(i,end ="")
print()

my_cur.execute("choose from where country=india")
for i in result:               #for Q-c
    print(i,end ="")
print()

my_cur.execute("season=fall")
for i in result:             #for Q-d
    print(i,end ="")
print()

my_cur.execute("city,country,season where rainfall>200 and<400")
for i in result:               #forQ-e
    print(i,end ="")
print()

my_cur.execute("city,country where season-fall and temprature>20")
for i in result:                  #for Q-f
    print(i,end ="")
print()

my_cur.execute("sum(rainfall), where city+cairo")
for i in result:               #for Q-g
    print(i,end ="")
print()

my_cur.execute("sum(rainfall) for each season")
for i in result:                  #for Q-h
    print(i,end ="")
print()

connection.close()

#Q-9:
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over','the', 'lazy', 'dog']

for i in range(len(words)):          #to generate the list with uppercase laters
    words[i] = words[i].upper()
print(words)

for i in range(len(words)):          #to generate the list with lowercase laters
    words[i] = words[i].lower()
print(words)

l0 = len(words[0])              # to count word from the list words
l1 = len(words[1])
l2 = len(words[2])
l3 = len(words[3])
l4 = len(words[4])
l5 = len(words[5])
l6 = len(words[6])
l7 = len(words[7])
l8 = len(words[8])
print([l1,l2,l3,l4,l5,l6,l7,l8])

w0 = [words[0].upper(),words[0].lower(),len(words[0])]   # for upeercase,lowercase, lentgth
w1 = [words[1].upper(),words[1].lower(),len(words[1])]
w2 = [words[2].upper(),words[2].lower(),len(words[2])]
w3 = [words[3].upper(),words[3].lower(),len(words[3])]
w4 = [words[4].upper(),words[4].lower(),len(words[4])]
w5 = [words[5].upper(),words[5].lower(),len(words[5])]
w6 = [words[6].upper(),words[6].lower(),len(words[6])]
w7 = [words[7].upper(),words[7].lower(),len(words[7])]
w8 = [words[8].upper(),words[8].lower(),len(words[8])]
print(w0,w1,w2,w3,w4,w5,w6,w7,w8)

list=[]                 # for items with length >=4
for i in words:
    if len(i)>=4:
        list.append(i)
print(list)
