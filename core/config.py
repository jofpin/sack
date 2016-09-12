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

class Config:
    def __init__(self):
        self.nameFramework = "sack"
        self.versionFramework = "1.0"
        self.descriptionFramework = "Identify connection of sessions for social engineering attacks."
        self.authorName = "Jose Pino"
        self.authorNick = "Fraph"
        self.authorTwitter = "@jofpin"
        self.homepage = "https://spartug.com"
        self.dateFramework = "22-08-2016"
        self.collaborators = ""

url = None
urlAction = "https://facebook.com"

Fbp = {
   "url": "https://spartug.com",
   "urlAction": "https://facebook.com",
   "redirect": "redirect.html"
}