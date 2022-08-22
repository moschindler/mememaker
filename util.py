import PIL
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import requests
from math import sqrt
from io import BytesIO
from math import atan
from bar import *
import re
from whitebar import *
import struct
import glob
from datetime import datetime, timedelta
import calendar

##########
#random utility
def opp(s):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    for i in alpha:
        if not i in s:
            ans += i
    return ans

def all_links(arr1,arr2):
    ans = []
    for i in range(len(arr1)):
        l1 = arr1[i]
        l2 = arr2[i]
        ends = opp(l2)
        for j in ends:
            ans.append(l1+j)
    return ans
#########################################
#CLASSES

class rectangle:
    def __init__(self,p1,p2,p3,p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.c = tsums(p1,p2,p3,p4)
        self.c = (self.c[0]/4,self.c[1]/4)
        arr = [p1,p2,p3,p4]
        c = self.c
        #these are COORDINATES..so smaller y means higher
        for i in range(4):
            if(arr[i][1]<c[1]):
                if(arr[i][0]<c[0]):
                    arr[i],arr[0] = arr[0],arr[i]
        for i in range(1,4):
            if(arr[i][0]>c[0]):
                if(arr[i][1]<c[1]):
                    arr[i],arr[1] = arr[1],arr[i]
        for i in range(2,4):
            if(arr[i][0]>c[0]):
                if(arr[i][1]>c[1]):
                    arr[i],arr[2] = arr[2],arr[i]
        self.p1 = arr[0]
        self.p2 = arr[1]
        self.p3 = arr[2]
        self.p4 = arr[3]

        self.mpt = tsum(p1,p2)
        self.mpt = (self.mpt[0]/2,self.mpt[1]/2)
        v = (self.mpt[0]-self.c[0],self.mpt[1]-self.c[1])
        self.angle = atan(v[0]/v[1])
        #NEGATIVE means turn LEFT from vertical
        #POSITIVE means right ok?

    def area(self):
        p1 = self.p1
        p2 = self.p2
        p3 = self.p3
        p4 = self.p4
        x1,y1 = p1[0],p1[1]
        x2,y2 = p2[0],p2[1]
        x3,y3 = p3[0],p3[1]
        x4,y4 = p4[0],p4[1]
        return abs(1/2*(x1*y2+x2*y3+x3*y4+x4*y1-y1*x2-y2*x3-y3*x4-y4*x1))
    
    def w(self):
        return sqrt(pow(self.p1[0]-self.p2[0],2)+pow(self.p1[1]-self.p2[1],2))
    
    def h(self):
        return sqrt(pow(self.p1[0]-self.p4[0],2)+pow(self.p1[1]-self.p4[1],2))
    
    def d(self,a1,a2):
        return sqrt(pow((a1[0]-a2[0]),2)+pow(a1[1]-a2[1],2))
    
    

class transbar(bar):    #TRANSPARENT BAR: for when you want to write text ON an image.
    def __init__(self,w,mtr,boxcoords,centered=True):
        self.w = w
        self.ps,self.pt = 0,0
        self.r = rectangle(boxcoords[0],boxcoords[1],boxcoords[2],boxcoords[3]) #wanna be explicit
        super().__init__(self,w,mtr,boxcoords=boxcoords,centered=centered)
##########################################
#IMAGE MANIPULATION (WRITING, ETC)
def gs(fontname,fontsize,text):
    return ImageFont.truetype(fontname,fontsize).getsize(text)
def textonpic(picpath,font,color,size,loc,text,single=False):
    #font in <whatever>, color in color or color..
    #FONT SHOULD CONTAIN TTF ALREADY
    #loc in percentages (across, down)
    #actually, loc a decimal
    #size in % of max size
    #pic should already be a url
    #text is our friendly text array
    #how is my fantasy team so good
    #(0,0) is in the TOP LEFT of the image. As in, draw(0,0) text puts the top left of your letters starting there. so subtract height/2, subtract width/2
    font = "fonts/"+font
    fontname = font
    colors = {
        "black":"#000000","red":"#FF0000","green":"#00FF00","blue":"#0000FF",
        "white":"#FFFFFF","pink":"#FF00FF","yellow":"#FFFF00","cyan":"#00FFFF",
        "grey":"#666666","gray":"#666666","purple":"#BB00FF","orange":"#FF7700",
        "darkgray":"#414141","darkgrey":"#414141"
    }
    try:
        int(color[1:])
    except:
        color = colors.get(color)
    color = color[1:]
    try:
        color = struct.unpack('BBB',bytes.fromhex(color))
    except:
        color = (61,61,61)
    
    ##########################
    #width and font size and shit
    img = Image.open(picpath)
    im = img.load()
    w,h = img.size
    start = (w*int(loc[0])/100,h*int(loc[1])/100)
    fz = float(size)*w/20*2
    fz = int(fz)
    hg = 19/16*fz   #decided this name a while ago. bring it.
    font = ImageFont.truetype(font,int(fz))
    draw = ImageDraw.Draw(img)
    ##########################
    #finding the height of the text and the width of each row
    if single:
        nrows = 1
    else:
        nrows = len(text)
    rowwidths = [gs(fontname,fz,i)[0] for i in text]
    textheight = fz+40/25*fz*(nrows-1)  #shrug
    truestarts = []
    start = list(start)
    start[1] = start[1]+fz/2    #for some reason it's off by >>that much<<
    print(start)
    print((w,h))
    if(start[1]-textheight/2<0):
        start[1] = int(textheight/2)+2
    if(start[1]+textheight/2>h):
        start[1] = h-int(textheight/2)-2
    if(start[0]-max(rowwidths)/2<0):
        start[0] = max(rowwidths)/2+2
    if(start[0]+max(rowwidths)/2>w):
        start[0] = w-max(rowwidths)/2-2     #fixing text flowing off the image
    start = tuple(start)
    for i in range(nrows):
        inx = i-nrows/2
        truestarts.append((start[0]-rowwidths[i]/2,start[1]+inx*hg-fz/2))   #here's hoping
        #PRAYER emojis
    #pic text loc font color size
    if single:
        for i in range(nrows):
            draw.text(truestarts[i],text,color,font=font)
    else:
        for i in range(nrows):
            draw.text(truestarts[i],text[i],color,font=font)
    img.save(picpath)
    #img.show()
    #pic text loc font color size


def ith(f,i):
    if(type(f) is list):
        return f[i]
    else:
        return f

def ttf(s):
    if(s[-4:]==".ttf"):
        return s
    else:
        s += ".ttf"
        return s

def alltextonpic(imgurl,font, color, size, locar, textar):
    response = requests.get(imgurl)
    img = Image.open(BytesIO(response.content))
    img.save("meme.jpg")
    #picurl, font, color, size, loc, text
    #isinstance,list
    #locar = ast.literal_eval(locar)
    #textar = ast.literal_eval(textar)
    for i in range(len(locar)): 
        textonpic("meme.jpg",ttf(ith(font,i)),ith(color,i),ith(size,i),locar[i],textar[i])

def alltextonscreening(font,color,size,locar,textar):
    #picurl, font, color, size, loc, text
    #isinstance,list
    #locar = ast.literal_eval(locar)
    #textar = ast.literal_eval(textar)
    for i in range(len(locar)): 
        textonpic("screening.png",ttf(ith(font,i)),ith(color,i),ith(size,i),locar[i],textar[i])

def gridlines(imgurl):
    if(imgurl[0] =="<"):
        imgurl = imgurl[1:-1]
    response = requests.get(imgurl)
    img = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(img)
    w,h = img.width,img.height
    font = ImageFont.truetype("fonts/helvetica.ttf",int(w/10))    #1
    font2 = ImageFont.truetype("fonts/helvetica.ttf",int(w/20))   #0.5
    font3 = ImageFont.truetype("fonts/helvetica.ttf",int(w/40))   #0.25
    font4 = ImageFont.truetype("fonts/helvetica.ttf",int(w/100))  #0.1
    font5 = ImageFont.truetype("fonts/helvetica.ttf",int(0.75*w/10))   #0.75
    font6 = ImageFont.truetype("fonts/helvetica.ttf",int(0.75*w/10))   #0.6
    draw.text((0,0),"font size 1.00",fill="black",font=font)
    draw.text((0,250),"font size 0.50",fill="black",font=font2)
    draw.text((0,325),"font size 0.25",fill="black",font=font3)
    draw.text((0,365.5),"font size 0.10",fill="black",font=font4)
    draw.text((0,150),"font size 0.75",fill="black",font=font5)
    for i in range(1,6):
        draw.rectangle((w*i/5,0)+(w*i/5+7,h),(255,0,0))
        draw.rectangle((0,h*i/5)+(w,h*i/5+7),(255,0,0))
        draw.rectangle((w*i/5-w/10,0)+(w*i/5+2-w/10,h),(255,0,0))
        draw.rectangle((0,h*i/5-h/10)+(w,h*i/5+2-h/10),(255,0,0))
    img.save("gridlines.jpg")
    #img.show()
#gridlines("https://i.pinimg.com/originals/6e/1e/28/6e1e287da53614647b9b33cc480c7a26.jpg")
'''
textars = '[["when","you"],["ar","e","sex"]]'
locar = '[(50,30),(10,10)]'

'''
#textonpic("meme2.jpg",["hygh","hygh","huhghghgh","hsdhagdasg","asdhglasdlghasdg"],(0.5,0.3),"helvetica.ttf","black",1)

def screening(name,sid):
    now = datetime.now()-timedelta(hours=6)
    cday = now.day
    cmon = calendar.month_name[now.month]
    cyear = now.year
    cweek = calendar.day_name[now.weekday()]
    tom = datetime.today()+timedelta(days=1)-timedelta(hours=6)
    tday = tom.day
    tmon = calendar.month_name[tom.month]
    tyear = tom.year
    tweek = calendar.day_name[tom.weekday()]
    
    toptext = "{}, {} {}, {}".format(cweek,cmon,cday,cyear)
    bottomtext = "{}, {} {}, {}".format(tweek,tmon,tday,tyear)
    #12.5,81.9
    font = "sourcesans"
    color = "darkgray"
    locar = [(52,12),(52,18),(52,62.5),(52,67.5),(52,81),(52,87)]
    size = 0.5
    textar = [[toptext],["07:30 AM"],[name],[sid],[bottomtext],["07:30 AM"]]
    #textar = [[{}],[{}]].format(toptext,bottomtext)
    alltextonscreening(font,color,size,locar,textar)
    #textonpic("/home/ec2-user/walterbot1/screening.png","sourcesans.ttf","black",0.45,(29,11),toptext,single=True)
    #textonpic("/home/ec2-user/walterbot1/screening.png","sourcesans-light.ttf","black",0.5,(29,80),bottomtext,single=True)

#################################################
#DISCORD, UH, BOT, STUFF
def isFloat(s):
    try:
        float(s)
        return True
    except:
        return False
    return False

def concat_v(im1,im2):  #put images on top of one another. like, physically, not sexually. what?
    dst = Image.new('RGB',(im1.width,im1.height + im2.height))
    dst.paste(im1,(0,0))
    dst.paste(im2,(0,im1.height))
    return dst

def addformatpic(f,u):     #format name, url
    if(re.search("<",u)):
        u = u[1:-1]
    with open('picformats.txt','r') as reader:
        for line in reader.readlines():
            if(line==f):
                return "Exists_Already"
            if(line==u):
                return l2   #gets the format name if it already exists
            l2 = line
    z = open("picformats.txt","a")
    z.write(f)
    z.write("\n")
    z.write(u)
    z.write("\n")
    z.close()
    return "Added_Fine"

def addformatvid(f,u):      #format name, url
    if(re.search("youtube",u)):
        u = u.split("?v=")[1][:11]
    with open('vidformats.txt','r') as reader:
        for line in reader.readlines():
            if(line==f):
                return "Exists_Already"
            if(line==u):
                return l2   #gets the format name if it already exists
            l2 = line
    z = open("vidformats.txt","a")
    z.write("\n")
    z.write(f)
    z.write("\n")
    z.write(u)
    z.close()
    return "Added_Fine"

def makememevid(i1,textar):
    pass
    #see shell script: getter.sh, which does the same thing and sends it to vid.mp4

def makememebpic(i1,textar):
    url = "&_&._"
    if(isUrl(i1)):
        url = i1
    elif(i1 == "savedMeme"):
        url = "savedMeme"
        pass
    else:
        d = ""
        with open('picformats.txt','r') as reader:
            for line in reader.readlines():
                if(d == "done"):
                    url = line.strip()
                    d = "overdone"
                if(line.strip()==i1):
                    d = "done"      #for some reason reading lines is hard ?
    if(url=="&_&._"):    
        return "bruh"
    if(re.search("<",url)):
        url = url[1:-1]
    if(url == "savedMeme"):
        img = Image.open("meme.jpg")
    else:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
    s = whitebar(img.width,textar)
    s2 = concat_v(img,s.img)
    return s2

def makememepic(i1,textar):
    url = "&_&._"
    if(isUrl(i1)):
        url = i1
    elif(i1 == "savedMeme"):
        url = "savedMeme"
        pass
    else:
        d = ""
        with open('picformats.txt','r') as reader:
            for line in reader.readlines():
                if(d == "done"):
                    url = line.strip()
                    d = "overdone"
                if(line.strip()==i1):
                    d = "done"      #for some reason reading lines is hard ?
    if(url=="&_&._"): 
        return "bruh"
    if(re.search("<",url)):
        url = url[1:-1]
    if(url=="savedMeme"):
        img = Image.open("meme.jpg")
    else:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
    s = whitebar(img.width,textar)
    s2 = concat_v(s.img,img)
    return s2

def getvidofformat(fo,fn,asList=False):   #format, file name
    #if asList: returns [format name,True] if in formats, [yid,False] if not.
    #if not asList: returns format name if in formats, yid if not.
    f = open(fn,"r")
    
    while True:
        line1 = f.readline()
        if(line1 == ""):
            line1 = f.readline()
        line2 = f.readline()
        if(line2 == ""):
            line2 = f.readline()
        if(line1.strip()==fo):
            if asList:
                return [line2.strip(),True]
            return line2.strip()
        if(line2.strip()==fo):
            if asList:
                return [line2.strip(),True]
            return line2.strip()
        if not line2:
            break
    if asList:
        return [fo,False]
    return fo


def isUrl(s):   #only urls contain . and /, right?!
    if(re.search("\.",s) and re.search("\/",s)):
        return True
    return False

def isYoutube(s):   #whatever
    if(len(s)==11):
        return True
    return False

def isinty(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def isin(s,f):  #checks if string is a line in a file
    with open(f,'r') as reader:
        for line in reader.readlines():
            if(line.strip()==s):
                return True
    return False

def delblank(fn):
    with open(fn,'r+') as file:
        for line in file:
            if not line.isspace():
                file.write(line)

def getrandomimgurmeme(s):
    infl = 0
    bob = True
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    while bob:
        infl += 1
        if(infl>50):
            print("ran out of time")
            break
        try: 
            ranlink = ""
            for i in range(5):
                rn = random.randint(0,61)
                ranlink += alphabet[rn:rn+1]
            print(ranlink)
            url = "https://i.imgur.com/{}.jpg".format(ranlink)
            response = requests.get("https://i.imgur.com/{}.jpg".format(ranlink))
            img = Image.open(BytesIO(response.content)).convert("RGB")
            if(img.size[0]==161 and img.size[1]==81):
                pass
                print("fuck")
            else:
                bob = False
                s = cutatmid(s)
                memesetup(url,s[0],s[1])
            #img.save("meme.jpg")
            #s = cutatmid(s)
            #print((s[0],s[1]))
            #memepathsetup("meme.jpg",s[0],s[1])
            #print("I GOT HERE AHAHAHAHA")
        except:
            pass
    #s = cutatmid(s)
    #memepathsetup("meme.jpg",s[0],s[1])

def getrandomimgurlink():
    infl = 0
    bob = True
    ranlink = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    while bob:
        if(infl>200):
            print("ran out of time")
            break
        try: 
            ranlink = ""
            for i in range(5):
                rn = random.randint(0,61)
                ranlink += alphabet[rn:rn+1]
            response = requests.get("https://i.imgur.com/{}.jpg".format(ranlink))
            img = Image.open(BytesIO(response.content))
            if(img.size[0]==161 and img.size[1]==81):
                raise ValueError("fuck2")
            bob = False
        except:
            pass
        infl += 1
    return "https://i.imgur.com/{}.jpg".format(ranlink)



############################
#DISCORD COMMAND PARSING

def contigbb(ar):
    ans1 = 0
    ans2 = -1
    for i in range(len(ar)):
        if(re.search("\[\[",ar[i])):
            ans1 = i
        if(re.search("\]\]",ar[i])):
            ans2 = i
    return [ans1,ans2]

def contigb(ar):
    ans1 = 0
    ans2 = -1
    for i in range(len(ar)):
        if(re.search("\[",ar[i])):
            ans1 = i
        if(re.search("\]",ar[i])):
            ans2 = i
    return [ans1,ans2]

def concat(ar):     #jams together all the elements of an array
    ans = ""
    for i in ar:
        ans += i
    return ans

def concats(ar):    #with spaces this time
    ans = ""
    for i in ar:
        ans += i
        ans += " "
    return ans.strip()

#picurl, font, color, size, loc, text
#DISTINGUISHING: isUrl, ar of string, also string...fuck., ar of tuple, DONE
def parseOnPicCommand(s):
    #fonts = ["helvetica"]
    fonts = glob.glob("fonts/*.ttf")
    fonts = [i.split("/")[-1] for i in fonts]
    if not 'helvetica' in fonts:
        fonts = [i.split("\\")[-1] for i in fonts]
    fonts = [i.split(".")[0] for i in fonts]
    #fonts = ["helvetica"]
    #return fonts
    print(fonts)
    
    print("HIIIIIIIIIIIIIIII")
    validfonts = ""
    for i in fonts:
        validfonts += i
        validfonts += ", "
    validfonts = validfonts[:-2]

    s = s.split(" ")
    s = s[2:]   #'cause ?m and pic
    tarloc = contigbb(s)
    textar = s[tarloc[0]:tarloc[1]+1]
    textar = ast.literal_eval(concats(textar))
    s = s[0:tarloc[0]]+s[tarloc[1]+1:]   #TEXTAR RETRIEVED
    url = ""
    for i in range(len(s)):
        if(isUrl(s[i])):
            url = s[i]
            s = s[:i]+s[i+1:]           #URL RETRIEVED
            break
    if(url[0]=="<"):
        url = url[1:-1]
    n = len(textar)
    tarloc = contigb(s)
    a1 = s[tarloc[0]:tarloc[1]+1]
    a1 = ast.literal_eval(concat(a1))
    s = s[0:tarloc[0]]+s[tarloc[1]+1:]

    tarloc = contigb(s)
    a2 = s[tarloc[0]:tarloc[1]+1]
    if(not a2 == []):
        a2 = ast.literal_eval(concat(a2))
    s = s[0:tarloc[0]]+s[tarloc[1]+1:]
    tarloc = contigb(s)
    a3 = s[tarloc[0]:tarloc[1]+1]
    if(not a3 == []):
        a3 = ast.literal_eval(concat(a3))
    s = s[0:tarloc[0]]+s[tarloc[1]+1:]
    tarloc = contigb(s)
    
    a4 = s[tarloc[0]:tarloc[1]+1]
    if(not a4 == []):
        a4 = ast.literal_eval(concat(a4))
    s = s[0:tarloc[0]]+s[tarloc[1]+1:]

    if(a2==[]): #all that should be left is <crap>
        a2 = [s[0]]*n
        a3 = [s[1]]*n
        a4 = [s[2]]*n
    if(a3==[]):
        a3 = [s[0]]*n
        a4 = [s[1]]*n
    if(a4==[]):
        a4 = [s[0]]*n
    #a1,a2,a3,a4 are: locar, fontar, colorar, sizear in some order
    locar,sizear,fontar,colorar = "","","",""
    for i in [a1,a2,a3,a4]:
        if(type(i[0]) is tuple):
            locar = i
        elif(isFloat(i[0])):
            sizear = i
        elif(i[0] in fonts):
            fontar = i
        else:
            colorar = i
    if(locar==""):
        return "location tuple array. It should be: An array of coordinates."
    if(sizear==""):
        return "font sizes. It should either be: A single number or an array of numbers."
    if(fontar==""):
        print("hi")
        return "fonts. It should either be: A single font or an array of fonts. Valid fonts are: "+validfonts
    if(colorar==""):
        return "colors. It should either be: A single color or an array of colors. Valid color format is either #XXXXX (0-F) or the name of a color."
    return (url,fontar,colorar,sizear,locar,textar)

#picurl, font, color, size, loc, text
#DISTINGUISHING: isUrl, ar of string, also string...fuck., ar of tuple, DONE
'''
intro = "?m picm"
url = "https://i.imgflip.com/ual56.jpg"
font = "helvetica"
color = "black"
size = "1"
loc = "[(30,50),(50,30)]"
text = '[["when", "you"],["sex"]]'
s = "{} {} {} {} {} {} {}".format(intro,url,font,color,size,loc,text)
print(parseOnPicCommand(s))
alltextonpic(*parseOnPicCommand(s))
'''


def parseVidCommand(s):
    #?meme video id start end text
    q = s.split(" ")
    ss = q[0]   #so we don't forget this when calculating l
    q = q[1:]
    if(len(q)<4):
        return "badlength"
    if(not (q[0]=="vid" or q[0]=="video")):
        if(q[0]=="bpic" or q[0]=="bpicture"):
            return "bpic"
        return "pic"
    else:
        idd = q[1]
        if(re.search("youtube",idd)):
            idd = idd.split("?v=")[1][:11]
        if(not (isin(idd,"vidformats.txt") or len(idd)==11)):
            return "badformat"
        
        if(not isinty(q[2])):
            return "bad"
        if(not isinty(q[3])):
            return "bad"
        l = len(q[0]+q[1]+q[2]+q[3])+4+len(ss)+1
        try:
            q4 = ast.literal_eval(s[l:])
            if(not isinstance(q4,list)):
                return "badtext"
        except:
            return "badtext"
        return [getvidofformat(idd,"vidformats.txt"),q[2],q[3],s[l:]]

def parsebvidCommand(s):
    #?meme video id start end text
    q = s.split(" ")
    ss = q[0]   #so we don't forget this when calculating l
    q = q[1:]
    if(len(q)<4):
        return "badlength"
    if(not (q[0]=="bvid" or q[0]=="bvideo")):
        return "pic"
    else:
        idd = q[1]
        if(re.search("youtube",idd)):
            idd = idd.split("?v=")[1][:11]
        if(not (isin(idd,"vidformats.txt") or len(idd)==11)):
            return "badformat"
        
        if(not isinty(q[2])):
            return "bad"
        if(not isinty(q[3])):
            return "bad"
        l = len(q[0]+q[1]+q[2]+q[3])+4+len(ss)+1
        try:
            q4 = ast.literal_eval(s[l:])
            print(q4)
            print("ASKFHLASKGHKLSHLGLASKHGLKSDAHGDLKSDJGKLSDJGLKSDJGDLSKGJS")
            if(not isinstance(q4,list)):
                return "badtext"
        except:
            return "badtext"
        return [getvidofformat(idd,"vidformats.txt"),q[2],q[3],s[l:]]

def allformats(fn):
    ef = []
    u = []
    f = open(fn,"r")
    while True:
        line1 = f.readline().strip()
        if(line1==""):
            line1 = f.readline().strip()
        line2 = f.readline().strip()
        if(line2==""):
            line2 = f.readline().strip()
        ef.append(line1)
        u.append("<"+line2+">")
        if not line2:
            break
    return [ef,u]

def allformats2(fn):
    ef = []
    u = []
    f = open(fn,"r")
    while True:
        line1 = f.readline().strip()
        if(line1==""):
            line1 = f.readline().strip()
        line2 = f.readline().strip()
        if(line2==""):
            line2 = f.readline().strip()
        ef.append(line1)
        u.append(line2)
        if not line2:
            break
    ans = []
    for i in range(len(ef)):
        try:
            ui = ast.literal_eval(u[i])
            ans.append((ef[i],"<"+ui[0]+">",len(ui[-1])))
        except:
            pass
    return str(ans)


def parsePicCommand(s):
    #?meme pic url text
    q = s.split(" ")
    ss = q[0]   #so we don't forget this when calculating l
    q = s.split(" ")[1:]
    if(len(q)<2):
        return "badlength"
    elif(q[0]=="vid" or q[0]=="video"):
        return "vid"
    elif(q[0]=="bpic" or q[0]=="bpicture"):
        return "bpic"
    elif(q[0]=="bvid" or q[0]=="bvideo"):
        return "bvid"
    elif(not (q[0]=="pic" or q[0]=="picture")):
        return "asdflasdfsadfsfasdf"
    else:
        idd = q[1]
        if(not (isin(idd,"picformats.txt") or isUrl(idd) or (idd == "savedMeme"))):
            return "badformat"
        l = len(q[0])+len(q[1])+3+len(ss)
        try:
            print(s[l:])
            q4 = ast.literal_eval(s[l:])
            if(not isinstance(q4,list)):
                return "badtext"
        except:
            return "badtext"
        if(not isUrl(idd)):
            idd = getvidofformat(idd,"picformats.txt")
        return [idd,ast.literal_eval(s[l:])]

def parsebpicCommand(s):
    #?meme pic url text
    q = s.split(" ")
    ss = q[0]   #so we don't forget this when calculating l
    q = s.split(" ")[1:]
    if(len(q)<2):
        return "badlength"
    if(not (q[0]=="bpic" or q[0]=="bpicture")):
        return "vid"
    else:
        idd = q[1]
        if(not (isin(idd,"picformats.txt") or isUrl(idd) or (idd == "savedMeme"))):
            return "badformat"
        l = len(q[0])+len(q[1])+3+len(ss)
        try:
            print(s[l:])
            q4 = ast.literal_eval(s[l:])
            if(not isinstance(q4,list)):
                return "badtext"
        except:
            return "badtext"
        if(not isUrl(idd)):
            idd = getvidofformat(idd,"picformats.txt")
        return [idd,ast.literal_eval(s[l:])]
        
def cutatmid(s):
    n = len(s)
    n = int(n/2)
    z = -1
    z2 = -1
    for i in range(n,-1,-1):
        if(s[i:i+1]==" "):
            z = i
            break
    for i in range(n,2*n+2):
        if(s[i:i+1]==" "):
            z2 = i
            break
    cut = n
    if(abs(z-n)<abs(z2-n)):
        cut = z
    else:
        cut = z2
    return ([s[0:cut]],[s[cut+1:len(s)]])



if __name__ == "__main__":
    #print(isin("cereal","picformats.txt"))
    #s = "?meme video rick 15 30 '[\"never am\",\"gonna\"]'"
    #print(parseVidCommand(s))
    #s2 = "?meme pic cereal '[\"never am\",\"gonna\"]'"
    #print(parsePicCommand(s2))
    '''
    print(isFloat("6"))
    print(isFloat('6.5'))
    img = Image.open("meme.jpg")
    font = ImageFont.truetype("fonts/Helvetica.ttf", 20)
    draw = ImageDraw.Draw(img)

    #...sound ok?

    draw.text((0,0), "blah blah blah", (128,128,128))
    img.show()
    '''
    screening("Moses Schindler","schindler")
    #print(getrandomimgurlink())
    pass
