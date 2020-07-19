#import openCV
#pip install pytube3
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

def trimandcomb(yid1,s1,e1,yid2,s2,e2):
    ydl(yid1)
    ydl(yid2)
    intro = "ffmpeg -y-i {}.mp4 -i {}.mp4 -filter_complex ".format(yid1,yid2)
    middle1 = '"[0:v]trim=start={}:end={},setpts=PTS-STARTP TS[v0];[0:a]atrim=start={}:end={},asetpts=PTS-STARTPTS[a0];'.format(s1,e1,s1,e1)
    middle2 = '[0:v]trim=start={}:end={},setpts=PTS-STARTPTS[v1];[0:a]atrim=start={}:end={},asetpts=PTS-STARTPTS[a1];'.format(s1,e1,s1,e1)
    middle3 = '[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]" '
    end = '-map "[v]" -map "[a]" output.mp4'
    com = intro+middle1+middle2+middle3+end
    com = 'ffmpeg -i 1.mp4 -i 2.mp4 -filter_complex "[0:1][0:0][1:1][1:0] concat=n=2:v=1:a=1[v][a]" -map [v] -map [a] test.mp4'
    print(com)
    os.system(com)
    #fails :/

def getclip(yid,s,e):
    os.system("rm "+yid+"*")
    os.system("rm -f meme.mp4")
    link = "https://www.youtube.com/watch?v="+yid
    yt = ""
    yt = YouTube(link).streams.filter(file_extension='mp4').first().download(filename=yid)
    #ffmpeg_extract_subclip(yid+".mp4",max(0,s-1),e,targetname=yid+"2.mp4")
    #os.system("ffmpeg -y -hide_banner -loglevel panic -i "+yid+".mp4 -c:a copy -c:v copy -force_key_frames "+str(int(s)+1)+" "+yid+"2.mp4")
    #os.system("mv "+yid+"2.mp4 "+yid+".mp4")
    #os.system("ffmpeg -y -hide_banner -loglevel panic -i "+yid+".mp4 -c:a copy -c:v copy -force_key_frames "+str(int(s)+1.5)+" "+yid+"2.mp4")
    #os.system("mv "+yid+"2.mp4 "+yid+".mp4")
    #os.system("ffmpeg -y -hide_banner -loglevel panic -i "+yid+".mp4 -c:a copy -c:v copy -force_key_frames "+str(int(s)+0.5)+" "+yid+"2.mp4")
    #os.system("mv "+yid+"2.mp4 "+yid+".mp4")
    #com = "ffmpeg -y -hide_banner -loglevel panic -i "+yid+".mp4 -vcodec copy -acodec copy -ss "+str(s)+" -to "+str(e)+" "+yid+"2.mp4"
    com = "ffmpeg -y -hide_banner -loglevel panic -ss "+str(s)+" -i "+yid+".mp4 -vcodec copy -acodec copy -to "+str(float(e)-float(s))+" "+yid+"2.mp4"
    #com = "ffmpeg -y -hide_banner -loglevel panic -ss "+str(s)+" -i "+yid+".mp4 -c copy -to "+str(e)+" "+yid+"2.mp4"
    #com = "ffmpeg -y -hide_banner -loglevel panic -ss "+str(s)+"-to "+str(e)+" -i "+yid+".mp4 -c copy "+yid+"2.mp4"
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
    os.system("ffmpeg -y -hide_banner -loglevel panic -loop 1 -i "+yid+"wb.png"+" -c:v libx264 -t "+str(int(e)-int(s))+" -pix_fmt yuv420p "+yid+"wb.mp4")
    
    clip.close()
    

def vidmememake(yid):
    print("Hi")
    #print("ffmpeg -y -hide_banner -loglevel panic -i "+yid+"wb.mp4 -i"+yid+".mp4 -filter_complex vstack=inputs=2 "+yid+"2.mp4")
    os.system("ffmpeg -y -hide_banner -loglevel panic -i "+yid+"wb.mp4 -i "+yid+".mp4 -filter_complex vstack=inputs=2 "+yid+"2.mp4")
    os.system("mv "+yid+"2.mp4 "+"meme.mp4")
    os.system("rm "+yid+"*")

def bvidmememake(yid):
    print("Hi")
    #print("ffmpeg -y -hide_banner -loglevel panic -i "+yid+"wb.mp4 -i"+yid+".mp4 -filter_complex vstack=inputs=2 "+yid+"2.mp4")
    os.system("ffmpeg -y -hide_banner -loglevel panic -i "+yid+".mp4 -i "+yid+"wb.mp4 -filter_complex vstack=inputs=2 "+yid+"2.mp4")
    os.system("mv "+yid+"2.mp4 "+"meme.mp4")
    os.system("rm "+yid+"*")

def ycombine(yid1,yid2):
    os.system("rm -f mylist.txt")
    f1 = yid1+".mp4"
    f2 = yid2+".mp4"
    #os.system("echo file "+"'"+f1+"'"+">>mylist.txt")
    #os.system("echo file "+"'"+f2+"'"+">>mylist.txt")
    com = "ffmpeg -y -hide_banner -loglevel panic -i "+yid1+".mp4 -i "+yid2+".mp4 -filter_complex "+'"[0:v][0:a][1:v][1:a] concat=n=2:v=1:a=1 [outv] [outa]" -map "[outv]" -map "[outa]" '+yid1+yid2+".mp4"
    print(com)
    #os.system("ffmpeg -hide_banner -loglevel panic -i "+yid1+".mp4 -acodec libvo_aacenc -vcodec libx264 -s 1920x1080 -r 60 -strict experimental "+yid1+".webm")
    #os.system("ffmpeg -hide_banner -loglevel panic -i "+yid2+".mp4 -acodec libvo_aacenc -vcodec libx264 -s 1920x1080 -r 60 -strict experimental "+yid2+".webm")
    #com = "ffmpeg -y -hide_banner -loglevel panic -f concat -i mylist.txt "+yid1+yid2+".mov"
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
    end = ' concat=n={}:v=1:a=1 [outv] [outa]" -map "[outv]" -map "[outa]" meme.mp4'.format(int(n/3))
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