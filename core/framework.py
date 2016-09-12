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

import os
import sys
import glob
import readline
import random
import urllib2

# Imports own
from core.config import Config
from core.generals import generals

# Define the settings or data of users to reflect
config = Config()

# The class principal, this is based on the life of ((-> sack <-))
class sack(object):
    def __init__(self):
        self.point = "."
        self.suffix = "py"
        self.modules = []
        self.define = "modules"
        self.path = self.point + "/" + self.define
        self.listing = self.modules

    # Important: in the process of use is possible that will ask for the root
    def rootConnection(self): 
        if os.getuid() != 0:
            generals.Go("\t" + "-------------------")
            generals.Go("\t" + "> Welcome to " + config.nameFramework + " <")
            generals.Go("\t" + "-------------------")
            generals.Go(generals.Color["blueBold"] + "[*] " + generals.Color["white"] + "Hello " + generals.Color["greenBold"] + os.uname()[1] + "," + generals.Color["white"] + " I hope you enjoy my role")
            generals.Go(generals.Color["redBold"] + "[x] " + generals.Color["white"] + "You must run in mode " + generals.Color["whiteBold"] + "root" + generals.Color["white"] + " to be able to operate.")
            exit(0)

    # Design principal of the header of sack
    def header(self, totalModules):
        generals.Go("\033[H\033[J")
        generals.Go("\t\t" + generals.Color["green"] + "███████╗ █████╗  ██████╗██╗  ██╗")
        generals.Go("\t\t" + generals.Color["green"] + "██╔════╝██╔══██╗██╔════╝██║ ██╔╝")
        generals.Go("\t\t" + generals.Color["green"] + "███████╗███████║██║     █████╔╝ ")
        generals.Go("\t\t" + generals.Color["green"] + "╚════██║██╔══██║██║     ██╔═██╗ ")
        generals.Go("\t\t" + generals.Color["green"] + "███████║██║  ██║╚██████╗██║  ██╗")
        generals.Go("\t\t" + generals.Color["green"] + "╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")
        generals.Go("")
        generals.Go("\t" + generals.Color["yellowBold"] + "      .:::" + generals.Color["redBold"] + "> " + generals.Color["whiteBold"] + "Footprint track-sessions" + " " + generals.Color["redBold"] + "<"  + generals.Color["yellowBold"] + ":::.  " + generals.Color["white"]) 
        generals.Go("\t" + generals.Color["blueBold"]   + "     --------------------------------------" +  generals.Color["white"])
        generals.Go("\t" + generals.Color["whiteBold"]  + "     x    " + generals.Color["blueBold"] + "🌎   " + generals.Color["redBold"] + "Hack the world happy" +  generals.Color["blueBold"] + "  🌍" + "     " + generals.Color["whiteBold"] + "x")
        generals.Go("\t" + generals.Color["blueBold"]   + "     --------------------------------------" + generals.Color["white"] + "\n")
        generals.Go("\t" + generals.Color["redBold"]    + "     " + "[*] " + generals.Color["whiteBold"]  + "Modules: " + generals.Color["white"] + generals.Color["blue"] + "%s" % (totalModules) + generals.Color["white"])
        generals.Go("\t" + generals.Color["redBold"]    + "     " + "[*] " + generals.Color["whiteBold"]  + "Version: " + generals.Color["white"] + generals.Color["blue"] + config.versionFramework + generals.Color["white"])
        generals.Go("\t" + generals.Color["yellowBold"] + "     " + "[!] " + generals.Color["whiteBold"]  + "Author: " + generals.Color["white"] + generals.Color["blue"] + config.authorName + generals.Color["blue"] + " (" + generals.Color["yellow"]+ config.authorNick + generals.Color["blue"] + "), " + config.authorTwitter + generals.Color["white"])
        generals.Go("\t" + generals.Color["yellowBold"] + "     " + "[!] " + generals.Color["whiteBold"]  + "Homepage: " + generals.Color["white"] + generals.Color["blue"] + config.homepage + generals.Color["white"] + "\n")
        generals.Go(generals.Color["blue"] + "  " + config.descriptionFramework + generals.Color["white"] + "\n")
 
    # Options of help, of easy use.
    def help(self, nameHelp):
        generals.Go("")
        generals.Go("----------")
        generals.Go("[!" + generals.Color["blueBold"] + " " + nameHelp + " " + generals.Color["white"] + "!]")
        generals.Go("----------")
        generals.Go("")
        generals.Go("These are all the commands that you can run in sack")
        generals.Go("")
        generals.Go("go     : " + generals.Color["blue"] + "load, call or execute a module" + generals.Color["white"])
        generals.Go("list   : " + generals.Color["blue"] + "open the list of all the modules" + generals.Color["white"])
        generals.Go("info   : " + generals.Color["blue"] + "to view information from a module" + generals.Color["white"])
        generals.Go("help   : " + generals.Color["blue"] + "to ask for help" + generals.Color["white"])
        generals.Go("reload : " + generals.Color["blue"] + "restart the console sack" + generals.Color["white"])
        generals.Go("about  : " + generals.Color["blue"] + "information on the creator author and collaborators" + generals.Color["white"])
        generals.Go("clear  : " + generals.Color["blue"] + "to clean the terminal" + generals.Color["white"])
        generals.Go("exit   : " + generals.Color["blue"] + "close or exit from the console sack" + generals.Color["white"])
        generals.Go("")

    # Autocompletion
    # Description: To maintain a clean console with autocompletion, this I help of stackoverflow <3
    # Url: http://stackoverflow.com/questions/187621/how-to-make-a-python-command-line-program-autocomplete-arbitrary-things-not-int/187660#187660
    def niceShell(text, state):
        matches = [i for i in commands if i.startswith(text)]
        if state < len(matches):
            return matches[state]
        else:
            return None

    # Autocompletion of console (shell sack)
    readline.parse_and_bind("tab:complete")
    readline.set_completer(niceShell)

    # Here we write the shell of sack. Where everything connected to call modules to run the magic
    def shell(self):
        command = None
        self.showList()
        self.header(len(self.listing))
        
        while True:
            try:
                command = raw_input(generals.Color["green"] + config.nameFramework + generals.Color["whiteBold"] + ":~>" + " " + generals.Color["white"]) or "help"
                command = command.split()
                # List modules
                if command[0] == "list" or command[0] == "ls":
                    generals.Go("")
                    generals.Go("---------------------")
                    generals.Go("[>" + generals.Color["blueBold"] + " List of modules " + generals.Color["white"] + "<]")
                    generals.Go("---------------------")
                    generals.Go("")
                    for module in self.listing:
                        try:
                            attribute = generals.ImportModule(self.define + self.point + "%s" % (module))
                        except ImportError:
                            generals.Go(generals.Color["redBold"] + "Alert: " + generals.Color["white"] + "There was a problem to the load the module " + generals.Color["blueBold"] + "\'%s\'" % (module))
                        else:
                            reflectModule = generals.Color["greenBold"] + "[" + generals.Color["blueBold"] + ">" + generals.Color["greenBold"] + "]" + generals.Color["white"] + " %s {%s} - %s" % (module, generals.Color["blue"] + attribute.doVersion + generals.Color["white"], attribute.doDescription)
                            generals.Go(reflectModule)
                    generals.Go("")
                elif command[0] == "go" or command[0] == "GO" or command[0] == "Go":
                    try:
                        preData = command[1]
                    except IndexError:
                        generals.Go(generals.Color["blueBold"] + "Usage:" + generals.Color["white"] + " go [module name] [commands]")
                    else:
                        self.go(command)
                elif command[0] == "exit" or command[0] == "close":
                    generals.Go(generals.Color["red"] + "Goodbye: " + generals.Color["white"] +  "Thank you for having me used, I hope soon.")
                    break
                elif command[0] == "clear":
                    generals.Go("\033[H\033[J")
                elif command[0] == "info":
                    try:
                        preData = command[1]
                    except IndexError:
                        generals.Go(generals.Color["blueBold"] + "Usage:" + generals.Color["white"] + " info [module name]")
                    else:
                        self.infoModule(preData)
                elif command[0] == "about":
                    generals.Go("")
                    generals.Go("---------------------------")
                    generals.Go("[>" + generals.Color["blueBold"] + "  Credits " + generals.Color["whiteBold"] + "&" + generals.Color["blueBold"] + " copyright  " + generals.Color["white"] + "<]")
                    generals.Go("---------------------------")
                    generals.Go("")
                    generals.Go(generals.Color["yellowBold"] + "[!] " + generals.Color['white'] + "Creator:" + " " + generals.Color["blue"] + config.authorName + generals.Color["blue"] + " (" + generals.Color["yellow"]+ config.authorNick + generals.Color["blue"] + ")")
                    generals.Go(generals.Color["yellowBold"] + "[!] " + generals.Color['white'] + "Contact:" + " " + generals.Color["blue"] + "email:" + generals.Color["green"] + "jofpin@gmail.com" + generals.Color["white"] + " | " + generals.Color["blue"] + "twitter:" + generals.Color["green"] + "@jofpin" + generals.Color["white"])
                    generals.Go(generals.Color["yellowBold"] + "[!] " + generals.Color['white'] + "Version:" + " " + generals.Color["blue"] + config.versionFramework + generals.Color['white'])
                    generals.Go(generals.Color["yellowBold"] + "[!] " + generals.Color['white'] + "Date:" + " " + generals.Color["blue"] + config.dateFramework + generals.Color['white'])
                    generals.Go("")
                elif command[0] == "reload":
                    self.header(len(self.listing))
                # Notices for the good writing of commands (list, clear, info)
                elif command[0] == "lis" or command[0] == "ist" or command[0] == "l" or command[0] == "lisr" or command[0] == "liss" or command[0] == "sl":
                    generals.Go(generals.Color["yellowBold"] + "Notice: " + generals.Color["white"] + "I think that tried of write " + generals.Color["blueBold"] + "'ls'" + generals.Color["white"] + " or " + generals.Color["blueBold"] + "'list'" + generals.Color["white"] + ", are those commands to see the list of modules.")
                elif command[0] == "cls" or command[0] == "cler" or command[0] == "c" or command[0] == "clean" or command[0] == "cl":
                    generals.Go(generals.Color["yellowBold"] + "Notice: " + generals.Color["white"] + "I think that tried of write " + generals.Color["blueBold"] + "'clear'" + generals.Color["white"] + ", the command to clean the console")
                elif command[0] == "inf" or command[0] == "in" or command[0] == "i" or command[0] == "if" or command[0] == "information":
                    generals.Go(generals.Color["yellowBold"] + "Notice: " + generals.Color["white"] + "I think that tried of write " + generals.Color["blueBold"] + "'info'" + generals.Color["white"] + ", the command to view the information of the modules")
                elif command[0] == "help":
                    self.help("Help")
                else:
                    generals.Go(generals.Color["redBold"] + "Error: " + generals.Color["blue"] +  "\'%s\' " % command[0] + generals.Color["white"] + "not be found the order, write command: " + generals.Color["whiteBold"] + "help" + generals.Color["white"])
            # Prevent closed easier, avoid interruption and continue.        
            except KeyboardInterrupt:
                generals.Go("")
                generals.Go(generals.Color["redBold"] + "Alert: " + generals.Color["white"] + "Interrupted.")
            except Exception as e:
                generals.Go(generals.Color["redBold"] + "Error: " + generals.Color["white"] + "%s" % e)

    # Preview module information
    def infoModule(self, moduleName):
        try:
            attribute = generals.ImportModule(self.define + self.point + "%s" % (moduleName)) 
        except ImportError:
            generals.Go(generals.Color["redBold"] + "Error: " + generals.Color["white"] + "not it can load " + generals.Color["blueBold"] + "\'%s\' " % (moduleName) + generals.Color["white"] + "in sack")
        else:
            try:
                generals.Go("")
                generals.Go(generals.Color["yellowBold"] + "[!]" + generals.Color["white"] + " " + "Information of " + generals.Color["blueBold"] + "%s" % moduleName + generals.Color["white"] + " " + "module")
                generals.Go("")
                generals.Go("name        :" + generals.Color["blue"] + " %s" % moduleName + generals.Color["white"])
                generals.Go("description :" + generals.Color["blue"] + " %s" % attribute.doDescription + generals.Color["white"])
                generals.Go("version     :" + generals.Color["blue"] + " %s" % attribute.doVersion + generals.Color["white"])
                generals.Go("date        :" + generals.Color["blue"] + " %s" % attribute.doDate + generals.Color["white"])
                generals.Go("author      :" + generals.Color["blue"] + " %s" % attribute.doAuthor + generals.Color["white"])
                generals.Go("")
            except IndexError:
                generals.Go(generals.Color["redBold"] + "Error: " + generals.Color["white"] + "set up well all the variables with the prefix (do) for this module.")

    # Configure the reading of those files with the suffix (.py)            
    def showList(self):
        principal = os.getcwd()
        os.chdir(self.path)
        self.modules = glob.glob("*" + self.point + self.suffix)

        # no modules
        if not self.modules:
            generals.Go(generals.Color["yellowBold"] + "Notice: " + generals.Color["white"] + "There are no modules available.")
        else:
            os.chdir(principal)
            for module in self.modules:
                module = module.split(self.point)[0]
                if module == "__init__":
                    continue
                self.listing.append(module)

    # Header design to modules            
    def headerModule(self, nameModule, versionModule, authorModule, copyrightModule):
        generals.Go("")
        generals.Go(generals.Color["greenBold"] + "+" + generals.Color["white"] + "--" + generals.Color["blue"] + "=" + generals.Color["yellowBold"] + "[->" + generals.Color["white"] + " " + nameModule)
        generals.Go(generals.Color["greenBold"] + "+" + generals.Color["white"] + "--" + generals.Color["blue"] + "=" + generals.Color["yellowBold"] + "[->" + generals.Color["white"] + " " + "Version: " + versionModule)
        generals.Go(generals.Color["greenBold"] + "+" + generals.Color["white"] + "--" + generals.Color["blue"] + "=" + generals.Color["yellowBold"] + "[->" + generals.Color["white"] + " " + "Author: " + authorModule)
        generals.Go(generals.Color["greenBold"] + "+" + generals.Color["white"] + "--" + generals.Color["blue"] + "=" + generals.Color["yellowBold"] + "[->" + generals.Color["white"] + " " + "Copyright: " + copyrightModule)
        generals.Go("")
        pass

    # Log Utility           
    def shellLog(self, msg):
        generals.Go("")
        generals.Go(generals.Color["greenBold"] + "+" + generals.Color["white"] + "--" + generals.Color["blue"] + "=" + generals.Color["yellowBold"] + "[->" + generals.Color["white"] + " " + msg) 
        pass

    def showIP(self):
        numberList = "0123456789."
        ip = ""
        request = urllib2.urlopen("http://checkip.dyndns.org").read()
        for reflectIP in str(request):
            if reflectIP in numberList:
                ip += reflectIP
        return ip

    # Add simple options    
    def usageOpt(self, string):
        generals.Go(generals.Color["blue"] + "Usage:" + " " + generals.Color["white"] + string)

    # Add html to file of redirect    
    def generatePost(self, url, urlAction, requestPost):
        # Create the page that will reidrect to the orignal page.
        #htmlFile = "redirect.html"
        #generals.Go("")
        #generals.Go(generals.Color["blueBold"] + "[*]" + " " + generals.Color["whiteBold"] + "Recent:" + " " + generals.Text["end"] + "updating file of redirection" + " " + generals.Color["white"] + "(" + generals.Color["blue"] + htmlFile + generals.Color["white"] + ")" + generals.Text["end"])

        #redirectFile = "redirect.html"
        #pathRedirect = os.getcwd() + "/data/" + indexFile

        with open("redirect.html", "w") as html:
            html.write("<!doctype html>")
            html.write("\n")
            html.write("<html>")
            html.write("\n")
            html.write("<head>") 
            html.write("\n")
            html.write("\t" + "<title>" + "Redirection.." + "</title>")
            html.write("\n")
            html.write("</head>")
            html.write("\n")
            html.write("<body>")
            html.write("\n")
            html.write("\t" + "<form id=\"sackForm\" action=\"%s\" method=\"post\" >\n" % urlAction)
            for post in requestPost:
                nameParameter = post.split()
                value = post.split()
                html.write("\t\t" + "<input name=\"%s\" value=\"%s\" type=\"hidden\" >\n" % (nameParameter, value))
            html.write("\t" + "</form>")
            html.write("\n")
            html.write("<!-- Submit data Form -->")
            html.write("\n")
            html.write("<!-- Copyright 2016 by Sack -->")
            html.write("\n")
            html.write("<script type=\"text/javascript\">document.forms[\"sackForm\"].submit();</script>")
            html.write("\n")
            html.write("</body>")
            html.write("\n")
            html.write("</html>")
        html.close()
#SERVER FIN

    # Execution of modules
    def go(self, command):
        moduleName = command[1]
        try:
            attribute = generals.ImportModule(self.define + self.point + "%s" % (moduleName))
            attribute.boot(command)
        except ImportError:
            generals.Go(generals.Color["yellowBold"] + "Notice: " + generals.Color["white"] + "no you can run " + generals.Color["blueBold"] + "\'%s\' " % moduleName + generals.Color["white"] + "inside sack; is likely that the module does not exist.")

    # Here we put at stake the shell, which runs the SACK class in the main file (sack.py)        
    def main(self):
        # Detect operating system, to compose the compatibility
        generals.checkOS()
        # Make a call to run the shell console
        framework = sack()
        framework.shell()