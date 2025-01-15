def oldmult2(la_liste):
    # r=[]
    # for i in la_liste:
    #     r.append(i*2)
    
    r=[i*2 for i in la_liste]
    return r


def mult2(i):
    return i*2

def main():
    l = [10,20,30,40,50]
    # l2 = mult2(l) # [20,40,60,80,100]
    l2 = list(map(mult2,l)) 
    l2 = list(map(lambda i:i*2,l)) 
    print(l2)
if __name__=='__main__':
    main()
