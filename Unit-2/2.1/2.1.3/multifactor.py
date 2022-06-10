# a213_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restricted app
my_auth = mfg.MultiFactorAuth()

# set the users authentication information
question = "What is the acronym of the high school you go to"
answer = "BASE"
my_auth.set_authentication(question, answer)
my_auth.set_authorization('admin', "thisissosecure100%")

# start the GUI
my_auth.mainloop()
