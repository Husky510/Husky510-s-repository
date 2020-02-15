#Η συνάρτηση που μετατρέπει τα strings σε ASCII.
def stringToInt(inputString):
    asciiString=""
    for i in range(len(inputString)):
        asciiString += str(ord(inputString[i]))
    return int(asciiString)

#Η συνάρτηση που ελέγχει αν ο ASCII αριθμός είναι πρώτος ή όχι.
def checkIfPrime(num):
    if num > 1: 
        for i in range(2, num//2):
            if (num % i) == 0:
                print("Το", num, "δεν είναι πρώτος αριθμός.")
                break
        else:
            print("Το", num, "είναι πρώτος αριθμός.")
    else:
        print("Το", num, "δεν είναι πρώτος αριθμός.")

#Το κύριο πρόγραμμα, απο το οποίο καλούνται οι συναρτήσεις.
while 1:
    inputValue = input("Παρακαλώ γράψτε κάτι και πιέστε Enter.\n")
    inputValue=stringToInt(inputValue)
    checkIfPrime(inputValue)
    input("Πιέστε ένα πλήκτρο για να συνεχίσετε...")
