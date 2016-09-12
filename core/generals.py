#!/usr/bin/env python
# -*- coding: utf-8 -*-
#**
#
########
# Sack #
########
#
# Sack depends of this file
# For full copyright information this visit: https://github.com/jofpin/sack
#
# Copyright 2016 by Jose Pino <jofpin@gmail.com>
#**

import sys
import os
import urllib2
import time
import importlib

class generals:
    'Functions to get is right'
    def __init__(self):
        pass

    'Simplification print'
    @staticmethod
    def Go(string):
        print string

    @staticmethod
    def GoTime(s, string):
      if s == 1:
        print("\033[01;31mError: %s\033[00m")
        sys.exit(1)
      elif s == 2:
        print("[%s]\033[01;32m %s\033[00m" %(time.strftime("%H:%M:%S"),string))
      elif s == 3:
        print("\033[01;37m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),string))
      else:
        print("\033[01;37m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),string))

    @staticmethod    
    def ImportModule(values):
      return importlib.import_module(values)

    # All color for design terminal UI
    Color = {
      "purple": "\033[95m",
      "purpleBold": "\033[01;95m",
      "cyan": "\033[36m",
      "cyanBold": "\033[01;36m",
      "blue": "\033[94m",
      "blueBold": "\033[01;34m",
      "red": "\033[91m", 
      "redBold": "\033[01;31m",
      "green": "\033[92m", 
      "greenBold": "\033[01;32m",
      "white": "\033[0m", 
      "whiteBold": "\033[01;37m",
      "yellow": "\033[93m",
      "yellowBold": "\033[01;33m"
    }

    # Text in bold, lines and end.
    Text = {
      "underline": "\033[4m",
      "bold": "\033[1m",
      "end": "\033[0m"
    }

    @staticmethod
    def checkOS():
        if "linux" in sys.platform:
            os.system("clear")
            generals.Go("Loading" + " " + generals.Color["green"] + "sack" + generals.Color["blue"] + "...")
            time.sleep(0.3)
            pass
        elif "win" in sys.platform:
            os.system("cls")
            generals.Go("Currently there is no support for Windows.")
        else:
            pass
