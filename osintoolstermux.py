import os
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

os.system("clear")

def ban():
 banner = """
                              `                     
                 zeI?:`      ` `:?yo,              
                :@@@@@Qdey}Fokg@@@@@w           `` 
                h@@@@@@@@@@@@@@@@@@@@\`            
               :@@@@@@@@@@@@@@@@@@@@@M.            
               e@@@@@@@@@@@@@@@@@@@@@@\            
              ,Q@@@@@@@@@@@@@@@@@@@@@@q            
              i@@@@@@@@@@@@@@@@@@@@@@@Q~           
              6@@@@@@@@@@@@@@@@@@@@@@@@/           
             .B@@@@@@@@@@@@@@@@@@@@@@@@S           
             :@@@@@@@@@@@@@@@@@@@@@@@@@p           
             ;@@@@@@@@@@@@@@@@@@@@@@@@@R`   `      
     ,'`     ~B@@@@@@@@@@@@@@@@@@@@@@@Qa``    .,'  
    .B@@QMwz>:` `,:+|lv{FyoSjFsl/>;,'` `'^z6B@@@e  
     \Q@@@@@@@Qg6Fi=;:,''.```.',:;?luERQ@@@@@@@U,  
      `:\yqgQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@QN9Fr.    
            `',:;+*\ii(vvvvzvvvvv7i/?+;:,`         

  """
 #print(banner)
 return banner
print(Fore.BLUE+ban())

tool1 = "go install github.com/lc/gau/v2/cmd/gau@latest"
tool2 = "git clone https://github.com/sherlock-project/sherlock"
tool3 = "git clone https://github.com/twintproject/twint"
tool4 = "git clone https://github.com/Datalux/Osintgram"
tool5 = "git clone https://github.com/ghuseyin/exiftool-for-termux"
tool6 = "wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz"
tool7 = "git clone https://github.com/htr-tech/zphisher"
tool8 = "git clone https://github.com/hangetzzu/saycheese"
tool9 = "git clone https://github.com/thewhiteh4t/seeker.git"

list = [tool1, tool2, tool3, tool4, tool5, tool6, tool7, tool8, tool9]

def printools():
 print(Fore.GREEN+"Ferramenta Gau                                                            "+Fore.RED+"[+]"+Fore.BLUE+"1")
 print(Fore.GREEN+"Feramenta Sherlock                                                        "+Fore.RED+"[+]"+Fore.BLUE+"2")
 print(Fore.GREEN+"Ferramenta Twint                                                          "+Fore.RED+"[+]"+Fore.BLUE+"3")
 print(Fore.GREEN+"Feramenta OsintGram                                                       "+Fore.RED+"[+]"+Fore.BLUE+"4")
 print(Fore.GREEN+"Feramenta Exiftool                                                        "+Fore.RED+"[+]"+Fore.BLUE+"5")
 print(Fore.GREEN+"Ferramenta Ngrok                                                          "+Fore.RED+"[+]"+Fore.BLUE+"6")
 print(Fore.GREEN+"Ferramenta Zphisher                                                       "+Fore.RED+"[+]"+Fore.BLUE+"7")
 print(Fore.GREEN+"Ferramenta Saychesse                                                      "+Fore.RED+"[+]"+Fore.BLUE+"8")
 print(Fore.GREEN+"Ferramenta Seeker                                                         "+Fore.RED+"[+]"+Fore.BLUE+"9")
 print(Fore.RED+"Todas as Ferramentas                                                      "+Fore.RED+"[+]"+Fore.BLUE+"0")

printools()

def install():
 choice = int(input("Choose => "))

 if choice == 1:
  os.system("clear")
  os.system("{} && clear".format(tool1))
  print(Fore.RED+"BOM HACKING ☕ ")

 elif choice == 2:
  os.system("clear")
  print(os.system("{} && clear".format(tool2)))
  print(os.system("ls --color "))
  print(Fore.RED+"BOM HACKING ☕ ")

 elif choice == 3:
  os.system("clear")
  os.system("{} && clear && pip install -r twint/requirements.txt".format(tool3))
  os.system("ls --color")
  print(Fore.RED+"BOM HACKING ☕ ")

 elif choice == 4:
   os.system("clear")
   print(os.system("{} && clear".format(tool4)))
   print(os.system("ls --color "))
   print(Fore.RED+"BOM HACKING ☕ ")

 elif choice == 5:
  os.system("clear")
  ask = input("Gostaria de abaixar do pkg/git ? ")
  if ask == 'git':
   print(os.system("git clone https://github.com/ghuseyin/exiftool-for-termux && clear"))
   print(os.system("ls --color "))
   print(Fore.RED+"BOM HACKING ☕ ")
  elif ask == 'pkg':
   print(os.system("pkg  install exiftool && clear && echo 'exif --help' "))
   print(Fore.RED+"BOM HACKING ☕ ")

 elif choice == 6:
  os.system("clear")
  print(os.system("{} ".format(tool6)))
  print(os.system("tar xvzf ngrok-stable-linux-amd64.tgz"))
  os.system("rm -rf ngrok-stable-linux-amd64.tgz && clear")
  print("===> ngrok -h"+Fore.RED+"  Bom Hacking ☕")

 elif choice == 7:
  os.system("clear")
  os.system("{} && clear ".format(tool7))
  os.system("ls --color ")
  print("===> bash zphisher/zphisher.sh "+Fore.RED+"BOM HACKING ☕ ")

 elif choice == 8:
  os.system("clear")
  os.system("{} && clear".format(tool8))
  os.system("ls --color ")
  print("bash saycheese/saycheese.sh"+Fore.RED+"BOM HACKING ☕ ")

 elif choice == 9:
  os.system("clear")
  os.system("{} && clear".format(tool9))
  os.system("./seeker/install.sh && ls --color ")
  print(Fore.RED+"BOM HACKING ☕ ")

 elif choice == 0:
  for i in list:
   os.system("mkdir OSINTTOOLS && cd OSINTTOOLS") 
   os.system("{}".format(i)) 
  os.system("tar xvzf ngrok-stable-linux-amd64.tgz && rm -rf ngrok-stable-linux-amd64.tgz && clear && ls --color")
  print(Fore.RED+"BOM HACKING ☕ ")

 else:
  os.system("clear")
  exit(Fore.RED+"NO SUCH OPTION {}".format(choice))

install()

