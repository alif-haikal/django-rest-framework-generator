#-*- coding: utf8 -*-

from config import con
from config import config_dict
from generate_view import *
from generate_url import *
from generate_model import *
from generate_serializer import *


print("""
            ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗  
            ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║  
            ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║  
            ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║  
            ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║  
            ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝  

 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

""")

def choice():

    print('\u0336'.join("\n1. Generate VIEW") + '\u0336')
    print("2. Generate URL")
    print("3. Generate MODEL")
    print("4. Generate SERIELIZER")
    print("\n99. Exit!")


    ch = input("\nEnter Your Choice : ")
    if ch == str(1):
        print("still development")
        choice()
    elif ch == str(2):
        generate_url(con,config_dict)
        choice()
    elif ch == str(3):
        generate_model(con,config_dict)
        choice()
    elif ch == str(4):
        generate_serializer(con,config_dict)
        choice()
    elif ch == str(99):
        print("See You again!")
        exit()
        pass
    else:
        print("Please Enter Valid Input")
        choice()

choice()