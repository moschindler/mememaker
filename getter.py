#import openCV
#pip install pytube3
#replace "cipher" with "signatureCipher" in extract.py line 295
import os
import sys
from pytube import YouTube
from moviepy.editor import *
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from whitebar import *

def ydl(yid):
    link = "https://www.youtube.com/watch?v="+yid
    yt = YouTube(link).streams.filter(file_extension='mp4').first().download(filename=yid)

def getclip(yid,s,e):
    os.system("rm "+yid+"*")
    os.system("rm -f meme.mp4")
    link = "https://www.youtube.com/watch?v="+yid
    yt = ""
    yt = YouTube(link).streams.filter(file_extension='mp4').first().download(filename=yid)
    com = "ffmpeg -y -hide_banner -loglevel panic -ss "+str(s)+" -i "+yid+".mp4 -vcodec copy -acodec copy -to "+str(float(e)-float(s))+" -vsync 0 -vf mpdecimate "+yid+"2.mp4"
    print(com)
    os.system(com)  #HOLY FUCK IT FINALLY WORKED FINALLY WOO
    os.system("mv "+yid+"2.mp4 "+yid+".mp4")

def vidmemesetup(yid,s,e,textar):
    getclip(yid,s,e)
    clip = VideoFileClip(yid+".mp4")
    w=clip.w
    #print(w)
    #print(ast.literal_eval(textar))
    bob = whitebar(w,ast.literal_eval(textar)) #width, text
    bob.out(yid+"wb.png")
    os.system("ffmpeg -y -hide_banner -loglevel panic -loop 1 -i "+yid+"wb.png"+" -c:v libx264 -t "+str(int(e)-int(s))+" -pix_fmt yuv420p -vsync 0 -vf mpdecimate "+yid+"wb.mp4")
    
    clip.close()
    

def vidmememake(yid):
    print("Hi")
    print("ffmpeg -y -hide_banner -loglevel panic -i "+yid+"wb.mp4 -i"+yid+".mp4 -filter_complex vstack=inputs=2 -vsync 0 -vf mpdecimate "+yid+"2.mp4")
    os.system("ffmpeg -y -i "+yid+"wb.mp4 -i "+yid+".mp4 -filter_complex vstack=inputs=2 "+yid+"2.mp4")
    os.system("mv "+yid+"2.mp4 "+"meme.mp4")
    os.system("rm "+yid+"*")

def bvidmememake(yid):
    print("Hi")
    #print("ffmpeg -y -hide_banner -loglevel panic -i "+yid+"wb.mp4 -i"+yid+".mp4 -filter_complex vstack=inputs=2 "+yid+"2.mp4")
    os.system("ffmpeg -y -hide_banner -loglevel panic -i "+yid+".mp4 -i "+yid+"wb.mp4 -filter_complex vstack=inputs=2 -vsync 0 -vf mpdecimate "+yid+"2.mp4")
    os.system("mv "+yid+"2.mp4 "+"meme.mp4")
    os.system("rm "+yid+"*")

def ycombine(yid1,yid2):
    os.system("rm -f mylist.txt")
    f1 = yid1+".mp4"
    f2 = yid2+".mp4"
    #os.system("echo file "+"'"+f1+"'"+">>mylist.txt")
    #os.system("echo file "+"'"+f2+"'"+">>mylist.txt")
    com = "ffmpeg -vsync 0 -y -hide_banner -loglevel panic -i "+yid1+".mp4 -i "+yid2+".mp4 -filter_complex "+'"[0:v][0:a][1:v][1:a] concat=n=2:v=1:a=1 [outv] [outa]" -map "[outv]" -map "[outa]" -vsync 0 -vf mpdecimate '+yid1+yid2+".mp4"
    print(com)
    os.system(com)

def ycombinemany(*args):
    n = len(args)
    intro = "ffmpeg -y -hide_banner -loglevel panic "
    intro2 = ""
    middle = '-filter_complex "'
    middle2 = ""
    print(n)
    for i in range(int(len(args)/3)):
        yl = args[3*i]
        s = args[3*i+1]
        e = args[3*i+2]
        getclip(yl,s,e)
        os.system("mv {}.mp4 {}.mp4".format(yl,i))
        intro2 += "-i {}.mp4 ".format(i)
        middle2 += "[{}:v][{}:a]".format(i,i)
    end = ' concat=n={}:v=1:a=1 [outv] [outa]" -map "[outv]" -map "[outa]" -vsync 0 -vf mpdecimate meme.mp4'.format(int(n/3))
    com = intro+intro2+middle+middle2+end
    print(com)
    os.system(com)
    for i in range(int(len(args)/3)):
        os.system("rm {}.mp4".format(i))





    

if __name__=="__main__":
    #vidmemesetup("dQw4w9WgXcQ",4,10,'["according to all known laws of aviation, blah bla hba lbhablh bla hba"]')
    #vidmememake("dQw4w9WgXcQ")
    #getclip(sys.argv[1],sys.argv[2],sys.argv[3])
    #getclip(sys.argv[4],sys.argv[5],sys.argv[6])
    #ycombine(sys.argv[1],sys.argv[4])
    #trimandcomb(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
    ycombinemany(*tuple(sys.argv[1:]))
    pass
