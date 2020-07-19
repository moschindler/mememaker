import discord
import asyncio
import ssl
import time
from datetime import datetime
import pandas as pd
import numpy as np
import sys
import logging
from datetime import datetime
from discord.ext import commands
from discord import File
import re
from util import *
import os
import subprocess
from getter import *
from impact import *
import asyncio
import random

nmes = 0

#server id = 695865535954550866
token = os.popen("cat token.txt | head -1").read().strip()
print(token)

bot = commands.Bot(command_prefix='?') #define command decorator

@bot.command(pass_context=True) #define the first command and set prefix to '!'
async def testt(ctx):
    await ctx.send('Hello!!')

@bot.event #print that the bot is ready to make sure that it actually logged on
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    os.system("rm *bar.png")
    os.system("rm *.mp4")
    #await bot.change_presence(game=Game(name="in rain ¬ !jhelp"))

@bot.event
async def on_message(message):
    global nmes
    bob = False
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if((len(message.content)<50 and len(message.content)>10 and len(message.content.split(" "))>0) and (not message.content[0]=="?")):
        nmes += 1
        print(nmes)
        bob = True
    if ((nmes % 100 == 50) and bob):
        infl = 0
        while bob:
            infl += 1
            if(infl>50):
                break
            try: 
                ranlink = ""
                for i in range(5):
                    rn = random.randint(0,61)
                    ranlink += alphabet[rn:rn+1]
                print(ranlink)
                response = requests.get("https://i.imgur.com/{}.jpg".format(ranlink))
                print("gothere")
                print("https://i.imgur.com/{}.jpg".format(ranlink))
                print("bump")
                img = Image.open(BytesIO(response.content))
                img.save("meme.jpg")
                s = cutatmid(message.content)
                print((s[0],s[1]))
                memepathsetup("meme.jpg",s[0],s[1])
                bob = False
                await message.channel.send(file=File("./meme.jpg"))
            except:
                pass
            
    #print(message)
    await bot.process_commands(message)
    ch = bot.get_channel(714987181818642473)
    if(not (message.author.id==bot.user.id)):
        s = message.content
        f_string_vid = "fill this in later" #...with what? I forgot
        f_string_pic = "fill this in later"
        if(s=="?sexbot test send"):
            await message.channel.send(discord.Attachment("./test.txt","test.txt"))
        if(s=="?sexbot test"):
            await message.channel.send("hi")


@bot.command(pass_context=True)
async def test(ctx):
    print("asdf")
    msg = ctx.message.content
    await ctx.message.channel.send(msg)

@bot.command(pass_context=True)
async def m(ctx):
    print("-------------------------------------------------------------------")
    #delblank('picformats.txt')
    #delblank('vidformats.txt')
    #delblank('onpicformats.txt')
    s = ctx.message.content
    opts = [i for i in s.split(" ") if i[0]=="-"]
    s = concats([i for i in s.split(" ") if (not i[0]=="-")])
    print(s)
    z = parsePicCommand(s)
    if(s=="?m help" or s=="?meme help"):
        await ctx.message.channel.send("Type ?m shelp for quick help.")
        await ctx.message.channel.send(file=File("./help.txt"))
    elif(s=="?m shelp"):
        await ctx.message.channel.send("?m [pic, bpic] [pic/format] [text]")
        await ctx.message.channel.send("?m [video, bvid] [url/code/format] [start] [end] [text]")
        await ctx.message.channel.send("?m gridlines [pic url]")
        await ctx.message.channel.send("?combine [youtube id] [start] [end] [yt id 2] [s2] [e2] ...")
        await ctx.message.channel.send("?m onpic url [font/font list] [color/color list] [size/size list] [location list] [text list list]")
        await ctx.message.channel.send("?m bt url [top text array] [bottom text array]")
        await ctx.message.channel.send("?m btvid [youtube id] start end [top text array] [bottom text array]")
    elif(s.split(" ")[1]=="gridlines"):
        gridlines(s.split(" ")[2])
        await ctx.message.channel.send(file=File("./gridlines.jpg"))
    elif(s.split(" ")[1]=="bt" or s.split(" ")[1]=="btpic"):
        z = s.split(" ")
        try:
            tarloc = contigb(z) #finds continguous bracket section
            tt = z[tarloc[0]:tarloc[1]+1]
            tt = ast.literal_eval(concats(tt))
            z = z[0:tarloc[0]]+z[tarloc[1]+1:]   #TEXTAR RETRIEVED
            tarloc = contigb(z) #finds continguous bracket section
            bt = z[tarloc[0]:tarloc[1]+1]
            bt = ast.literal_eval(concats(bt))
            z = z[0:tarloc[0]]+z[tarloc[1]+1:]   #TEXTAR RETRIEVED
            bob = True
        except:
            await ctx.message.channel.send("Something's wrong with your text arrays, amigo.")
        if(bob):
            url = z[2]
            tt,bt = bt,tt
            memesetup(getvidofformat(url,'picformats.txt'),tt,bt)
            await ctx.message.channel.send(file=File("./meme.jpg"))
    elif(s.split(" ")[1]=="btvid" or s.split(" ")[1]=="btvideo"):
        z = s.split(" ")
        bob = False
        try:
            tarloc = contigb(z) #finds continguous bracket section
            tt = z[tarloc[0]:tarloc[1]+1]
            tt = ast.literal_eval(concats(tt))
            z = z[0:tarloc[0]]+z[tarloc[1]+1:]   #TEXTAR RETRIEVED
            tarloc = contigb(z) #finds continguous bracket section
            bt = z[tarloc[0]:tarloc[1]+1]
            bt = ast.literal_eval(concats(bt))
            z = z[0:tarloc[0]]+z[tarloc[1]+1:]   #TEXTAR RETRIEVED
            bob = True
        except:
            await ctx.message.channel.send("Something's wrong with your text arrays, amigo.")
        if(bob):
            #?m btvid yid 5 10 tt bt
            yid = z[2]
            s = z[3]
            e = z[4]
            tt,bt = bt,tt
            vidtextsetup(getvidofformat(yid,"vidformats.txt"),int(s),int(e),tt,bt)
            if("-gif" in opts):
                os.system("ffmpeg -i meme.mp4 meme.gif")
                await ctx.message.channel.send(file=File("./meme.gif"))
            else:
                await ctx.message.channel.send(file=File("./meme.mp4"))
            os.system("rm -f ./meme.mp4")
            os.system("rm -f ./meme.gif")
    elif(s.split(" ")[1]=="onpic"):
        print("Hi")
        #TIME FOR THE FUCKING NIGHTMARE
        z = s.split(" ")
        tarloc = contigbb(z)
        textar = z[tarloc[0]:tarloc[1]+1]
        textar = ast.literal_eval(concats(textar))
        z = z[0:tarloc[0]]+z[tarloc[1]+1:]   #TEXTAR RETRIEVED
        sizear = []
        print(z)
        try:
            tarloc = contigb(z)
            print(tarloc)
            sizear = z[tarloc[0]:tarloc[1]+1]
            sizear = ast.literal_eval(concats(sizear))
            z = z[0:tarloc[0]]+z[tarloc[1]+1:]
        except:
            pass

        if(len(z)==3):
            tup = os.popen("grep -A1 '{}' onpicformats.txt | grep -v {}".format(z[2],z[2])).read()
            #tup = tuple(tup)
            #print("---------------------")
            tup = ast.literal_eval(tup)
            
            tup += (textar,)
            if(not sizear == []):
                tup = tup[:3]+(sizear,)+tup[4:]
            print(sizear)
            print(tup)
            alltextonpic(*tup)
            await ctx.message.channel.send(file=File("./meme.jpg"))
            pass    #fill this in later
        else:
            tup = parseOnPicCommand(s)
            print(tup)
            if not type(tup) is tuple:
                await ctx.message.channel.send("There was something wrong with your "+tup)
            else:
                alltextonpic(*tup)
                os.system("rm -f temp.txt")
                f = open('temp.txt',"w+")
                f.write(str(ctx.message.author.id))
                f.write("\n")
                f.write(str(tup[:-1]))
                f.close()
                #os.system("echo {} >>temp.text".format(ctx.message.author.id))
                #os.system("echo {} >>temp.text".format(tup[:-1]))
                
                await ctx.message.channel.send("Type ?yes <formatname> to save this as a format (so you'd only need the text next time)")
                await ctx.message.channel.send(file=File("./meme.jpg"))
    elif(isinstance(z,list)):     #MAKING A PICTURE MEME
        await ctx.message.channel.send("acknowledged")
        makememepic(z[0],z[1]).save("meme.jpg")
        await ctx.message.channel.send(file=File("./meme.jpg"))
    elif(z=="badformat"):
        await ctx.message.channel.send('The meme format you entered does not exist.')
    elif(z=='badtext'):
        await ctx.message.channel.send('Your text was in the wrong format. Try "?m help" perhaps.')
    elif(z=="badlength"):
        await ctx.message.channel.send("bruh you need some help. ?m help")
    elif(z=="vid"):     #MAKING A VIDEO MEME
        z = parseVidCommand(s)
        if(z=="bpic"):
            pass
        elif(z=="bad"):
            await ctx.message.channel.send("Somehow you fucked up the numbers LOL. its ltiealy just seconds bro")
        elif(z=="badlength"):
            await ctx.message.channel.send("try ?m help")
        elif(z=="badtext"):
            await ctx.message.channel.send("Your text was in the wrong format. Try ?m help.")
        elif(z=="badformat"):
            await ctx.message.channel.send("The format doesn't exist or maybe you entered a crappy url. Try harder or ?m help.")
        if(isinstance(z,list)):
            await ctx.message.channel.send("cool, gimme a sec.")
            #process = subprocess.check_call("./getter.sh %s %s %s %s" % (str(z[0]), str(z[1]), str(z[2]), str(z[3])),shell=True)
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            z[3] = re.sub("'","~",z[3])
            print((z[0],z[1],z[2],z[3]))
            vidmemesetup(z[0],z[1],z[2],re.sub("'","~",z[3]))
            vidmememake(z[0])
            if("-gif" in opts):
                os.system("ffmpeg -i meme.mp4 meme.gif")
                await ctx.message.channel.send(file=File("./meme.gif"))
            else:
                await ctx.message.channel.send(file=File("./meme.mp4"))
            os.system("rm -f ./meme.mp4")
            os.system("rm -f ./meme.gif")
    elif(z=="bpic"):    #MAKING A PICTURE MEME BUT THE PICTURE IS ON THE BOTTOM
        z = parsebpicCommand(s)
        if(isinstance(z,list)):
            await ctx.message.channel.send("acknowledged")
            makememebpic(z[0],z[1]).save("meme.jpg")
            await ctx.message.channel.send(file=File("./meme.jpg"))
        elif(z=="bvid"):
            pass
        elif(z=="bad"):
                await ctx.message.channel.send("Somehow you fucked up the numbers LOL. its ltiealy just seconds bro")
        elif(z=="badlength"):
                await ctx.message.channel.send("try ?m help")
        elif(z=="badtext"):
                await ctx.message.channel.send("Your text was in the wrong format. Try ?m help.")
        elif(z=="badformat"):
                await ctx.message.channel.send("The format doesn't exist or maybe you entered a crappy url. Try harder or ?m help.")
    elif(z=="bvid"):     #MAKING A VIDEO MEME
        z = parsebvidCommand(s)
        if(z=="bad"):
            await ctx.message.channel.send("Somehow you fucked up the numbers LOL. its ltiealy just seconds bro")
        elif(z=="badlength"):
            await ctx.message.channel.send("try ?m help")
        elif(z=="badtext"):
            await ctx.message.channel.send("Your text was in the wrong format. Try ?m help.")
        elif(z=="badformat"):
            await ctx.message.channel.send("The format doesn't exist or maybe you entered a crappy url. Try harder or ?m help.")
        if(isinstance(z,list)):
            await ctx.message.channel.send("cool, gimme a sec.")
            #process = subprocess.check_call("./getter.sh %s %s %s %s" % (str(z[0]), str(z[1]), str(z[2]), str(z[3])),shell=True)
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            z[3] = re.sub("'","~",z[3])
            print((z[0],z[1],z[2],z[3]))
            vidmemesetup(z[0],z[1],z[2],re.sub("'","~",z[3]))
            bvidmememake(z[0])
            if("-gif" in opts):
                os.system("ffmpeg -i meme.mp4 meme.gif")
                await ctx.message.channel.send(file=File("./meme.gif"))
            else:
                await ctx.message.channel.send(file=File("./meme.mp4"))
            os.system("rm -f ./meme.mp4")
            os.system("rm -f ./meme.gif")
    else:
        await ctx.message.channel.send("?m help...the problem was in your first argument. We only take vid,video,pic,picture,bvid,bvideo,bpic,bpicture")

@bot.command(pass_context=True)
async def yes(ctx):
    s = ctx.message.content
    s = str(s).split(" ")[1]
    f = open('temp.txt')
    aut = f.readline().strip()
    ctt = f.readline().strip()
    f.close()
    print(ctt)
    if(not aut == str(ctx.message.author.id)):
        await ctx.message.channel.send("Sorry, only the creator of the meme can save it as a format")
    else:
        print("gothere")
        if(s==""):
            await ctx.message.channel.send("You forgot the format name, ?yes <format name>")
        else:
            c = os.popen('grep -c "^{}.*$" onpicformats.txt'.format(str(s))).read()
            c = int(c)
            if(c>0):
                await ctx.message.channel.send("Format name already exists. Try another one.")
            else:
                print("gothear")
                f = open('onpicformats.txt','a')
                f.write(str(s))
                f.write("\n")
                print(ctt)
                
                #print(ctt[:-1])
                f.write(str(ctt))
                f.write("\n")
                f.close()
                await ctx.message.channel.send("Success!")


@bot.command(pass_context=True)
async def f(ctx):       #add format
    s = ctx.message.content
    if(s=="?f help"):
        await ctx.message.channel.send("adds a format")
        await ctx.message.channel.send("USAGE: ?f [either 'pic' or 'video'] [format name] [url of pic]")
        await ctx.message.channel.send("Alternatively, '?f pic list' or '?f video list' lists all known pic/video formats and their links.")
    if(s=="?f pic list"):
        await ctx.message.channel.send(allformats("picformats.txt"))
    if(s=="?f video list"):
        await ctx.message.channel.send(allformats("vidformats.txt"))
    if(s=="?f onpic list"):
        await ctx.message.channel.send(allformats("onpicformats.txt"))
    else:
        s = s.split(" ")
        if(not len(s) == 4):
            await ctx.message.channel.send("try ?f help")
        else:
            if(s[1].lower() == "video" or s[1].lower() == "v"):
                if(len(s[2])>len(s[3]) and (not len(s[3])==11)):
                    await ctx.message.channel.send("format name comes BEFORE url")
                else:
                    addformatvid(s[2],s[3])
                    await ctx.message.channel.send("nice")
            elif(s[1].lower() in ["pic","picture","image","i","p"]):
                if(len(s[2])>len(s[3])):
                    await ctx.message.channel.send("format name comes BEFORE url")
                else:
                    addformatpic(s[2],s[3])
                    await ctx.message.channel.send("nice")

@bot.command(pass_context=True)
async def combine(ctx):
    s = ctx.message.content
    opts = [i for i in s.split(" ") if i[0]=="-"]
    s = concats([i for i in s.split(" ") if (not i[0]=="-")])
    s = s.split(" ")
    print(s)
    print(s[1])
    if(len(s)<2):
        await ctx.message.channel.send("USAGE: ?combine [id 1] [start] [end] [id 2] [start] [end]")
        await ctx.message.channel.send("I'll get it working with formats later but I'm far too lazy for that now")
    elif(s[1]=="help"):
        await ctx.message.channel.send("USAGE: ?combine [id 1] [start] [end] [id 2] [start] [end]")
        await ctx.message.channel.send("I'll get it working with formats later but I'm far too lazy for that now")
    elif(len(s)>=7):
        bob = True
        s = s[1:]
        for i in range(int(len(s[1:])/3)):
            s[3*i] = getvidofformat(s[3*i],"vidformats.txt")
            if(re.search("youtube",s[3*i])):
                s[3*i] = s[3*i].split("?v=")[1][:11]
            if(not (len(s[3*i])==11)):
                await ctx.message.channel.send("One of your youtube ids is bad...")
                bob = False
            elif(not (isFloat(s[3*i+1]) and isFloat(s[3*i+2]))):
                ctx.message.channel.send("One of your times is bad...please use the time in seconds (as an int or decimal)")
                bob = False
        if(bob):
            print(tuple(s))
            await ctx.message.channel.send("Gotcha. This might take a bit...")
            ycombinemany(*tuple(s))
            await ctx.message.channel.send("Done.")
            if("-gif" in opts):
                os.system("ffmpeg -i meme.mp4 meme.gif")
                await ctx.message.channel.send(file=File("./meme.gif"))
            else:
                await ctx.message.channel.send(file=File("./meme.mp4"))
            os.system("rm -f ./meme.mp4")
            os.system("rm -f ./meme.gif")
    elif(len(s)==7):
        id1 = getvidofformat(s[1],"vidformats.txt")
        id2 = getvidofformat(s[4],"vidformats.txt")
        if(re.search("youtube",id1)):
            id1 = id1.split("?v=")[1][:11]
        if(re.search("youtube",id2)):
            id2 = id2.split("?v=")[1][:11]
        if(not (len(id1)==11 and len(id2)==11)):
            await ctx.message.channel.send("One of your youtube ids is bad...")
        elif(not (isFloat(s[2]) and isFloat(s[3]) and isFloat(s[5]) and isFloat(s[6]))):
            await ctx.message.channel.send("One of your times is bad...please use the time in seconds (as an int or decimal)")
        else:
            print((id1,s[2],s[3],id2,s[5],s[6]))
            getclip(id1,s[2],s[3])
            getclip(id2,s[5],s[6])
            ycombine(id1,id2)
            if("-gif" in opts):
                os.system("ffmpeg -i {}{}.mp4 meme.gif".format(id1,id2))
                await ctx.message.channel.send(file=File("./meme.gif"))
            else:
                await ctx.message.channel.send(file=File("./{}{}.mp4".format(id1,id2)))
            os.system("rm -f ./{}{}.mp4".format(id1,id2))
            os.system("rm -f ./meme.gif")
            #await ctx.message.channel.send(file=File("./"+id1+id2+".mp4"))

            print("Combined vid should have sent")
            #os.system("rm -f "+id1+"*")
            #os.system("rm -f "+id2+"*")
    else:
        await ctx.message.channel.send("?combine help")
            


@bot.command(pass_context=True)
async def send(ctx):
    await ctx.message.channel.send("test")
    await ctx.message.channel.send(file=File("./white.png"))

@bot.command(pass_context=True)
async def restart(ctx):
    await ctx.send("Restarting...")
    os.execv(sys.executable,['python3'] + sys.argv)

@bot.command(pass_context=True)
async def r(ctx):
    await ctx.send("Restarting...")
    os.execv(sys.executable,['python3'] + sys.argv)

@bot.command(pass_context=True)
async def kill(ctx):
    exit()

#KEY FOR FLOWALGO
KEY = "863f942a072346d24c32"

bot.run(token)

