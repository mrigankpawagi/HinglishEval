
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    
    def swap(n,m):
        temp=n[m]
        n[m]=n[m-1]
        n[m-1]=temp
    
    n=copy.deepcopy(lst)
    n.sort()
    def find_strange_sort(lst):
        pivot=lst[int(len(lst)/2)]
        arr=[[pivot]]
        
        for n in lst:
            if n < pivot:
                arr.append([n])
            else:
                arr.append([pivot])
        
        arr.sort()
        
        for i in range(1,len(arr)):
            x=arr[i-1]
            y=arr[int(i)]
        
            if x == y:
                return [x]
            else:
                if x[0] < y[0]:
                    x=[y[0],x[0]]
                    y=x
                arr.remove(x)
                temp=arr.count(y)
                arr.count(y)-=temp
                
        return arr
        
    def strange_sort(lst):
        
        if lst == []:
            return lst
        q=[]
        s=swap(lst,0,len(lst)-1)
        for i in s:
            
            pivot=(s[0]+s[-1])//2
            l=len(lst)
            if pivot < l:
                if lst[pivot:pivot+l] < lst:
                    c=pivot
                    
