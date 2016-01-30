import sys
import time
from random import randint
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
 
#Definition des procédures et fonctions

#Cette donction s'occupe de cliquer avec les informations envoyer
def addclick(driver, id, id_rouge, bouton_final_absent, speed):
    #On localise la première annonce et on clique dessus
    driver.find_element_by_id(id).click()
    
    #on attend
    time.sleep((randint(0,3*100)/100))
    
    #On clique sur le bouton rouge (si celui si existe bien sur)
    if id_rouge != 0:
        driver.find_element_by_xpath(id_rouge).click()

    #on attend
    time.sleep((randint(0,3*100))/100)

    #Une nouvelle fenetre s'ouvre, on doit donc switch sur celle si :
    driver.switch_to_window(driver.window_handles[-1])

    #On va alors attendre que le temps sois écoulé
    x=1
    actualTime = time.time()
    while x:
        isPresent = len(driver.find_elements_by_xpath(bouton_final_absent))
        if isPresent != 1:
            time.sleep(3)
            #On clique sur le bouton orange qui est apparue, et donc on ferme la fenetre
            driver.find_element_by_css_selector("a.button.small2.orange").click()
            x=0
        else:
            time.sleep((randint(0,3*100))/100)
        #Ou cas ou il y aurais une erreur on ferme tout seul au bout de 3 minutes
        if int(time.time()-actualTime) >= 3*60:
            x=0


    #On revient sur la fenetre principale
    driver.switch_to_window(driver.window_handles[0])

    #On tire le temps a attendre
    rnd = (randint(1,1*100)/100)+(int(speed))
    
    #On imprime les resultats
    print ("Add viewed sucessfully. Next add in "+str(rnd)+"s")

    #On attend pour finir
    time.sleep(rnd)

    #On return notre driver
    return driver

#cette procédure va vérifier si une pause est nécéssaire ou non
def pause():
    if randint(0,30)==5:
        rnd = randint(2*60*100,3*60*100)/100
        print ("We make a little pause of "+ str(rnd)+" seconds ! (because it's so exhausting to click on adds xD) \n")
        time.sleep(rnd)

#Introduction
print ("NeoBot By Linktag for NULLED\n\nThis bot is FREE and OPEN SOURCE, it can be download here :https://github.com/linktag/NeoBot\nIf you buy this programm to anyone, pls report him to Linktag17 on Nulled.io and ask for a refund\n\n")
time.sleep(3)

#on recupère les données
file = open("data", "r")
inf = (file.read()).split("\n")
file.close()
user = inf[0]
psw = inf[1]
speed = inf[2]
see_addprize = inf[3]
make_pause = inf[4]

#On va commencer par la fonction debut
i = 1
print ("Let's go !\n")

#Ouverture de la page
print ("1 - Open Firefox and go to Neobux")
driver = webdriver.Firefox()
driver.get("https://www.neobux.com/m/l/?vl=1062F974ABAAB97FF378E7C9964A55B1")

#Connexion à Neobux
print ("2 - Connection to Neobux with username = "+user+" and password = "+psw)
driver.find_element_by_id("Kf1").send_keys(user)
driver.find_element_by_id("Kf2").send_keys(psw)

#On verifie la presence d'un Captcha ( en faites on vérifie si le captcha est caché, et si c'est le cas on ne fait rien, si on ne trouve rien c'est qu'il n'est pas caché et donc on test)
isPresent = len(driver.find_elements_by_xpath("//input[@id='Kf3'][@type='hidden']"))
if isPresent == 0:
    captcha = input("2BIS - A captcha has been detected. Can you please enter it just here :")
    driver.find_element_by_id("Kf3").send_keys(captcha)
    
#On attend d'arriver sur la page principale
driver.find_element_by_id("botao_login").click()
time.sleep(randint(4*100,6*100)/100)

#On créer nos variables
nb_adds=0

#On va maintenant chercher le bouton pour aller sur la page des pubs
print("3 - Click on advertissment page")
driver.find_element_by_xpath("//td[@valign='bottom']/table/tbody/tr/td/a[@class='button green'][1]").click()


#On compte les pubs a voir
i=1
while i!=0:
    if len(driver.find_elements_by_id("da"+str(i)+"a")) != 0:
        nb_adds = nb_adds+1
        i = i+1
    else:
        i = 0

#On reset i
i = 1

#On indique le nombre de pub
print("4 - There is "+str(nb_adds)+" adds on this page.\n \n")

#On vérifie si il y a des pubs
if nb_adds !=0:

    #On attend
    time.sleep(randint(1*100,4*100)/100)

    #On peut commencer a visionner les pubs (si il y en a)

    while i <= (nb_adds):
        #On affiche le nom
        print ("Add number "+str(i))

        #On envoie a la fonction pour cliquer tous les données nécéssaire (le driver, l'ID de la pub, le XPAth du bouton rouge et le prix la pub
        if len(driver.find_elements_by_xpath("//div[@id='da"+str(i)+"a']/div[@class='ad0']"))==0 :
            driver = addclick(driver, "da"+str(i)+"a", "//span[@id='da"+str(i)+"c']/a[1]", "//table[@id='o1'][@style='display:none;']", speed)

            #On calcul si l'on fait une pause ou non
            if make_pause ==1:
                pause()
        else:
               print("This add has already been seen")
            
        #On incremente
        i = i+1
        
        #On saute une ligne
        print("\n")


#On a finit, on imprime ca !
print ("\nAll Adds viewed !! Congratulation =DD \n\n")

#On finit par recupérer les ADprizes
print ("Now we will get our Adprize. Refreshing ")

#On refresh la page
driver.refresh()

#On attend
time.sleep(randint(1*100,4*100)/100)

#On vérifie de base si ils existent
isPresent = len(driver.find_elements_by_xpath("//a[@class='button small2 blue']/span[1]"))
if isPresent !=0 and see_addprize!=0:
    #On clique sur le bouton 
    driver.find_element_by_xpath("//a[@class='button small2 blue']/span[1]").click()
	
    #On regarde le nombre d'adprize
    nb_adprize = int(driver.find_element_by_xpath("//span[@id='ap_hct']/a[1]").text)

    #On l'affiche
    print ("\nThere is "+str(nb_adprize)+" adprize to see\n")
    
    #On lance la routine
    i=1
    while i <= (nb_adprize):
        #On affiche le nom
        print ("AdPrize number "+str(i))

        #On envoie a la fonction pour cliquer tous les données nécéssaire (le driver, l'ID de la pub, le XPAth du bouton rouge et le prix la pub
        driver = addclick(driver, "ap_hct", 0, "//table[@id='prm0'][@style='padding-bottom:5px;display:none;']", speed)
        
        #On incremente
        i = i+1

        #On calcul si l'on fait une pause ou non
        if make_pause ==1:
            pause()
else:
    print ("No adprize")

#On a terminé, on peut conclure
print("Congratulation. The bot is terminated and it ll close in 10 secs. Thanks for using it !")
time.sleep(10)
driver.close()
