def main():
    
    def lgn_search():
        a=[ i*10 for i in range(1,11)]
        n=len(a)
        b=len(a)//2   
        k=0
        key=90
        while(b>=1):
            while(k+b<n and  a[k+b]<=key):
                k+=b
            b//=2      
        if(a[k]==key):
            print('found at:{index}'.format(index=k))
        else:
            print('notfound')
    lgn_search()
if __name__ =="__main__":
    main()
  
