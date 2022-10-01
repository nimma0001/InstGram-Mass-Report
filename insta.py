from files.helpfun import  runreport, listofoption, Nudity, bull
import json




reprtn=('username of the account u want to report : ')
wait = input('wait after login set to 2 if all already logined all other wise 40: ')
for x in listofoption:
    print(x)
typeof = []
useri = input('choose 1-5: ')
typeof.append(useri)
print(typeof)
if typeof[0] == "2":
    for x in range(len(Nudity)):
        print(Nudity[x])
    useri = int(input('choose 1-4: '))
    typeof.append(useri)
    typeof[1] = typeof[1] - 1
    typeof[1] == Nudity[typeof[1]]
if typeof[0] == "4":
    for x in bull:
        print(x)
    useri = int(input('choose 1-3: '))
    typeof.append(useri)
    typeof[1] = typeof[1] - 1
    typeof[1] == bull[typeof[1]]
#
upfile = json.load(open("config.json"))
upfile = upfile['accounts']
runreport(upfile, typeof, reprtn, wait)  
