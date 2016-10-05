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

import requests
from libs.untangle import untangle

class geo(object):
    def __init__(self):
      # APIS of check ip & identify GEO
      self.apiIP = "https://api.ipify.org"
      self.apiGEO = "http://ip-api.com/json"
      self.varGeo = {}
      self.notFound = "not found"
        
    def showIPclient(self):
      ip = requests.get(self.apiIP).text
      return ip
    
    def getIPlookup(self, ipAddress = None):
      apiGeo = requests.get(self.apiGEO + "/" + str(ipAddress))
      data = apiGeo.json()
      if not ipAddress:
        message = "Error" + ":" + " " + "Not it has captured the ip of the victim"
        return message
      else:
        try:
          self.varGeo["ip"] = data["query"]
          self.varGeo["isp"] = data["isp"]
          self.varGeo["city"] = data["city"]
          self.varGeo["country"] = data["country"]
          self.varGeo["latitude"] = data["lat"]
          self.varGeo["longitude"] = data["lon"]
          print("\n[+] Information of victim:")
          print(" |- IP Victim: " + self.varGeo["ip"])
          print(" |- ISP: " + self.varGeo["isp"])
          print(" |- City: " + self.varGeo["city"])
          print(" |- Country: " + self.varGeo["country"])
          print(" |- Latitude: " + str(self.varGeo["latitude"]))
          print(" |- Longitude: " + str(self.varGeo["longitude"]))
        except Exception:
          print("Error" + ":" + " " + "Does not appear to be a valid IP" + ":" + " " + ipAddress)
    
    def getGeoInfo(self, ipAddress = None):
      apiGeo = requests.get(self.apiGEO + "/" + str(ipAddress))
      data = apiGeo.json()
      if not ipAddress:
        message = "Error" + ":" + " " + "Not it has captured the ip of the victim"
        return message
      else:
        try:
          self.varGeo["ip"] = data["query"]
          self.varGeo["isp"] = data["isp"]
          self.varGeo["city"] = data["city"]
          self.varGeo["country"] = data["country"]
          self.varGeo["latitude"] = data["lat"]
          self.varGeo["longitude"] = data["lon"]
          return self.varGeo
        except Exception:
          self.varGeo["ip"] = self.notFound
          self.varGeo["isp"] = self.notFound
          self.varGeo["city"] = self.notFound
          self.varGeo["country"] = self.notFound
          self.varGeo["latitude"] = self.notFound
          self.varGeo["longitude"] = self.notFound
          return self.varGeo
