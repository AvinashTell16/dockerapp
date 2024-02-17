import os
import socket
from collections import Counter

Counter = Counter()

def getMyIPAdress():
    hostname = socket.gethostname()
    IPAddress = socket.gethostbyname(hostname)
    return IPAddress

def getNumberOfWords(file):
    total_word_count = 0
    with open(file, 'r') as file:
        for line in file:
            if (line != '\n'):
                if (file.name.endswith("IF.txt")):
                    Counter.update(line.replace("Â", "").split())
                total_word_count = total_word_count + len(line.replace("Â", "").split())
    return total_word_count

Tf_Word_Counts = {}
path ="/home/data"
if os.path.exists(path + "/" +"result.txt"):
  os.remove(path + "/" +"result.txt")
out=" The path of the text files is \n /home/data \n"
for eachFile in os.listdir(path):
    if eachFile.endswith(".txt"):
        out=out+eachFile+"\n"
        Tf_Word_Counts[eachFile] = getNumberOfWords(path + "/" + eachFile)
        
out=out+"\n"
out=out+"b.Total number of words in both files\n\n"
AllFiles_WC = 0
AllFilesNames = ""
for eachkey in Tf_Word_Counts.keys():
    AllFilesNames = AllFilesNames + eachkey + ","
    AllFiles_WC = AllFiles_WC + Tf_Word_Counts.get(eachkey)
    out = out +"Total number of words in " + eachkey + " is : " + str(Tf_Word_Counts.get(eachkey))+"\n"

out = out +"\n"
out = out +"c.Total number of words in both files (Grand Total):"
out = out + AllFilesNames[0:len(AllFilesNames) - 1] + " is: " + str(AllFiles_WC)+"\n"
out = out +"\n"
out = out +"d. Top three words with maximum number of count in IF.txt are: \n"
out = out +str(Counter.most_common(3))+"\n"
out = out +"\n"
out = out +"e.IP Address of the machine:" + getMyIPAdress()

results_File = open("/home/output/" +"result.txt","w")
results_File.write(out)
results_File.close()
for line in open("/home/output/" +"result.txt","r").readlines():
    print(line.replace("\n",""))