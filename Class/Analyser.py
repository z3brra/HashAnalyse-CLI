#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import platform
import sys

from .Colors import colorize
from .Entity import File

class Analyse:
    """## Class for file anlayse."""
    def __init__(self, **kwargs):#, title: str, subtitle: str, bar: str, footer: str):
        self.title = kwargs['title']
        self.subtitle = kwargs['subtitle']
        self.author = kwargs['author']
        self.bar = kwargs['bar']
        self.footer = kwargs['footer']
        self.file = File()
        self.__input_hashkey = None


    @property
    def input_hashkey(self) -> str:
        return self.__input_hashkey

    @input_hashkey.setter
    def input_hashkey(self, file_hashkey: str) -> None:
        self.__input_hashkey = file_hashkey
    
    @input_hashkey.deleter
    def input_hashkey(self) -> None:
        del self.__input_hashkey

    def header(self):
        print(colorize.text2art(self.title, 'light_red', None, ['bold']))
        str_subtitle = colorize.colored(self.subtitle, 'light_blue')
        str_author = colorize.colored(self.author, 'yellow', None, ['bold', 'blink'])
        print(f"{str_subtitle}{str_author}\n".center(100))
        print(colorize.colored(self.bar, 'blue'))
        print('\n')
    
    def clear(self):
        if platform.system().lower() == "linux":
            os.system('clear')
        elif platform.system().lower() == "windows":
            os.system("cls")

        self.header()


    def pfooter(self, color:str):
        print(colorize.colored(f"\n{self.footer}", color, None, ['bold']))

    def show_file(self):
        folder = self.file.format_list()
        for dict_value in folder:
            for index_key, name_value in dict_value.items():
                text_index = colorize.colored(index_key, 'light_red', None, ['bold'])
                text_name = colorize.colored(name_value, 'yellow', None)
                print(f"{text_index:>40} {text_name}")
        print('\n')

    def ask_file(self):
        print(colorize.colored(self.bar, 'blue'))
        print(colorize.colored('\nEntrer le numéro du fichier : ', 'cyan', None, ['bold']), end='')
        index = 0
        while index == 0:
            try:
                index_input = int(input())
            except ValueError:
                index_input = 0
            if index_input > 0 and index_input <= len(self.file.format_list()):
                index = index_input
            else:
                print(colorize.colored(f"Entrer le numéro du fichier [1 : {len(self.file.format_list())}] : ", 'green', None, ['bold']), end='')
                index_input = 0
        self.file.ask_path(index)

    def ask_hashkey(self):
        text_var2 = colorize.colored(self.file.name, 'yellow')
        text_var1 = colorize.colored(f"Entrer la clé md5 du fichier {text_var2} : ", 'cyan', None, ['bold'])
        print(text_var1, end='')
        self.input_hashkey = input()

    def compare(self) -> bool:
        return self.input_hashkey == self.file.get_hashkey()

    def response(self):
        system_name = platform.uname()[1]
        system_user = os.getenv('USERNAME', 'defaultValue')
        if self.compare():
            text = colorize.colored("L'empreinte du fichier correspond avec celle reçue en amont..", 'green', None, ['bold'])
        else:
            text_var1 = colorize.colored("L'empreinte reçue ne correspond pas avec l'empreinte sur le système ", 'light_red', None)
            text_var2 = colorize.colored(system_name, 'yellow', None, ['bold'])
            text_var3 = colorize.colored("\nLe fichier pourrait corrompre les données de l'utilisateur ", 'light_red', None, )
            text_var4 = colorize.colored(system_user, 'yellow', None, ['bold'])
            text = f"{text_var1}{text_var2}{text_var3}{text_var4}\n"
        self.clear()
        print(text)
        print(colorize.colored(f"\n{self.bar}\n", 'green'))
    
    def is_file(self) -> bool:
        folder = self.file.format_list()
        if len(folder) > 0:
            return True
        return False

    def execute(self):
        self.clear()
        if self.is_file():
            self.show_file()
            self.ask_file()
            self.ask_hashkey()
            self.response()
        return

    def loop(self) -> bool:
        if self.is_file():
            answer = ""
            while answer == "":
                text1 = colorize.colored('Voulez vous faire une analyse de fichier ?', 'green', None, ['bold'])
                str_yes = colorize.colored('[Y/N] or', 'light_blue', None, ['bold'])
                str_no = colorize.colored('[y/n] >', 'light_blue', None, ['bold'])
                print(f"{text1} {str_yes} {str_no} ", end="")
                answer_input = input()

                if answer_input == "Y" or answer_input == "y" or answer_input == 'Yes' or answer_input == 'yes':
                    answer = answer_input
                    return True
                elif answer_input == "N" or answer_input == "n" or answer_input == 'No' or answer_input == 'no':
                    self.pfooter('green')
                    return False
                else:
                    answer_input = ""    
        else:
            self.clear()
            str1 = colorize.colored(f"Le dossier", 'red', None, ['bold'])
            str_folder = colorize.colored(os.path.basename(self.file.root_path), 'yellow', None, ['bold'])
            str2 = colorize.colored("est vide.\n", 'red', None, ['bold'])
            return print(f"{str1} {str_folder} {str2}".center(110))
    

    def run(self):
        self.header()
        while self.loop():
            self.execute()
        sys.exit(1)