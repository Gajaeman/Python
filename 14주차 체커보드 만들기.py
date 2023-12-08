table=[]

def printList(mylist):
    for row in range(len(mylist)):
        for col in range(len(mylist[0])):
            print(mylist[row][col],end='')
        print()

def init(mylist):
    for row in range(len(mylist)):
        for col in range(len(mylist[0])):
            if(row+col)%2==0:
                table[row][col]=1

for row in range(10):
    table+=[[0]*10]

init(table)
printList(table)
