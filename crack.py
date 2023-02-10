
characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z", "^", "_", "`", "!", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]

cracked = "1"

sep = ""

def crack():

    global cracked
    try:
        for i in range(0,77):
            current = characters[i]
            temp = list(cracked)
            index = len(temp) -1
            if temp[index] == "~":
                    print("works")
            else:
                temp[index] = current
                cracked = sep.join(temp)
                print(cracked)
    except:
        cracked = cracked + "1"
        print(cracked)
crack()
