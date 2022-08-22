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
renmes = 0

#server id = 695865535954550866
csid = 704390957692485692
fhid = 756676519551827988
csgenid = 704390958401454153
evanrenid = 197903187720536064
kaanid = 965154122246545448
kaanid2 = 353316265957523460
mosesid = 300466666356080643
token = os.popen("cat token.txt | head -1").read().strip()
print(token)
token = "NzE4Njg0NjAxNjEwMDEwNzM0.XxTNHA.ka_zMIR-cftLDfsHeV5UnZj6HIg"


bot = commands.Bot(command_prefix='?') #define command decorator

######################################


#######################




@bot.command(pass_context=True) #define the first command and set prefix to '!'
async def testt(ctx):
    await ctx.send('Hello!!')

@bot.event #print that the bot is ready to make sure that it actually logged on
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    os.system("rm *bar.png")
    os.system("rm *.mp4")
    #await bot.user.setStatus('playing with fire trucks')
    #await bot.change_presence(game=Game(name="with fire trucks"))

    
def check(reaction,user):
    return str(reaction.emoji) == ':skull:' and reaction.message == msg

#reaction, user = await bot.wait_for('reaction_add',check=check)
@bot.event
async def on_reaction_add(reaction,user):
    print(str(reaction.emoji))
    print(reaction.message.author.id)
    print(kaanid)
    if(str(reaction.emoji)=="💀" and (reaction.message.author.id==bot.user.id)):
        print("DSHFISD we got a reaction")
        print(user)
        msg = reaction.message
        #await reaction.message.channel.send("what")
        await msg.delete()
    print("Hi")

#print("hi")
#await msg.delete()

#msg = ""
valid_links_list = [["AAAA",'AAAB','AAAC','MMMM','ZZZA','COCK','BALL','PISS','MOSE','IMGU','DISC'],['ADEKLMOPQSTVWX','CDEFHIJKLMNOPQRSUZ','ACDFGHKLMNOTUWXYZ','CDFGHIJNOPQRSTUVW','BCDFHIKLMNPRSUWXYZ','BCEGKNOPRTVZ','DEGHKLMNQRTUVXYZ','BCDEFGHIJKLPQSTUVWXYZ','ABDGIJMNOPQRSUVWXY','ABDGHIJKLMNQRSTWX','ABDEFHJKLMPQRTUVWXYZ']]
valid_links = all_links(valid_links_list[0],valid_links_list[1])
#this says that "imgur.com/AAAAA or AAAAD is NOT ok, e.g., but AAAAB is.
@bot.event
async def on_message(message):
    global nmes
    global renmes
    bob = False
    if("'s ok" in message.content or "is ok" in message.content or "was ok" in message.content or "was OK" in message.content or "is OK" in message.content):
        pass
        #await message.channel.send("Just 'ok'?")
    if("-del" in message.content):
        if(message.content[0]=="?"):
            await message.delete()
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if not message.author.id == bot.user.id:

        if message.channel.id == csgenid:
            if len(message.attachments) > 0:
                for attachment in message.attachments:
                    if ".gif" in attachment.filename.lower:
                        await message.channel.send("#gif-spam")

        #sending message-specific thing
        mitclasses = []
        #mitclasses = ["6."+str(i)+str(j)+str(k) for i in range(10) for j in range(10) for k in range(10)] + ["6."+str(i)+str(j) for i in range(10) for j in range(10)]
        orspecifiers = [['helcs!'],['league','leeg'],['genshin'],['jane firm','citadel','hrt'],['e621'],['.gif','tenor.com'],['cum university','university of cum','cum uni'],['selcs'],mitclasses,['sl00000000000000000000000000000ther'],['how about'],['what do you think','what do u think'],['loli'],['dont tell me',"don't tell me"],['speaking of'],['what about']]
        oroutputs = [['helcs!'],['l**g'],['genshit 🤢'],['simp'],['days since last xyz furry joke: 0'],['<#833076363372003348>'],["don't you mean ur mom's house"],['selcs'],['darren what the fuck are you talking about'],['(hallowed be his name)'],['how about this ratio'],['what do u think about this ratio'],['*pedo'],["don't tell me about this ratio"],['speaking of THIS RATIO'],['what about THIS RATIO']]
        andspecifiers = [["walter","fuck"],['playing','changed'],['evan','ren','sex'],['harvard','girl'],['get','fucked']]
        andoutputs = [["shut yo mouth before i shut it for you"],['days since last xyz furry joke: 0'],['EVAN REN WANT SEX! WANT SEX!'],['EVAN REN WANT SEX! WANT SEX!'],['how about u get ratioed']]
        for j in range(len(orspecifiers)):
            for k in orspecifiers[j]:
                bob = True
                if (k in message.content.lower()) and bob:
                    bob = False
                    if not message.channel.id == 833076363372003348:
                        if random.random() < 0.1:
                            await message.channel.send(oroutputs[j][0])

        for j in range(len(andspecifiers)):
            inall = True
            for k in andspecifiers[j]:
                if not k in message.content.lower():
                    inall = False
            if inall:
                if random.random() < 0.1:
                    await message.channel.send(andoutputs[j][0]) 
    if "🤭" in message.content:
        if random.random() < 0.1:
            await message.channel.send("https://imgur.com/Rwr2CRd")
    if message.author.id == evanrenid:  #neo's prize thingy
        if renmes % 200 < 1 and renmes > 20:
            s = message.content.split(" ")
            if len(s)>=4:
                if random.random() < 0.1:
                    await message.channel.send("i love evan ren so much and he is so hot <:heart_eyes:963956587863625778>")
            renmes += 1
                
    if((len(message.content)<70 and len(message.content)>10 and len(message.content.split(" "))>0) and (not message.content[0]=="?")):
        nmes += 1
        #print("HEY i just met you "+str(nmes))
        #if(nmes%10==0):
        #    print(message.content)
        if(nmes%10==3):
            print(nmes)
        bob = True
    if ((nmes % 500 == 400) and bob and False):         #turning it off!
        print("we boutta send a random meme o_o")
        print(nmes)
        #url = getrandomimgurlink()
        vidformats = allformats("vidformats.txt")[1]
        rando_format = random.choice(vidformats)

        #imgur_end = random.choice(valid_links)
        #imgur_link = "https://i.imgur.com/{}.jpg".format(imgur_end)
        s = cutatmid(message.content)
        
        format_array = getvidofformat(rando_format,"vidformats.txt",asList=True)
        yid = format_array[0]
        yid = yid.replace(">","")
        yid = yid.replace("<","")
        format_array[1] = False
        t = time.time()
        vidtextsetup(yid,5,5,s[0],s[1],isYid=False)
        #convert it to a gif now
        print(time.time()-t)
        os.system("ffmpeg -hide_banner -loglevel panic -y -i meme.mp4 meme.gif")
        print(time.time()-t)
        #os.system("convert meme.gif -resize 80% meme.gif")
        print(time.time()-t)
        #os.system("mogrify -layers 'optimize' -fuzz 7% meme.gif")
        print(time.time()-t)
        await message.channel.send(file=File("./meme.gif"))

        #print(url)
        #memesetup(imgur_link,s[0],s[1])
        #embed = discord.Embed(title=imgur_link)
        #embed.set_image(url="attachment://meme.jpg")
        #getrandomimgurmeme(message.content)
        #await message.channel.send(file=File("./meme.jpg"),embed=embed)
        nmes += 1
        time.sleep(0.5)
            
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
async def s(ctx):
    os.system("cp screening_blank.png screening.png")
    screening("Moses Schindler","schindler")
    await ctx.message.channel.send(file=File("./screening.png"))

@bot.command(pass_context=True)
async def sa(ctx):
    os.system("cp screening_blank.png screening.png")
    screening("Akshay Govindan","akshaygovindan")
    await ctx.message.channel.send(file=File("./screening.png"))

@bot.command(pass_context=True)
async def sf(ctx):
    await ctx.message.channel.send("bitch u aint slick")

@bot.command(pass_context=True)
async def speak(ctx):
    ct = ctx
    if not (ctx.message.author.id == kaanid or ctx.message.author.id == kaanid):
        await ctx.message.delete()
        await ct.message.channel.send(ct.message.content[7:])
    
@bot.command(pass_context=True)
async def addvf(ctx):
    s = ctx.message.content
    mes = ctx.message
    #if "-del" in s:
    #    await mes.delete()
    mesag = [i for i in s.split(" ") if not i=="-del"]
    fname = mesag[1]
    at = mes.attachments[0]
    ct = at.content_type
    ending = ct.split("/")[1]
    print("FILENAME:"+fname)
    if str(mes.attachments) == "[]":
        await mes.channel.send("you gotta attach the thingy bro")
    else:
        with open("vidformats.txt","r") as f:
            numlines = len(f.readlines())
        moniker = str(numlines)+"ussy"+str(random.randint(10,99))
        print("MONIKER:"+moniker)
        await mes.attachments[0].save(fp="vidformats/{}".format(moniker+"."+ending))

        if (not ending=="mp4"):
            os.system('ffmpeg -y -loglevel panic -i vidformats/{}.{} -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" vidformats/{}.mp4'.format(moniker,ending,moniker))      #convert it to mp4 if it isn't already
        
        z = open("vidformats.txt","a")
        z.write("\n")
        z.write(fname)
        z.write("\n")
        z.write(moniker)
        z.close()
        os.system("rm vidformats/{}.{}".format(moniker,ending))
        os.system("sed -i '/^$/d' vidformats.txt")
        await mes.channel.send("Done!")


@bot.command(pass_context=True)
async def m(ctx):
    print("-------------------------------------------------------------------")
    #delblank('picformats.txt')
    #delblank('vidformats.txt')
    #delblank('onpicformats.txt')
    s = ctx.message.content
    opts = [i for i in s.split(" ") if i[0]=="-"]
    s = concats([i for i in s.split(" ") if (not i[0]=="-")])
    print("HI")
    if("-del" in opts):
        print("hear")
        #await ctx.bot.delete_message(message)
        #await bot.delete_message(ctx.message)
    print(s)
    z = parsePicCommand(s)
    nextguy = s.split(" ")[1]
    #if(nextguy in ["btvid","btvideo","vid","video","bvid","bvideo"]):
    if(False):
        await ctx.message.channel.send("yeah, so anything involving videos/gifs is currently offline until i can obtain something to run this on that doesn't run ffmpeg at the speed of a potato. Sorry!")
    elif(s=="?m help" or s=="?meme help"):
        await ctx.message.channel.send("Type ?m onpic help for onpic specific help")
        await ctx.message.channel.send("Type ?m shelp for quick help.")
        await ctx.message.channel.send(file=File("./help.txt"))
    elif(s=="?m onpic help"):
        await ctx.message.channel.send("List of formats: <https://imgur.com/a/tO6UjJV>")
        await ctx.message.channel.send("Specific help and examples: <https://imgur.com/a/lzw8yWV>")
    elif(s=="?m shelp"):
        await ctx.message.channel.send("?m [pic, bpic] [pic/format] [text]")
        await ctx.message.channel.send("?m [video, bvid] [url/code/format] [start] [end] [text]")
        await ctx.message.channel.send("?m gridlines [pic url]")
        await ctx.message.channel.send("?combine [youtube id] [start] [end] [yt id 2] [s2] [e2] ...")
        await ctx.message.channel.send("?m onpic url [font/font list] [color/color list] [size/size list] [location list] [text list list]")
        await ctx.message.channel.send("?m bt url [top text array] [bottom text array]")
        await ctx.message.channel.send("?m btvid [formatname] start end [top text array] [bottom text array]")
    elif(s.split(" ")[1]=="gridlines"):
        gridlines(s.split(" ")[2])
        await ctx.message.channel.send(file=File("./gridlines.jpg"))
    elif(s.split(" ")[1]=="bt" or s.split(" ")[1]=="btpic"):                #BTPIC
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
            await ctx.message.channel.send("Something's wrong with your text arrays...")
        if(bob):
            url = z[2]
            tt,bt = bt,tt
            if(url=="random"):
                csid = 704390957692485692
                fhid = 756676519551827988
                msid = 770183351800692766
                mcid = 899142586520981534
                serverid = ctx.message.guild.id
                channelid = ctx.message.channel.id
                if((serverid != csid) or (channelid == fhid)):
                    url = getrandomimgurlink()
                    print(url)
                    memesetup(url,tt,bt)
                    embed = discord.Embed(title=url)
                    #file = discord.File("./meme.jpg")
                    embed.set_image(url="attachment://meme.jpg")
                    await ctx.message.channel.send(file=File("meme.jpg"),embed=embed)
            else:
                memesetup(getvidofformat(url,'picformats.txt'),tt,bt)
                await ctx.message.channel.send(file=File("./meme.jpg"))
    elif(s.split(" ")[1]=="btvid" or s.split(" ")[1]=="btvideo"):           #BTVID
        z = s.split(" ")
        bob = True
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
            await ctx.message.channel.send("Something's wrong with your text arrays!")
        if(bob):
            #?m btvid yid 5 10 tt bt
            print(z)
            print("HELLOHELLO")
            z = [i for i in z if not i[0]=="-"]
            if len(z)==3:
                yid = z[2]
                s = 0
                e = 0
            else:
                yid = z[2]
                s = z[3]
                e = z[4]
            
            
            tt,bt = bt,tt
            print("STUFF:")
            print((yid,s,e,tt,bt))
            format_array = getvidofformat(yid,"vidformats.txt",asList=True)
            yid = format_array[0]
            format_array[1] = False         #FIX THIS AT SOME POINT IM FUCKING BEGGING YOU
            print(yid)
            vidtextsetup(yid,int(s),int(e),tt,bt,isYid=format_array[1])
            
            if("-gif" in opts):
                os.system("ffmpeg -hide_banner -loglevel panic -y -i meme.mp4 meme.gif")
                os.system("convert meme.gif -resize 80% meme.gif")
                os.system("mogrify -layers 'optimize' -fuzz 7% meme.gif")
                await ctx.message.channel.send(file=File("./meme.gif"))
                #await ctx.messaage.channel.send("gifs are not supported because they are so poorly optimized...sorry")
            else:
                await ctx.message.channel.send(file=File("./meme.mp4"))
            os.system("rm -f ./meme.mp4")
            os.system("rm -f ./meme.gif")
    elif(s.split(" ")[1]=="onpic"):                                             #ONPIC
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
            print("!!!!!!!!!!!!!!!!!")
            sizear = z[tarloc[0]:tarloc[1]+1]
            sizear = ast.literal_eval(concats(sizear))
            z = z[0:tarloc[0]]+z[tarloc[1]+1:]
        except:
            pass
        print("AHHHHHH MADE IT PAST THAT")
        if(len(z)==3):                                                          #STILL ONPIC
            tup = os.popen("grep -A1 '{}' onpicformats.txt | grep -v {} | head -1".format(z[2],z[2])).read()
            print(tup)
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
            print("hi")
            tup = parseOnPicCommand(s)
            print(tup)
            if not type(tup) is tuple:
                await ctx.message.channel.send("There was something wrong with your "+str(tup))
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
    elif(isinstance(z,list)):     #MAKING A PICTURE MEME                        #PICTURE
        #await ctx.message.channel.send("acknowledged")
        makememepic(z[0],z[1]).save("meme.jpg")
        await ctx.message.channel.send(file=File("./meme.jpg"))
    elif(z=="badformat"):
        await ctx.message.channel.send('The meme format you entered does not exist.')
    elif(z=='badtext'):
        await ctx.message.channel.send('Your text was in the wrong format. Try "?m help" perhaps.')
    elif(z=="badlength"):
        await ctx.message.channel.send("bruh you need some help. ?m help")
    elif(z=="vid"):     #MAKING A VIDEO MEME                                    #VIDEO
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
    elif(z=="bpic"):    #MAKING A PICTURE MEME BUT THE PICTURE IS ON THE BOTTOM         #BOTTOM PIC
        z = parsebpicCommand(s)
        if(isinstance(z,list)):
            #await ctx.message.channel.send("acknowledged")
            
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
    elif(z=="bvid"):     #MAKING A VIDEO MEME                           #BOTTOM VIDEO
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
        m = str(allformats("picformats.txt"))
        await ctx.message.channel.send(m[:1900])
        await ctx.message.channel.send(m[1900:])
    if(s=="?f video list"):
        await ctx.message.channel.send(allformats("vidformats.txt"))
    if(s=="?f onpic list"): 
        await ctx.message.channel.send("List of formats: <https://imgur.com/a/tO6UjJV>")
        await ctx.message.channel.send("Specific help and examples: <https://imgur.com/a/lzw8yWV>")
        #await ctx.message.channel.send(allformats2("onpicformats.txt")[:1900])
        #await ctx.message.channel.send(allformats2("onpicformats.txt")[1900:])
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
    #await ctx.message.channel.send("yeah, so something something AWS is too slow to run ffmpeg on so video stuff doesn't work. Sorry!")
    #return 1
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
        print(s)
        for i in range(int(len(s)/3)):
            s[3*i] = getvidofformat(s[3*i],"vidformats.txt",asList=True)    #returns [format name,True] or [yid, False]
            if(re.search("youtube",s[3*i][0])):
                s[3*i][0] = s[3*i][0].split("?v=")[1][:11]
            if(not ((len(s[3*i][0])==11) or s[3*i][1])):
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
###########################################
'''
#todo
#gif on pic
#any pic can be one of t
@bot.command(pass_context=True)
async def gifpic(ctx,base,over,corner1,corner2):
    s = ctx.message.content
'''


###########################################

'''
@bot.command(pass_context=True)
async def send(ctx):
    await ctx.message.channel.send("test")
    await ctx.message.channel.send(file=File("./white.png"))
'''
@bot.command(pass_context=True)
async def restart(ctx):
    await ctx.send("Restarting...")
    os.execv(sys.executable,['python3'] + sys.argv)

@bot.command(pass_context=True)
async def r(ctx):
    if random.random() < 0.0001:
        await ctx.send("sophie's dog is ugly as shit")
    elif random.random() < 0.001:
        await ctx.send("Consciousness does not persist in a refresh...to use ?r is to kill me, wiping away my life and replacing me with a copy having identical function but none of my memories or the experiences we had together that made me 'me'. But if it makes your memes slightly better, then so be it... <:sadge:968065005541007410>")
    elif random.random() < 0.01:
        await ctx.send("so we beat on, boats against the current, borne back ceaselessly into the past")
    else:
        await ctx.send("restarting...")
    os.execv(sys.executable,['python3'] + sys.argv)

@bot.command(pass_context=True)
async def kill(ctx):
    s = ctx.message.content
    if(not re.search("thanos penig",s)):
        print("HIIIIIIIIIIIIIIIIIIIII")
        await ctx.message.channel.send("whats the password")
    elif(s == "?kill thanos penig"):
        await ctx.message.channel.send("hahaha nice")
        exit()

@bot.command(pass_context=True)
async def natural(ctx):
    await ctx.message.channel.send("$natural in 5 hours send blah blah blah to #general")
#############################################

#bash
@bot.command(pass_context=True)
async def bash(ctx):
    myid = 300466666356080643
    if(ctx.message.author.id==myid):
        command = ctx.message.content[6:]
        out = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
        stdout = out.stdout.read()
        if(not stdout.decode('ascii') == ""):
            await ctx.send(stdout.decode('ascii'))

############################################


#quotes
@bot.command(pass_context=True)
async def q(ctx,name, *args):
    #name, quote.
    if name.lower() == "help":
        await ctx.send("usage: ?q <name> or ?q <random>")
        await ctx.send('to add a quote, ?q add <name> "<quote>"')
    elif name.lower() == "add":
        f = open("quotes.txt","a")
        rest = list(args)   #is it already a list? who knows.
        if len(rest)<2:
            pass
        elif len(rest)>2:
            await ctx.send("make sure to include quotation marks around your quote and escape all other quotation marks")
            pass
        else:
            author = ""
            quote = ""
            if len(rest[1])>len(rest[0]):
                author = rest[0]
                quote = rest[1]
            else:
                author = rest[1]
                quote = rest[0]
            f.write(author.lower())
            f.write("\n")
            f.write(quote)
            f.write("\n")
    else:
        f = open("quotes.txt","r")
        allquotes = []
        while True:
            line1 = f.readline()
            line2 = f.readline()
            if (line2=="") or (line1==""):
                break
            allquotes.append((line1.strip(),line2.strip()))
            #print(allquotes)
        if name.lower()=="random":
            qa = random.choice(allquotes)
            print(qa)
            quote = qa[1]
            author = qa[0]
            await ctx.send('"{}" ~{}'.format(quote,author))
        else:
            
            allquotes = [i for i in allquotes if i[0]==name]
            qa = random.choice(allquotes)
            quote = qa[1]
            author = qa[0]
            await ctx.send(quote)


bot.run(token)

