n,h = map(int,input().split())
boxes = [int(i) for i in input().split()]
ptr=0
pickedFrom = None
def moveLeft():
    global ptr
    if ptr>0:
        ptr -= 1

def moveRight():
    global ptr
    if ptr<n-1:
        ptr += 1

def pickBox():
    global pickedFrom
    if boxes[ptr]!=0 and pickedFrom is None:
        boxes[ptr] -= 1
        pickedFrom = ptr


def dropBox():
    global pickedFrom
    if boxes[ptr]<h and pickedFrom is not None:
        boxes[ptr] += 1
        pickedFrom = None

def executeTask(k):
    if k==1:
        moveLeft()
    elif k==2:
        moveRight()
    elif k==3:
        pickBox()
    elif k==4:
        dropBox()

commands = [int(i) for i in input().split()]
for command in commands:
    executeTask(command)
for box in boxes:
    print(box,end=' ')