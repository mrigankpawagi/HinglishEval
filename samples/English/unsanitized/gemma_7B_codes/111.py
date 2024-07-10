
def histogram(test):
    """
    Ek string di gayi hai jo space separated lowercase letters ko represent karti hai, return karo ek dictionary
    jisme sabse zyada repeat hone wale letter aur unke corresponding count ho.
    Agar kai letters ka occurrence same hai, to un sabhi ko return karo.
    
    Udaharan:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    count={}
    list1=test.split()
    max_num = 0
    for i in test:
        if i in count.keys():
            count[i]+=1
        else:
            count[i]=1
            

        
    for j in range (len(test)):
        if count.values():
            if ((max_num<count[j])):
                max_num=count[j]
        else:
            continue
    for i in count:
        if ((count[i]==max_num)):
            print(i,count[i],sep=' ')
        else:
            continue

    count=count.values()
  
    

print(histogram('b b b b a'))
