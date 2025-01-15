def main():
    l = [10,20,30,40,50]
    to_find = 300
    
    for i in l:
        print(i)
        if i == to_find:
            print("ok")
            break
    else:
        print("pas trouvé")

if __name__=='__main__':
    main()
