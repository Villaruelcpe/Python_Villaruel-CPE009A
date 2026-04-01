# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:38:42 2026

@author: Administrator
"""

class TextFileReaderWriter:
    def read(self, filepath):
        file = open(filepath, "r")   
        print(file.read())           
        file.close()                

    def write(self, filepath, data):
        file = open(filepath, "w")   
        file.write(data)             
        file.close()                 
        print("Done writing!")

# Test the class directly 
tf = TextFileReaderWriter()
tf.write("sample.txt", "Kanye West")   
tf.read("sample.txt")             