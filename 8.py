#Εδώ φέρνουμε τυχαίο αριθμό αυτοκινήτων στα 3 φανάρια
from random import randrange

#Εδώ είναι η συνάρτηση που καθορίζει ποιο φανάρι θα ανάψει πράσινο
#σύμφωνα με το που βρίσκονται τα περισσότερα αυτοκίνητα.
#False είναι το κόκκινο και true το πράσινο.
def defineGreen(k1,k2,k3):
    k1Green=False
    k2Green=False
    k3Green=False
    if k1>k2 and k1>k3:
        k1Green=True
    elif k2>k1 and k2>k3:
        k2Green=True
    elif k3>k1 and k3>k2:
        k3Green=True
    elif k1==k2 and k1==k3 and k2==k3:
        randNum=randrange(3)
        if randNum==0:
            k1Green=True
        elif randNum==1:
            k2Green=True
        else:
            k3Green=True
#Εδώ αν 2 φανάρια έχουν ίδιο αριθμό αυτοκινήτων, διαλέγει ένα στην τύχη.
    else:
        randNum=randrange(2)
        if k1==k2:
            if randNum==0:
                k1Green=True
            else:
                k2Green=True
        elif k1==k3:
            if randNum==0:
                k1Green=True
            else:
                k3Green=True
        else:
            if randNum==0:
                k2Green=True
            else:
                k3Green=True
    return k1Green,k2Green,k3Green

#Εδώ καθορίζεται ο αρχικός αριθμός αυτοκινήτων στα φανάρια.
#Έχω βάλει έναν τυχαίο αριθμό απο το 0 έως το 100.
k1=randrange(100)
k2=randrange(100)
k3=randrange(100)

#Αυτό ειναι το κύριο πρόγραμμα που εμφανίζει πόσα αυτοκίνητα
#ειναι σε κάθε φανάρι και το πόσα έρχονται-φεύγουν.
while 1:
    k1Green,k2Green,k3Green = defineGreen(k1,k2,k3)
    k1b=k1
    k2b=k2
    k3b=k3
    print("Η οδός Πανόρμου έχει",k1,"αυτοκίνητα.")
    print("Η οδός Ερυθρού Σταυρού έχει",k2,"αυτοκίνητα.")
    print("Η λεωφόρος Κηφισίας έχει",k3,"αυτοκίνητα.")        
    if k1Green:
        randNum=randrange(5,11)
        if k1-randNum>=0:
            k1=k1-randNum
            k2=k2+randrange(6)
            k3=k3+randrange(6)
        else:
            k1=0
            k2=k2+randrange(6)
            k3=k3+randrange(6)
    elif k2Green:
        randNum=randrange(5,11)
        if k2-randNum>=0:
            k2=k2-randNum
            k1=k1+randrange(6)
            k3=k3+randrange(6)
        else:
            k2=0
            k1=k1+randrange(6)
            k3=k3+randrange(6)
    else:
        randNum=randrange(5,11)
        if k3-randNum>=0:
            k3=k3-randNum
            k2=k2+randrange(6)
            k1=k1+randrange(6)
        else:
            k3=0
            k2=k2+randrange(6)
            k1=k1+randrange(6)

    
    k1b=k1b-k1
    k2b=k2b-k2
    k3b=k3b-k3

    if k1b>0:
        print(k1b,"αυτοκίνητα έφυγαν από την οδό Πανόρμου.")
    else:
        print(abs(k1b),"αυτοκίνητα ήρθαν στην οδό Πανόρμου.")
    if k2b>0:
        print(k2b,"αυτοκίνητα έφυγαν από την οδό Ερυθρού Σταυρού.")
    else:
        print(abs(k2b),"αυτοκίνητα ήρθαν στην οδό Ερυθρού Σταυρού.")
    if k3b>0:
       print(k3b,"αυτοκίνητα έφυγαν από τη λεωφόρο Κηφισίας.")
    else:
        print(abs(k3b),"αυτοκίνητα ήρθαν στη λεωφόρο Κηφισίας.")
    input("Πιέστε ένα πλήκτρο για να συνεχίσετε...\n")
