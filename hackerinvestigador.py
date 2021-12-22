import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

os.system("clear")

id = os.getuid()

if id != 0:
 exit(Fore.RED+"RUN THE SCRIPT AS SUDO")
else:
 pass

def printools():
 print(Fore.GREEN+"Ferramenta Gau                                                            "+Fore.RED+"[+]"+Fore.BLUE+"1")
 print(Fore.GREEN+"Feramenta Sherlock                                                        "+Fore.RED+"[+]"+Fore.BLUE+"2")
 print(Fore.GREEN+"Ferramenta Twint                                                          "+Fore.RED+"[+]"+Fore.BLUE+"3")
 print(Fore.GREEN+"Feramenta Exiftool                                                        "+Fore.RED+"[+]"+Fore.BLUE+"4")
 print(Fore.GREEN+"Ferramenta Ngrok                                                          "+Fore.RED+"[+]"+Fore.BLUE+"5")
 print(Fore.GREEN+"Ferramenta Zphisher                                                       "+Fore.RED+"[+]"+Fore.BLUE+"6")
 print(Fore.GREEN+"Feraamenta Saychesse                                                      "+Fore.RED+"[+]"+Fore.BLUE+"7")
 print(Fore.GREEN+"Ferramenta Seeker                                                         "+Fore.RED+"[+]"+Fore.BLUE+"8")
 print(Fore.GREEN+"Download all options                                                      "+Fore.RED+"[+]"+Fore.BLUE+"9")
printools()

#choice = input("Choose => ")

def install():
 choice = int(input("Choose => "))
 
 if choice == 1:
  print(os.system("go install github.com/lc/gau/v2/cmd/gau@latest && clear && ls --color"))
  os.system("mv /root/go/bin/gau /usr/local/bin")
  print("====> gau -h")
  print(Fore.RED+"BOM HACKING ☕ ")

 elif choice == 2:
  os.system("clear") 
  print(os.system("git clone https://github.com/sherlock-project/sherlock"))
  print(os.system("ls --color ")) 
  print(Fore.RED+"BOM HACKING ☕ ")

 elif choice == 3:
  os.system("clear")
  print(os.system("git clone https://github.com/twintproject/twint"))
  print(os.system("ls --color ")) 
  print(Fore.RED+"BOM HACKING ☕ ")

 elif choice == 4:
  os.system("clear")
  ask = input("Gostaria de abaixar do apt/git ? ")
  if ask == 'git':
   print(os.system("git clone https://github.com/ghuseyin/exiftool-for-termux"))
  elif ask == 'apt' :
   print(os.system("sudo apt install exif")) 


 elif choice == 5:
  print(os.sytem("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz "))
  print(os.sytem("sudo tar xvzf ~/Downloads/ngrok-stable-linux-amd64.tgz -C /usr/local/bin"))
  os.system("rm -rf ngrok-stable-linux-amd64.tgz")
  print("===> ngrok -h"+Fore.RED+"  Bom Hacking ☕")
  
 elif choice == 6:
  os.system("git clonehttps://github.com/htr-tech/zphisher")
  os.system("ls --color ")
  print(Fore.RED+"BOM HACKING ☕ ")

 elif choice == 7:
  print(os.system("git clone https://github.com/hangetzzu/saycheese && clear")) 
  print(os.sytem("ls --color ")) 
  print(Fore.RED+"BOM HACKING ☕ ")
 
 elif choice == 8:
  print(os.system("git clone https://github.com/thewhiteh4t/seeker"))
  os.system("ls --color ")
  print(Fore.RED+"BOM HACKING ☕ ")

 else:
  os.system("clear") 
  exit(Fore.RED+"NO SUCH OPTION {}".format(choice))

install()

