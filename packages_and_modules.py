

"""
    any file with .py extension --> python module

    you can import its content into another module

"""

"""1- import all the module """
# import  data_engineering
# data_engineering.sayhello()
# print(data_engineering.track_name)

"import part of the module inside another module"
# from data_engineering import sayhello
#
# sayhello()

"""Alias imported parts """
# import data_engineering  as de
# print(de.track_name)

# import pandas as pd . import tensorflow as tf

# from data_engineering import sayhello as myfun
# myfun()


""" check this scenario"""
from data_engineering import track_name

# in python each python module has its own main --->
# in the file ?? it is defined global on the module __name__ = '__main__'
# this variable contains the entry point of the file
# the file is executed once its called

# print(track_name)
# """ modify track name"""
# track_name = 'updated track'
# print(track_name)

# modify value of variable in the current memory (for current module)

print("***************************************************")
"1- import module from package"
# import  iti.greeting
# iti.greeting.saywelcome()
#
# import  iti.greeting as gt
# gt.saywelcome()

"""2- import part of the module from package"""
# from iti.greeting import saywelcome
# saywelcome()

""" call ask for int from data_eng package"""

# from data_eng.inputs_module import ask_for_int
from data_eng import ask_for_int
num1 = ask_for_int('please enter first number')
num2 = ask_for_int('please enter second number')
res= num1 + num2
print(res)


from data_eng import pkg_name

