#NOTE TO SELF: do text parsing in sexbot
import PIL
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
import math
from getter import *

def gs(fontname,fontsize,text):
    return ImageFont.truetype(fontname,fontsize).getsize(text)
class impact:

    def __init__(self,imgpaths,textar,top="top",fontname="impact",isvid=False):
        self.text = textar
        self.text = [i.upper() for i in self.text]
        if isvid:
            self.img = Image.open(imgpaths).convert("RGBA")
        else:
            self.img = Image.open(imgpaths).convert("RGB")
        self.font = "fonts/{}.ttf".format(fontname)
        self.w,self.h = self.img.width,self.img.height
        print((self.w,self.h))
        self.ps,self.pt = self.w/40,self.h/100          #someone please tell me what any of this means!
        
        self.fz = min([self.maxfz(i) for i in self.text])
        
        if(self.fz>int(self.w/7)):
            self.fz = int(self.w/7)
        self.hg = 17/16*self.fz
        self.war = [gs(self.font,self.fz,i)[0] for i in self.text] #array of widths of texts
        if(top=="top"):
            self.topwritelines()
        else:
            self.bottomwritelines()
    
    def out(self,fn):
        self.img.save(fn)
    
    def topwritelines(self):
        mid = self.w/2
        start = (mid-self.war[0]/2,self.pt)
        
        for i in range(len(self.war)):
            start = (mid-self.war[i]/2,start[1])
            self.imgtextborder(self.text[i],self.fz,start)
            start = (0,start[1]+self.hg)
    
    def bottomwritelines(self):
        mid = self.w/2
        totalheight = 2.5*self.pt+self.hg*(len(self.text)-1)+1.1*self.fz
        start = (mid-self.war[0]/2,self.h-totalheight)
        
        for i in range(len(self.war)):
            start = (mid-self.war[i]/2,start[1])
            self.imgtextborder(self.text[i],self.fz,start)
            start = (0,start[1]+self.hg)

    def maxfz(self,text):
        ans = int(self.h/2)
        g = gs(self.font,ans,text)[0]
        while(g>self.w-2*self.ps and ans>5):
            ans -= 1
            g = gs(self.font,ans,text)[0]
        return ans

    def imgtextborder(self,text,size,start,color="white"):        #CENTERED at start.
        #so i made this before i made the class. sue me.
        border = "thick"
        shadowcolor = "black"
        
        img = self.img
        w,h = img.width,img.height
        font = ImageFont.truetype(self.font, self.fz)
        draw = ImageDraw.Draw(self.img)
        x = int(start[0])
        y = int(start[1])
        n,m = 1,2
        if(border=="thin"):
            draw.text((x-n, y), text, font=font, fill=shadowcolor)
            draw.text((x+n, y), text, font=font, fill=shadowcolor)
            draw.text((x, y-n), text, font=font, fill=shadowcolor)
            draw.text((x, y+n), text, font=font, fill=shadowcolor)
        else:
            for a in range(x-m,x+m+1):
                for b in range(y-m,y+m+1):
                    draw.text((a,b),text,font=font,fill=shadowcolor)
            draw.text((x-m, y-m), text, font=font, fill=shadowcolor)
            draw.text((x+m, y-m), text, font=font, fill=shadowcolor)
            draw.text((x-m, y+m), text, font=font, fill=shadowcolor)
            draw.text((x+m, y+m), text, font=font, fill=shadowcolor)
        draw.text((x, y), text, font=font, fill=color)
     
def idl(path,link):
    if(link=="savedMeme"):
        pass
    else:
        response = requests.get(link)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        img.save(path)

def vidtextsetup(yid,ss,ee,tt,bt,isYid=True):
    vidlink = yid
    if isYid:
        getclip(yid,ss,ee)
        clip = VideoFileClip(yid+".mp4")
    else:
        clip = VideoFileClip("vidformats/"+yid+".mp4")
        vidlink = "vidformats/"+yid
    img = Image.open("transparent.png")
    ww,hh=clip.w,clip.h
    print("where am i?")
    #print(ww)
    img = img.resize((clip.w,clip.h))
    img.save("transparent.png")
    #print((ww,hh))        #making it the right size...
    s = impact("transparent.png",tt,isvid=True)
    s.out("temp.png")
    s = impact("temp.png",bt,top="bottom",isvid=True)
    s.out("temp.png")                 #making a transparent thing with bottom text and top text at the right parts
    #os.system("start temp.png")
    print(int(ee)-int(ss))
    #os.system("ffmpeg -y -hide_banner -loglevel panic -loop 1 -i "+yid+"tp.png"+" -c:v libx264 -t "+str(int(ee)-int(ss))+" -pix_fmt yuv420p "+yid+"tp.mp4")
    clip.close()
    os.system('ffmpeg -y -hide_banner -loglevel panic -i {} -i temp.png -filter_complex "[1]lut=a=val*1.0[a];[0][a]overlay=0:0" -c:v libx264 meme.mp4'.format(vidlink+".mp4"))
    #os.system("ffmpeg -y -hide_banner -loglevel panic -i {} -i {} -filter_complex 'overlay' meme.mp4".format(yid+"tp.mp4",yid+".mp4"))
    os.system("rm -f temp.png")
#imgpaths textar top .out(fn)

def memesetup(url,tt,bt):
    if(re.search("<",url)):
        url = url[1:-1]
    idl("meme.jpg",url)
    s = impact("meme.jpg",tt)
    s.out("meme.jpg")
    s = impact("meme.jpg",bt,top="bottom")
    s.out("meme.jpg")

def memepathsetup(path,tt,bt):
    s = impact(path,tt)
    s.out("meme.jpg")
    s = impact("meme.jpg",bt,top="bottom")
    s.out("meme.jpg")

if __name__=="__main__":
    #imgpath, textar, top
    #s = impact("meme3.png",["when you piss in the cum jar","or the cum jar pisses in you"],top="top")
    vidtextsetup("dQw4w9WgXcQ",10,20,["when mom finds out you pissed in the cum jar"],["fuck it, armenian genocide"])
    pass
