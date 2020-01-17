from bs4 import BeautifulSoup
import requests
#from selenium  import webdriver
import playsound
from gtts import gTTS


URL="https://scores.sify.com/live-cricket-scores/Australia-in-India-3-ODI-Series-2020/INDIA_vs_AUSTRALIA_JAN17_2020.shtml"

#lenn=0
#flag=0
voiceno=0
prev='h'

def speak(text):
    global voiceno
    tts=gTTS(text=text,lang="en")
    filename="voice"+str(voiceno)+".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    voiceno=voiceno+1

def change_in_len(lenn,soup):
    len2=len(soup.find_all('div',class_="description"))
    if(lenn != len2):
        return len2-lenn
    return 0
print("")
#driver = webdriver.Chrome('C:\\Users\\Dell\\Downloads\\chromedriver')
#driver.get("https://scores.sify.com/live-cricket-scores/Basil-D'Oliveira-Trophy-2019-20/SOUTH-AFRICA_vs_ENGLAND_JAN03_JAN07_2020.shtml")
#headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def repeat():
    global URL
    #global lenn
    #global flag
    global prev
    source=requests.get(URL).text
    soup=BeautifulSoup(source,'lxml')

    #soup2=BeautifulSoup(soup.prettify(),'lxml')
    div=soup.find('div',class_="commentary-item")
    cmntry=div.find('div',class_='description').text
    #if lenn==0:
    #    lenn=len(soup.find_all('div',class_="description"))
    #price=soup.find(id='productTitle')
    #if flag==0:
    #    print(cmntry)
    #    print(lenn)
    #    flag=1

    if(cmntry!=prev):
        gottaPrintCommentary=False
        '''if(cmntry.find("FOUR")!=-1 or cmntry.find("SIX")!=-1 or cmntry.find("OUT")!=-1):'''
        if(cmntry.find("FOUR")!=-1):
            print("It's a FOUUUUURRRRRR!!!")
            gottaPrintCommentary=True
        elif(cmntry.find("SIX")!=-1):
            print("It's a SIIIXXXXXX!!!")
            gottaPrintCommentary=True
        elif(cmntry.find("OUT")!=-1):
            print("It's a Wicket!!!")
            gottaPrintCommentary=True
        if(gottaPrintCommentary):
            print(cmntry)
            speak(cmntry)
            print()
        prev=cmntry
    #newl=change_in_len(lenn,soup)
    #for i in range(newl):
    #    cmntry=div.find('div',class_='description')
    #    print(cmntry)

print("Press 'Ctrl+C' to stop")
while(1):
    repeat()