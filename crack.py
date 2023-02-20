import json
import time

# loads settings.json

cracked = ""
Password = ""

with open("settings.json", "r") as f:
    json_object = json.loads(f.read())
    lenght = json_object["lenght"]
    Password = json_object["password"]

for i in range(0,lenght):
    cracked = cracked + "1"

###################################

characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z", "^", "_", "`", "!", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]

sep = ""

print(type(Password), type(cracked))

def check(result):

    global Password

    if result == Password:
        return True



for tries in range(0,1000):

    st = time.time()

    Break_Flag = False

    for i in range(0,76):
        current = characters[i]
        temp = list(cracked)
        index = len(temp) -1
        temp[index] = current
        cracked = sep.join(temp)
        print(cracked)
        CheckResult = check(cracked)

        if CheckResult == True:
            Break_Flag = True
            break

    if Break_Flag == True:
        break

et = time.time()
print(f"cracked in {et-st} seconds")
