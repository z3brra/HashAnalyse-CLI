#! /usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib
import os

class Entity:
    """# Défine entity used with File object
    """
    def __init__(self, root_path: str) -> None:
        self.root_path = root_path
        self.__file_path = None
        self.__file_name = None
        self.__hashkey = None

    @property
    def path(self) -> str:
        return self.__file_path

    @path.setter
    def path(self, file_path: str) -> None:
        self.__file_path = file_path

    @path.deleter
    def path(self) -> None:
        del self.__file_path

    @property
    def name(self) -> str:
        return self.__file_name

    @name.setter
    def name(self, file_name_value: str) -> None:
        self.__file_name = file_name_value
    
    @name.deleter
    def name(self) -> None:
        del self.__file_name

    @property
    def hashkey(self) -> str:
        return self.__hashkey
    
    @hashkey.setter
    def hashkey(self, hashkey: str) -> None:
        self.__hashkey = hashkey
    
    @hashkey.deleter
    def hashkey(self) -> None:
        del self.__hashkey
    

class File(Entity):
    """## Classe File
    define a file method
    """
    def __init__(self) -> None:
        super().__init__("%s/TargetFiles" %os.getcwd())

    def get_all_path(self) -> list[dict[str, str]]:
        return [{name: os.path.join(path, name)} for path, subdirs, files in os.walk(self.root_path) if 'Class' not in path for name in files if 'hash_analyse.py' not in name]

    def ask_path(self, number: int) -> None:
        all_path = self.get_all_path()
        my_dict = all_path[number-1]
        for k_name, v_path in my_dict.items():
            self.name =  k_name
            self.path = v_path

    def format_list(self) -> list[dict[int, str]]:
        folder = self.get_all_path()
        proper_list = list()
        for index, dict_value in enumerate(folder):
            for name in dict_value.keys():
                proper_list.append({index+1: name})
        return proper_list

    def get_hashkey(self) -> str:
        m = hashlib.md5()
        try :
            with open(self.path, 'rb') as fiche:
                line = fiche.read()
                m.update(line)
            md5code = m.hexdigest()
            self.hashkey = md5code
            return self.hashkey
        except:
            return None