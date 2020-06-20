
def partition(a,l,h):
    i=l-1;
    pi=a[h]
    for j in range(0,h):
        if(j<=a[h]):
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],pi=pi,a[i+1]
    return i+1

def quicksort(a,l,h):
    if l<h:
        pi=partition(a,l,h)
        quicksort(a,l,pi-1)
        quicksort(a,pi+1,h)
        
if __name__=="__main__":
    a=[1,5,2,9,7]
    quicksort(a,0,len(a)-1)
    print ("ans: ",a)