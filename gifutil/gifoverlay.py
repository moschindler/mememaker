import os
from PIL import Image, ImageSequence
#os.system('ffmpeg -hide_banner -loglevel error -y -i tenor3.mp4 -ignore_loop 0 -i cat.gif -filter_complex "[1:v]scale=100:100[ovrl];[0:v][ovrl]overlay=0:0" -frames:v 900 -codec:a copy -codec:v libx264 -crf 18 -max_muxing_queue_size 2048 video.mp4')

def toVid(gifp,vidp="temp.mp4"):    #converts gif to mp4 given gif path and output path
    os.system('ffmpeg -y -hide_banner -loglevel error -i {} -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" {}'.format(gifp,vidp))
    print("hi")

def toGif(vidp,gifp="temp.gif"):
    i = os.popen('ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {}'.format(vidp)).read().strip().split("x")
    os.system('ffmpeg -y -hide_banner -loglevel error -i {} -vf "fps=10,scale={}:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 {}'.format(vidp,i[0],gifp))

def overlayPic(back,over,ll,ur,vidp="out.mp4"):   #background path, overlay path, ..
    l = os.popen("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {}".format(over)).read().strip()   #length of the gif
    backVid = back.split(".")[0]+".mp4"    #here's praying for no dots
    (w,h) = Image.open(back).size
    w = w+w%2
    h = h+h%2
    os.system("ffmpeg -hide_banner -loglevel error -y -loop 1 -i {} -c:v libx264 -t {} -pix_fmt yuv420p -vf scale={}:{} {}".format(back,str(int(float(l))),str(w),str(h),backVid))
    back = backVid

    i = os.popen('ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {}'.format(back)).read().strip().split("x")

    ulx = str(min(ll[0],ur[0]))
    uly = str(min(ll[1],ur[1]))
    vx = str(abs(ll[0]-ur[0])*float(i[0])/100)
    vy = str(abs(ll[1]-ur[1])*float(i[1])/100)
    s = 'ffmpeg -hide_banner -loglevel error -y -i {} -i {} -filter_complex "[1:v]scale={}:{}[ovrl];[0:v][ovrl]overlay=W*{}/100:H*{}/100" -t {} -codec:a copy -codec:v libx264 -crf 18 -max_muxing_queue_size 2048 {}'.format(back,over,vx,vy,ulx,uly,str(int(float(l)+0.5)),vidp)
    os.system(s)
    os.system("rm {}".format(backVid))

def overlayVid(back,over,ll,ur,vidp="out.mp4"):   #background path. Overlay is a picture this time.
    if ".gif" in back:
        back2 = back.split(".gif")[0]   #ehe
        toVid(back,vidp=back2+".mp4")
        back = back2+".mp4"

    i = os.popen('ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {}'.format(back)).read().strip().split("x")
    l = os.popen("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {}".format(back)).read().strip()
    ulx = str(min(ll[0],ur[0]))
    uly = str(min(ll[1],ur[1]))
    vx = str(abs(ll[0]-ur[0])*float(i[0])/100)
    vy = str(abs(ll[1]-ur[1])*float(i[1])/100)
    s = 'ffmpeg -hide_banner -loglevel error -y -i {} -stream_loop -1 -i {} -filter_complex "[1:v]scale={}:{}[ovrl];[0:v][ovrl]overlay=W*{}/100:H*{}/100" -t {} -codec:a copy -codec:v libx264 -crf 18 -max_muxing_queue_size 2048 {}'.format(back,over,vx,vy,ulx,uly,str(int(float(l)+0.5)),vidp)
    #print(s)
    
    os.system(s)
    
if __name__=="__main__":
    #overlayVid("giffy.gif","paimu.gif",(70,30),(100,70))
    overlayPic("untitled.png","thanostwerk.gif",(30,10),(70,90))
    toGif("out.mp4",gifp="meme.gif")
    os.system("rm out.mp4")
