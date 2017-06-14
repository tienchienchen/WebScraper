# -*- coding: utf-8 -*-
#"""
#Created on Sat Jun 10 17:51:37 2017
#
#@author: rchen
#"""
## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#Web scraping using beautifulsoup
#"""
#
#
#import sqlalchemy as al
#import pandas as pd
#import pyodbc as db
#import pandasql as psql
#import matplotlib as plt
#import numpy as np
import os
import pymssql
from bs4 import BeautifulSoup
import urllib



#try:
os.chdir(r"C:\Users\rchen\Downloads\SERP\apartmentguideSERParchive20170608")
#for filename in os.listdir("C:\User\rchen/Downloads/SERP/www.apartmentguide.com-HTML-SERP-archive-2017-06-08//*"):
#cnn = db.connect('DSN=warehouse;DATABASE=readerOwnThis;UID=reader;PWD=reader')
# Set up database connection
#cnn = db.connect('DRIVER={SQL Server};SERVER=warehouse;DATABASE=readerOwnsThis;UID=reader;PWD=reader')
con = pymssql.connect(host='warehouse',user='reader',password='reader',database='readerOwnsThis')
session = con.cursor()

idx = 0
for filename in os.listdir(r"C:\Users\rchen\Downloads\SERP\apartmentguideSERParchive20170608"):
    print idx
    if idx >= 11146:
        print '##################################################################################################'
        propertyName = ''
        Goocnt= ''
        GooRate= ''
    
        print filename
        filename=filename.replace(' ','%20')
        #print filename
        r = urllib.urlopen(r"file:///C:/Users/rchen/Downloads/SERP/apartmentguideSERParchive20170608/"+filename).read()
        soup = BeautifulSoup(r)
        print '##################################################################################################'
        #`name
        try:
            propertyName=soup.body.find('div', attrs={'data-dtype':'d3bn'}).find('span').get_text()
            print "PropertyName:"+propertyName
        except:
            propertyName= ''
        #'google
    
        try:
            #GooCnt= soup.body.find('span', attrs={'class':'fl r-i9o0Pef_x_xg'}).get_text()
            GooCnt= soup.body.find('div', attrs={'class':'_A8k'}).find_all('span')[4].get_text()
            print GooCnt
            sql = 'update dbo.scraperFile set googleReviewCount =\''+GooCnt.encode("utf-8").replace("'","''")+'\' where idx='+str(idx)+';'
            print sql
            session.execute(sql)
            con.commit()
        except:
            GooCnt= ''
        
        try:    
            GooRate= soup.body.find('div', attrs={'class':'_A8k'}).find('span').get_text()
            print "Google Rating:"+GooRate
        except:
            GooRate= ''
    
    
        #sql ='insert into dbo.scraperFile (idx,filename,propertyname,googleReviewCount, googleReviewRating) Values ('+str(idx)+',\''+filename+'\',\''+propertyName+'\',\''+GooCnt+'\',\''+GooRate+'\');'
        #
        #session.execute('insert into dbo.scraperFile (idx,filename,propertyname,googleReviewCount, googleReviewRating) Values ('+str(idx)+',\''+filename+'\',\''+propertyName+'\');') 
#        sql ='insert into dbo.scraperFile (idx,filename,propertyname,googleReviewCount, googleReviewRating) Values ('+str(idx)+',\''+filename+'\',\''+propertyName.encode("utf-8").replace("'","''")+'\',\''+GooCnt.encode("utf-8").replace("'","''")+'\',\''+GooRate.encode("utf-8").replace("'","''")+'\');'
        #print 'insert into dbo.scraperFile (idx,filename,propertyname,googleReviewCount, googleReviewRating) Values ('+str(idx)+',\''+filename+'\',\''+propertyName.encode("utf-8").replace("'","''")+'\',\''+GooCnt.encode("utf-8").replace("'","''")+'\',\''+GooRate.encode("utf-8").replace("'","''")+'\');'
#        print sql
        #session.execute(sql)
        #con.commit()
        
        print '\n'
        #'1st reviews
    idx = idx +1
    if idx == 12762:
        break
#con.close()
#except:
#    print 'Error: Occured' + filename
#    con.close()        