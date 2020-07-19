
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import requests
import ast
import re

def join(arr):
    s = ""
    s += arr[0]
    for i in range(1,len(arr)):
        s += " "
        s += arr[i]
    return s

def gs(fontname,fontsize,text):
    return ImageFont.truetype(fontname,fontsize).getsize(text)

def tsum(a,b): #adds two tuples element-wise, e.g. (1,2)+(3,4)=(4,6)
    return tuple(map(sum,zip(a,b)))

def tsums(*args):
    ans = (0,0)
    for d in args:
        ans = tsum(ans,d)
    return ans

class bar: #VERY DIFFERENT FROM TRANSPARENT BAR! THE DIFFERENCE COMES FROM CENTERING TEXT
    def __init__(self,w,mtr,font="fonts/Helvetica.ttf",angle=0,boxcoords=[],centered=False):    #meme text 'rray
        self.tar = mtr #text of white bar
        self.tar = [re.sub("~","'",d) for d in self.tar]
        self.w = w      #image width (not the white bar...ok i guess it is the white bar :/)
        self.fontname = font    #FUCKING FREETYPE VS. TRUETYPE ISSUES
        self.font = font
        self.centered = centered
        self.angle = angle   

        #self.out(fn)
        #     
    def params(self):
        print("(w,font,pads,padh,gap,fullstop)")
        print((self.w,self.fz,self.ps,self.pt,self.hg,self.fs))
    
    def ts(self,text):  #size of some text
        return gs(self.fontname,self.fz,text)

    def tsum(self,a,b): #adds two tuples element-wise, e.g. (1,2)+(3,4)=(4,6)
        return tuple(map(sum,zip(a,b)))

    def getlen(self,lol):    #how large is our white bar going to be, anyway...
        l = len(lol)
        z = len([val for sublist in lol for val in sublist])    #shrugggu
        #okay fs is the weird shit and hg is the normal shit
        leng = int(2.5*self.pt+(z-1)*self.hg+(l-1)*self.fs)   #is that right?
        leng += leng % 2
        return leng


    def splat1(self,s):  #splits a long-ass piece of text into several rows of text. or maybe just 1.
        words = s.split(" ")
        ans = []
        for i in range(len(words)):
            if(self.ts(words[i])[0] > self.w-2*self.ps):
                return s
        while(len(words)>0):
            #print(words)
            curs = ""
            #print(words)
            bob = True
            for i in range(len(words)):
                if(self.ts(curs + " " + words[i])[0] > self.w - 2*self.ps):
                    bob = False
                    break
                else:
                    if(i==0):
                        curs += words[i]
                    else:
                        curs += " " + words[i]
            if(i==len(words)-1 and bob):
                ans.append(curs)
                words = []
            else:
                ans.append(curs)
                words = words[i:]
            
        return ans
    
    def splat(self,ar):     #does that thingy but like for each word in the whosamawhatsit
        ans = []
        for i in ar:
            ans.append(self.splat1(i))
        return ans
    
    def splatter(self):
        img = Image.open("white.png")
        self.font = ImageFont.truetype(self.font, self.fz)
        img = img.resize((self.w,1000))
        draw = ImageDraw.Draw(img)
        self.texty = self.splat(self.tar)   #what? why not just mtr?
        self.img = self.img.resize((self.w,self.getlen(self.texty)))
        self.draw = ImageDraw.Draw(self.img,"RGB")

        #...sound ok?

    def writeline(self,start,text):
        self.draw.text(start, text, (0,0,0), font=self.font)

    def writelines(self,tar):    #WRITE! ALL THE LINES!
        start = self.start
        for i in tar:
            for j in i:
                print(j)
                self.writeline(start,j)
                start = self.tsum(start,(0,self.hg))        #in retrospect hg was a stupid variable name
            start = self.tsum(start,(0,self.fs))
        #NICE!!!!!!!!!!!!!!!!!!!

    def out(self,fn):
        self.img.save(fn)
    