from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import sys
import csv
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

def fetchJobData(link,fileNames,destFile,institutionName,counter):
    driver = webdriver.PhantomJS('C:/ADS/A1_HiringTrends/Support/phantomjs/phantomjs')
    driver.get(link)
    counterVal=counter

    time.sleep(10)
    htmlJobContent = driver.execute_script("return document.body.innerHTML;")
    soup = bs(htmlJobContent,'html.parser')
    divClass=soup.find('div',attrs={'class':'GWTCKEditor-Disabled','dir':'ltr'})
    headVal=divClass.text
    ulClass=soup.find_all('ul',attrs={'class':'WPFO WGGO','role':'presentation'})[2]
    try:
        location=str(ulClass)
        loc=location.find('<b>Location</b>')
        loc=location.find('</h1>',loc)+5
        loc2=location.find('<p',loc)
        location=location[loc:loc2]
        data=''
        for x in ulClass:
            data+=' '+x.text
        data=data.lower()
        driver.close()
        driver.quit()
        stop_words = set(stopwords.words("english"))
        data=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",data)
		# remove special characters and digits
        data=re.sub("(\\d|\\W)+"," ",data)
		##Convert to list from string
        data = data.split()
        #Lemmatisation
        stop_words = set(stopwords.words("english"))
        lem = WordNetLemmatizer()
        data = [lem.lemmatize(word,pos="v") for word in data if not word in stop_words]
        data = " ".join(data)
        id=1

        for fileN in fileNames:
            valToAppend=[counterVal,institutionName,link,headVal,location,id]
            with open(fileN, newline='') as myFile:
                reader = csv.reader(myFile)
                for row in reader:
                    count=0
                    valtosearch=str(row[1])
                    count = sum(1 for match in re.finditer(valtosearch.lower(), data.lower()))
                    valToAppend.append(str(count))
            with open(destFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(valToAppend)
                counterVal+=1
            id+=1
    except:
        with open('C:/ADS/A1_HiringTrends/Data/Generated/By Algorithms/Unresolved.csv', 'a') as unresolved:
            writer = csv.writer(unresolved)
            writer.writerow([link])
        driver.close()
        driver.quit()
    return counterVal

driver = webdriver.PhantomJS('C:/ADS/A1_HiringTrends/Support/phantomjs/phantomjs')
driver.get("https://mtb.wd5.myworkdayjobs.com/MTB")
# This will get the initial html - before javascript
# This will get the html after on-load javascript
time.sleep(10)
html2 = driver.execute_script("return document.body.innerHTML;")

soup = bs(html2,'html.parser')
totalcount=0
for i,tag in enumerate(soup.find_all('span',attrs={'class':'gwt-InlineLabel WF2N WG2N'})):
    totalcount=int(tag.text.replace("Results","").strip())
    break
print(totalcount)
count=0
totalcount+=50
while count<totalcount:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    count+=50
html2 = driver.execute_script("return document.body.innerHTML;")
driver.close()
soup = bs(html2,'html.parser')
driver.quit()

link=''
unsolved=[]
counter=1
for i,tag in enumerate(soup.find_all(['div','span'],attrs={'class':['gwt-Label WOTO WISO','gwt-InlineLabel WM-F WLYF']})):
    if(i%2==0):
        link=''
        if tag.has_attr('aria-label'):
            link=tag['aria-label']
        else:
            continue
    else:
        if(link==''):
            continue
        else:
            link='https://mtb.wd5.myworkdayjobs.com/en-US/MTB/job/'+tag.text.split('|')[0].strip().replace(' ','-').replace('.','').replace('&','').replace('(','').replace(')','').replace(',','').replace('/','').replace('\\','')+'/'+link.replace('- Bankruptcy','').replace(' ','-').replace('.','').replace('&','-').replace('(','-').replace(')','-').replace(',','-').replace('/','-').replace('\\','-')+'_'+tag.text.split('|')[1].strip()
            fileNames=['C:/ADS/A1_HiringTrends/Data/Generated/By Algorithms/Textrank_top100.csv','C:/ADS/A1_HiringTrends/Data/Generated/By Algorithms/TF-IDF_top100.csv','C:/ADS/A1_HiringTrends/Data/Generated/By Algorithms/WordCount_top100.csv']
            destFile='C:/ADS/A1_HiringTrends/Data/Generated/By Algorithms/M&T_Scraped.csv'
            instName='M&T Bank'
            try:
                print(link)
                counter=fetchJobData(link,fileNames,destFile,instName,counter)
            except:
                print(sys.exc_info()[0])
                try:
                    print(link+'-1')
                    counter=fetchJobData(link+'-1',fileNames,destFile,instName,counter)
                except:
                    unsolved.append(link)
                    with open('C:/ADS/A1_HiringTrends/Data/Generated/By Algorithms/Unresolved.csv', 'a') as unresolved:
                        writer = csv.writer(unresolved)
                        writer.writerow([link])
                    print('*'*50+'\nUnsolved:'+link+'\n'+'*'*50)
                    print(sys.exc_info()[0])
print('End')
