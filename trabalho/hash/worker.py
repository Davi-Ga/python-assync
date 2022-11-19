import hashlib


dict = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



#Ideia: criar um vetor de worker que receba - woker = []
# worker.push[<nome da função worker/theading>[lenght(dict)/MAXWORKERS]]


worker = []
worker.append(dict[15])
worker.append(dict[0])
worker.append(dict[20])
 

hash = 'ed968e840d10d2d313a870bc131a4e2c311d7ad09bdf32b3418147221f51a6e2' #aaaaa


def crack(i,j,k,l):
    global dict
    str = []
    str.append('a')

    str.append(dict[i])
    str.append(dict[j])
    str.append(dict[k])
    str.append(dict[l])

    hashB = hashlib.sha256(''.join(str).encode())
    resultB = hashB.hexdigest()


    if(hash == resultB):
       print("Achei")
       print(f"A palavra decodificada é: {''.join(str)}")

    else:
        l+=1
        print(l)
        if(l==25):
            l=0
            k+=1
        if(k==25):
            k=0
            j+=1
            print('k:',k)

        crack(i,j,k,l)


i = 0 #Worker 1 
j = 0 #Worker 2
k = 0 #Worker 3
l = 0 #Worker 4


str = []
str.append('a')
crack(i,j,k,l)
