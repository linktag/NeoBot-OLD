import sys
x=True
answer =0
print ("Welcome to NeoBot's settings !\n\n")
while x:
    f = open("data",'r')
    file  = (f.read()).split("\n")
    f.close()
    print ("Just enter the nember of what setting you want to change")
    print ("1) Username :"+file[0])
    print ("2) Password :"+file[1])
    print ("3) Speed :"+file[2]+"s")
    print ("4) See Addprize :"+file[3])
    print ("5) Make some pause :"+file[4]+"\n")
    print ("0) Stop this programm")
    answer = input ("Your answer:")
    if answer =="0":
        x = False
    elif answer =="1":
        file[0] = input("New username:")
    elif answer =="2":
        file[1] = input("New password:")
    elif answer =="3":
        file[2] = input("New speed (number of seconds between each add.\nThe humanizer will randomly add betwen 0.1 and 1s)\n:")
    elif answer =="4":
        file[3] = input("Do you want to see adprize ? (1=Yeah,0=No!):")
    elif answer =="5":
        file[4] = input("Do you want to makes so pause (5% chance between each adds) (1=Yeah,0=No!):")
    else:
        print ("Invalid answer.")
    f = open("data",'w')
    f.write(file[0]+"\n"+file[1]+"\n"+file[2]+"\n"+file[3]+"\n"+file[4])
    f.close()
