#Η συνάρτηση η οποία ανοιγει το αρχείο .txt
def splitText():
    file = open("5.txt","r")
    file = file.read()
    file = file.split()
    return file

#Η συνάρτηση η οποία σπάει το κείμενο σε λεξεις και αν οι λέξεις έχουν μήκος πάνω από
#3 γράμματα, αφαιρεί το πρώτο γράμμα και προσθέτει το γράμμα στο τέλος μαζί με το ay.
def processWords(wordsArray):
    for i in range(len(wordsArray)):
        if len(wordsArray[i]) > 3:
            wordsArray[i] = wordsArray[i][1:] + wordsArray[i][0] + "ay"
    return wordsArray

#Το κύριο πρόγραμμα που καλεί τις συναρτήσεις.
fileText = splitText()
processedWords = processWords(fileText)

#Η εκτύπωση του κειμένου
for i in range(len(processedWords)):
    print(processedWords[i])
        
input("Πιέστε ένα πλήκτρο για να συνεχίσετε...")
