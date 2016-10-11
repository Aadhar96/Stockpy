import os
from urllib import urlopen as u
import pandas as pd
import warnings
from datetime import datetime
def daily(a,b,c,d,e,f,g):
    path=r'C:\StockData\Daily'
    if not os.path.exists(path):
        os.makedirs(path)
    x=c-1
    y=f-1
    url="http://real-chart.finance.yahoo.com/table.csv?s=%s&a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&g=d&ignore=.csv"%(a,x,b,d,y,e,g)
    csv=u(url).read()
    temp=open("%s\%s.csv"%(path,a),'wb+')
    temp.write(csv)
    temp.close()

def weekly(a,b,c,d,e,f,g):
    path=r'C:\StockData\Weekly'
    if not os.path.exists(path):
        os.makedirs(path)
    x=c-1
    y=f-1
    url="http://real-chart.finance.yahoo.com/table.csv?s=%s&a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&g=w&ignore=.csv"%(a,x,b,d,y,e,g)
    csv=u(url).read()
    temp=open("%s\%s.csv"%(path,a),'wb+')
    temp.write(csv)
    temp.close()    

def sec_based(a,b,c=3600):
        path=r'C:\StockData\Hourly'
        if not os.path.exists(path):
            os.makedirs(path)
	warnings.filterwarnings("ignore")
	url="https://www.google.com/finance/getprices?i=%d&p=%dd&f=d,o,h,l,v,c&df=cpct&q=%s"%(c,b,a)
	csv=u(url).read()
	temp=open('Stocktemp.csv','wb')
	temp.write(csv)
	temp.close()
	temp=open('Stocktemp.csv','r')
	lines=temp.readlines()
	temp.close()
	temp=open("Stocktemp.csv",'w')
	temp.write(lines[4][8:])
	temp.write(lines[7][1:])
	for i in lines[8:]:
		temp.write(i)
	temp.close()
	d1=pd.read_csv("Stocktemp.csv")
	os.remove('Stocktemp.csv')
	for i in range(1,d1.shape[0]):
		d1['DATE'][i]=d1['DATE'][i-1]+c
	for i in range(d1.shape[0]):
		d1["DATE"][i]=datetime.utcfromtimestamp(float(d1["DATE"][i])).strftime('%Y-%m-%d %H:%M:%S')
	d1.to_csv("%s\%s.csv"%(path,a),index=False)

def bse():
        import time
        import zipfile
        path=r'C:\StockData\StockList'
        if not os.path.exists(path):
            os.makedirs(path)
        x=datetime.fromtimestamp(time.time())
        if(x.weekday()<2):
            if((x.day-4)<10):
                temp='0'+str(x.day-4)
            else:
                temp=str(x.day-4)
        else:    
            if((x.day-2)<10):
                temp='0'+str(x.day-2)
            else:
                temp=str(x.day-2)
        if((x.month<10)):
            temp+='0'
            temp+=str(x.month)
        else:
            temp+=str(x.month)
        temp+=str(x.year%1000)
        url="http://www.bseindia.com/download/BhavCopy/Equity/EQ%s_CSV.ZIP"%temp
        csv=u(url).read()
        temp1=open('temp.zip','wb')
        temp1.write(csv)
        temp1.close()
        temp1=zipfile.ZipFile("temp.zip")
        data=temp1.read("EQ%s.CSV"%temp)
        temp1.close()
        temp2=open('Stocktemp.csv','wb')
        temp2.write(data)
        temp2.close()
        df1=pd.read_csv('Stocktemp.csv',usecols=('SC_CODE','SC_NAME'))
        df1.to_csv(r"%s\BSElist.csv"%(path),index=False)
        os.remove('Stocktemp.csv')
        os.remove('temp.zip')

def nse():
        import time
        import zipfile
        import requests
        path=r'C:\StockData\StockList'
        if not os.path.exists(path):
            os.makedirs(path)
        x=datetime.fromtimestamp(time.time())
        s1=x.strftime("%B")[0:3].upper()
        if(x.weekday()<2):
            if((x.day-4)<10):
                temp='0'+str(x.day-4)
            else:
                temp=str(x.day-4)
        else:    
            if((x.day-2)<10):
                temp='0'+str(x.day-2)
            else:
                temp=str(x.day-2)
        temp=temp+s1+str(x.year)
        url="https://www.nseindia.com/content/historical/EQUITIES/%d/%s/cm%sbhav.csv.zip"%(x.year,s1,temp)
        c=requests.get(url)
        csv=c.content
        temp1=open('temp.zip','wb')
        temp1.write(csv)
        temp1.close()
        temp1=zipfile.ZipFile("temp.zip")
        data=temp1.read("cm%sbhav.csv"%temp)
        temp1.close()
        temp2=open('Stocktemp.csv','wb')
        temp2.write(data)
        temp2.close()
        df1=pd.read_csv('Stocktemp.csv',usecols=('SYMBOL','ISIN'))
        df1.to_csv(r"%s\NSElist.csv"%(path),index=False)
        os.remove('Stocktemp.csv')
        os.remove('temp.zip')
