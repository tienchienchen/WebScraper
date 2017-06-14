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
# Html compressed file location.  4GB.
# https://rentpath.getstat.com/bulk_reports/download_report/863?key=f248cd1e1f75d72c7134c03242a76e5957a7342f
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


#==============================================================================
# def isBlank (myString):
#     if myString and myString.strip():
#         #myString is not None AND myString is not empty or blank
#         return ''
#     #myString is None OR myString is empty or blank
#     return myString
# 
#==============================================================================


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
    if idx >= 0:
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
            print "Google Review Count:"+GooCnt
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
        sql ='insert into dbo.scraperFiletest (idx,filename,propertyname,googleReviewCount, googleReviewRating) Values ('+str(idx)+',\''+filename+'\',\''+propertyName.encode("utf-8").replace("'","''")+'\',\''+GooCnt.encode("utf-8").replace("'","''")+'\',\''+GooRate.encode("utf-8").replace("'","''")+'\');'
        print 'insert into dbo.scraperFiletest (idx,filename,propertyname,googleReviewCount, googleReviewRating) Values ('+str(idx)+',\''+filename+'\',\''+propertyName.encode("utf-8").replace("'","''")+'\',\''+GooCnt.encode("utf-8").replace("'","''")+'\',\''+GooRate.encode("utf-8").replace("'","''")+'\');'
        print sql
        session.execute(sql)
        con.commit()
        
        print '\n'
        #1st reviews
        lists= soup.body.find_all('span', attrs={'class':'_G2n _H2n'})
        reviews=soup.body.find_all('span', attrs={'class':'_G2n _N2n'})
        reviewcnt=soup.body.find_all('span', attrs={'class':'_G2n _d3n'})
        #print lists
        #print reviews
        #print reviewcnt
        #print '\n'
        name0=None
        value0=None
        review0=None
        try:
            name0= lists[0].contents[0].replace("'","''")
            print name0
        except:pass
            
        try:
            value0= reviews[0].contents[0].replace("'","''")
            print value0
        except:pass
        
        try:
            review0= reviewcnt[0].contents[0].replace("'","''")
            print review0
        except:pass
    
        if name0<> None:
                sql ='insert into dbo.scraperRighttest(idx,sitename,rating,ReviewCount) values ('+str(idx)+',\''+name0.encode("utf-8")+'\',\''+value0.encode("utf-8").replace("'","''")+'\',\''+review0.encode("utf-8").replace("'","''")+'\');'
                print sql
                session.execute(sql)
                con.commit()
    
        ##########################
        name1=None
        value1=None
        review1=None    
        try:
            name1= lists[1].contents[0].replace("'","''")
            print name1
        except:pass
            
        try:
            value1= reviews[1].contents[0].replace("'","''")
            print value1
        except:pass
        
        try:
            review1= reviewcnt[1].contents[0].replace("'","''")
            print review1
        except:pass
    
        if name1<> None:
                sql ='insert into dbo.scraperRighttest(idx,sitename,rating,ReviewCount) values ('+str(idx)+',\''+name1.encode("utf-8")+'\',\''+value1.encode("utf-8").replace("'","''")+'\',\''+review1.encode("utf-8").replace("'","''")+'\');'
                print sql
                session.execute(sql)
                con.commit()
    
        #########################
        name2=None
        value2=None
        review2=None        
        try:
            name2= lists[2].contents[0].replace("'","''")
            print name2
        except:pass
            
        try:
            value2= reviews[2].contents[0].replace("'","''")
            print value2
        except:pass
        
        try:
            review2= reviewcnt[2].contents[0].replace("'","''")
            print review2
        except:pass
    
        if name2<> None:
                sql ='insert into dbo.scraperRighttest(idx,sitename,rating,ReviewCount) values ('+str(idx)+',\''+name2.encode("utf-8")+'\',\''+value2.encode("utf-8").replace("'","''")+'\',\''+review2.encode("utf-8").replace("'","''")+'\');'
                print sql
                session.execute(sql)
                con.commit()
    
        #########################
        
        z=0
        srps = soup.body.find_all('div', attrs={'class':'rc'})
        for srp in srps:
            n = len(srp)
            #print type(srp)
            #print srp
            for i in range(0,n):
                #print type(srp.contents[i])
                #print i
                #print srp.contents[i]
                header = ''
                navigation = ''
                rating = None
                if i == 0:
                    try:
                        v=''
                        header=''
                        v = srp.contents[i].find('a').contents[0].encode("utf-8").replace("'","''")
                        #print 'V is :'+ v
                        header  = v
                    except: 
                        pass
                if i == 1:
                    try:
                        navigation = srp.contents[i].find('cite', attrs={'class':'_Rm'}).contents[0].replace("'","''")
                    except:
                        pass
                if i == 1:
                    try:
                        #print "rating\n"
                        #print type(srp)
                        mysrps = srp.contents[i].find_all('div', attrs={'class':'slp f'})
                        #print mysrps[0]
                        for Rsrp in mysrps:
                            #print  Rsrp
                            #print "End Outer Loop"
                            try:
                                Rsrp.contents[0].extract().sibiling
                                rating = Rsrp.contents[0].replace("'","''")
                                hasrating = True
                                #srpReview = Rsrp.contents[0]
                            except:
                                hasrating = False
                    #try:
                    #    print srp.contents[i].find('cite', attrs={'class':'_Rm'}).contents[0]
                    except:
                        pass
                if rating <> None:
        #            print header
                    #print navigation.encode('utf-8')
                    #print rating.encode('utf-8')
                    #print 'insert into dbo.scraperLeft(idx,LinkLable,ReviewText) values ('+str(idx)+',\''+navigation.encode('utf-8')+'\',\''+rating.encode('utf-8')+'\');'
                    #sql ='insert into dbo.scraperLeft(idx,LinkLable,ReviewText) values ('+str(idx)+',\''+navigation+'\',\''+rating+'\');'
                    sql = 'insert into dbo.scraperLefttest(idx,header,LinkLable,ReviewText) values ('+str(idx)+',\''+v+'\',\''+navigation.encode('utf-8')+'\',\''+rating.encode('utf-8')+'\');'
                    print sql
                    session.execute(sql)
                    con.commit()                
                    print '\n'
            #z= z+1
            #if z == 10:
            #    break
        #idx = idx +1
        
    idx = idx +1
    #if idx == 10:
    #    break
con.close()
#except:
#    print 'Error: Occured' + filename
#    con.close()        


