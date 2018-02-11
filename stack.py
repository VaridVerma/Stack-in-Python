#push Operation
def isFull(stack , sp):
    if sp==len(stack)-1:
        return 1
    else:
        return 0
def push(stack ,sp):
    if isFull(stack,sp):
        print("stack is full ")
    else:
        data=input('Enter the value to be pushed : ')
        sp+=1
        stack[sp]=data
        traverse(stack,sp)
    return sp

#pop operation
def isEmpty(stack,sp):
    if sp==-1:
        return 1
    else:
        return 0

def pop(stack, sp):
   if isEmpty(stack,sp):
       print 'stack is empty '
   else:
       stack[sp]=0
       sp-=1
   return sp

#stack traversal
def traverse(stack, sp):
   while sp>=0:
       print stack[sp]
       sp-=1

#main function
def main():
    stack=[0,0,0,0,0]
    sp =-1
    while 1:
        print '1 for push'
        print '2 for pop'
        print '0 for exit'
        print '3 view Stack'
        ch = input('Enter your choice : ')
        if ch == 1:
            sp=push(stack,sp)
            traverse(stack,sp)
        elif ch==2:
            sp=pop(stack,sp)
            traverse(stack,sp)
        elif ch==0:
            print 'bye'
            break
        elif ch==3:
            print traverse(stack,sp)
        else:
            print 'Invalid Input'
            break

main()