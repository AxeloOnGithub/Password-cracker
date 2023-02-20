import json
import time
def crack():
    characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z", "^", "_", "`", "!", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]

    with open("settings.json", "r") as f:
        json_object = json.loads(f.read())
        length = json_object["length"]
        Password = json_object["password"]
        visualfeedback = json_object["visual_feedback"]

    var_dict = {}

    for x in range(length):  
        var_dict[str(x)]="1"

    def getlength(var_dict):

        match length:
            case 4:
                cracked = str(var_dict["0"]) + str(var_dict["1"]) + str(var_dict["2"]) + str(var_dict["3"])
                return cracked
            case 5:
                cracked = str(var_dict["0"]) + str(var_dict["1"]) + str(var_dict["2"]) + str(var_dict["3"] + str(var_dict["4"]))
                return cracked
            case 6:
                cracked = str(var_dict["0"]) + str(var_dict["1"]) + str(var_dict["2"]) + str(var_dict["3"]) + str(var_dict["4"]) + str(var_dict["5"])
                return cracked
            case 7:
                cracked = str(var_dict["0"]) + str(var_dict["1"]) + str(var_dict["2"]) + str(var_dict["3"]) + str(var_dict["4"]) + str(var_dict["5"]) + str(var_dict["6"])
                return cracked
            case 8:
                cracked = str(var_dict["0"]) + str(var_dict["1"]) + str(var_dict["2"]) + str(var_dict["3"]) + str(var_dict["4"]) + str(var_dict["5"]) + str(var_dict["6"]) + str(var_dict["7"])
                return cracked

    q = 0
    y = 0
    z = 0
    c = 0
    v = 0
    b = 0
    n = 0

    st = time.time()

    while True == True:
        cracked = getlength(var_dict)
        break_flag = False

        for x in range(0,76):
            q+=1

            if cracked == Password:
                et = time.time()
                print(f"your password is: {cracked}\ncracked in {et-st} seconds")
                break_flag = True
                break

            if visualfeedback == True:
                print(cracked)
                
            var_dict["0"] = characters[q]

            if var_dict["0"] == "~":
                y += 1
                q = 0
                var_dict["1"] = characters[y]
                var_dict["0"] = 0
                if var_dict["1"] == "~":
                    z += 1
                    y = 0
                    var_dict["2"] = characters[z]
                    var_dict["1"] = 0
                    if var_dict["2"] == "~":
                        c += 1
                        z = 0
                        y = 0
                        var_dict["3"] = characters[c]
                        var_dict["2"] = 0
                        if var_dict["3"] == "~":
                            v += 1
                            c = 0
                            z = 0
                            y = 0
                            var_dict["4"] = characters[v]
                            var_dict["3"] = 0
                            print("lol")
                            if var_dict["4"] == "~":
                                b += 1
                                v = 0
                                c = 0
                                z = 0
                                y = 0
                                var_dict["5"] = characters[b]
                                var_dict["4"] = 0

        
        if break_flag == True:
            break