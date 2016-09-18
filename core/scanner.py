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

import socket
import sys

class scanner(object):
    def __init__(self):
        self.portList = [0, 21, 22, 23, 80, 8080, 3389]
        
    def scanIP(self, victim):
        clientIP = socket.gethostbyname(victim)
        listPorts = self.portList
        results = []
        for port in listPorts:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((clientIP, port))
            sys.stdout.flush()
            if result == 0:
                results.append(str(port))
        return ",".join(results)
