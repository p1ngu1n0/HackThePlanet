#!/usr/bin/env python3         
# -*- coding: utf-8 -*-

################################
#	  autor: @_p1ngu1n0_       #
################################     
import os
import sys
import git 
import json
import random
import requests
import subprocess

banner = str()
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"     \            _    _            _     "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"      \          | |  | |          | |    "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"       \\        | |__| | __ _  ___| | __ "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"        \\       |  __  |/ _` |/ __| |/ / "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"         >\/7    | |  | | (_| | (__|   <  "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"     _.-(6'  \   |_|  |_|\__,_|\___|_|\_\ "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"    (=___._/` \         _   _           "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"         )  \ |        | | | |          "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"        /   / |        | |_| |__   ___  "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"       /    > /        | __| '_ \ / _ \ "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"      j    < _\        | |_| | | |  __/ "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"  _.-' :      ``.       \__|_| |_|\___| "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"  \ r=._\        `. "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r" <`\\_  \         .`-.          _____  _                  _   _  "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"  \ r-7  `-. ._  ' .  `\       |  __ \| |                | | | | "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"   \`,      `-.`7  7)   )      | |__) | | __ _ _ __   ___| |_| | "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"    \/         \|  \'  / `-._  |  ___/| |/ _` | '_ \ / _ \ __| | "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"               ||    .'        | |    | | (_| | | | |  __/ |_|_| "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"                \\  (          |_|    |_|\__,_|_| |_|\___|\__(_) "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"                 >\  > "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"             ,.-' >.' "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"            <.'_.'' "+"\n"
banner += "\033[0;"+str(random.randint(90, 97))+"m"+r"              <' "+"\n\u001b[0m"

class HackThePlanet:
    def __init__(self):
        self.run        = True
        self.path       = os.getcwd()
        self.file       = "mirrors.txt"
        self.promp      = "\nroot@newbie#> "
        self.clear      = lambda : os.system("cls") if os.name == "nt" else os.system("clear")
        self.parse      = dict()
        self.tools      = dict()
        self.install    = dict()
        self.contador   = 1
        self.caregory   = dict()
        self.opt_tool   = str()
        self.opt_cate   = str()

    def search(self):
        "Buscar una tool"
        pass

    def exit(self):
        "Salir del programa"
        self.run = False

    def menu_func(self, opciones):
        "Genera menus"
        for x ,y in opciones.items():
            print("{}) {}".format(x, y.__doc__))
        opciones.get(input(self.promp), None)()
    
    def instalar(self):
        "Instalar Tool"
        mirror = open(self.file, "r").readlines()
        #Parseo
        for x in mirror:
            self.parse.update(json.loads(requests.get(x+".json").text))
        #Obtener categoria con numero de opcion
        for y in self.parse.keys():
            self.caregory[str(self.contador)] = y
            self.contador += 1
        self.contador = 1
        #Visualizar Categorias
        for x ,y in self.caregory.items():
            print("{}) {}".format(x, y))
        self.opt_cate = self.caregory.get(input(self.promp), None)
        if self.opt_cate == "99":
            self.run = False
        #Obtener Tool con numero de opcion
        for x in self.parse[self.opt_cate].keys():
            self.tools[str(self.contador)] = x
            self.contador += 1
        self.contador = 1
        #Visualizar Tools
        for x ,y in self.tools.items():
            print("{}) {}".format(x, y))
        self.opt_tool = self.tools.get(input(self.promp), None)
        if self.opt_tool == "99":
            self.run = False
        #Instalar
        print("Descargando "+self.opt_tool)
        try:
            git.Git("tools").clone(''.join(self.parse[self.opt_cate][self.opt_tool].keys()))
        except git.exc.GitCommandError as s:
            print("Ya se encuentra instalada mira en la carpeta tools o hay algun error: "+s)
        print("Descargando en {}/tools/{}/   !".format(os.getcwd(), self.opt_tool))
      
    def apploop(self):
        "Bucle del programa"
        self.clear()
        print("{}\n{}\n".format(banner, random.choice(["Hack The Planet !", "\\(^v^)/\\(^v^)/\\(^v^)/\\(^v^)/\\(^v^)/", "https://exilon.ga/", "Sigueme en instagram @_p1ngu1n0_"])))
        while self.run:
            try:
               self.menu_func({"1":self.instalar, "99":self.exit})
            except TypeError:
                print("Opcion no valida")
                pass
    
if __name__ == '__main__':
    HackThePlanet().apploop()
    