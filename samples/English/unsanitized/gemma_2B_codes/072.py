
def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''
    return q.reverse()==q and sum(q)<=w
a=[]
i = 0
while(a[i]==5):
    i=1
while(i!=5):
    x=int(input("enter the number:"))
    a.append(x)
while(i!=5):
    if x>11:
        print("invalid input")
    else:
        y=int(input("enter the number of times"))
        if x>y:
            print("invalid input")
        q=int(input("enter sum"))
        w=int(input("enter weight"))
        ll=0
        for i in a:
            
            ll=ll+i
            if ll>q:
                print("invalid input")
                return False
       
        print(q," ",y)
        if (q-ll)>w:
            print("invalid input")
            return False
        if q==0:
            print("invalid input")
            return False
        if q-w in a or ll in a:
            print("invalid input")
            return False
        
        if will_it_fly(a,w):
            print("yes")
        else:
            print("yes")
            if q-ll<=w:
                print("yes")
            else:                
                print("no")
else:
    print("done")
