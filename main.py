import discord
from discord.ext import commands
import random
from ext import *
import music
import os # For fetching ENV SECRETS
from keep_alive import keep_alive # Uptime Robot SRC file
import re, urllib.parse, urllib.request
from random import choice
from youtube_search import YoutubeSearch # pip install youtube_search
import time # Sleep functions
import praw # pip install praw
import pyjokes # pip install pyjokes
# import googlesearch # pip install beautifulsoup4 google
import requests, json, wikipedia # pip install requests wikipedia
from dotenv import load_dotenv # pip install python-dotenv
from titan import shorten # Shortening urls with titan
import bs4

# Function to get memes from praw (Python Reddit API Wrapper)
def getmeme(topic): # Topic/Subreddit name
    reddit = praw.Reddit(client_id=REDDIT_CID,
                    client_secret=REDDIT_SCT,
                    user_agent='meme') # Initializing details

    submission = reddit.subreddit(topic)
    return submission.title, submission.url

# ---------------------------------------------------------------------------------------

REDDIT_CID = os.getenv('REDDIT_CID')
REDDIT_SCT = os.getenv('REDDIT_SCT')
TKEY = os.getenv("TENOR_KEY")
RMKEY = os.getenv("rmkey")



def drt(limit):
    import random
    password = random.randint(10000, 30000)
    return str(password)


# GIFs for Damn Son react
dms = ["https://giphy.com/gifs/batman-film-qVID3J8fLrlZK", "https://giphy.com/gifs/homer-simpson-barney-batman-and-robin-pSFEEQMaNcFAQ", "https://giphy.com/gifs/hug-5sos-5-seconds-of-summer-BcOvvS5t0sxnG", 'https://giphy.com/gifs/joker-the-joaquin-phoenix-A7ZbCuv0fJ0POGucwV']

# GIFs for LOL react
lolm = ['https://giphy.com/gifs/originals-lol-3o6ozvv0zsJskzOCbu', 'https://giphy.com/gifs/theoffice-episode-6-the-office-tv-bC9czlgCMtw4cj8RgH','https://giphy.com/gifs/moodman-lol-spit-take-Q7ozWVYCR0nyW2rvPW', 'https://giphy.com/gifs/moodman-funny-lol-laughing-fUYhyT9IjftxrxJXcE', 'https://giphy.com/gifs/laughing-despicable-me-minions-ZqlvCTNHpqrio', 
'https://giphy.com/gifs/laughing-applause-mike-tyson-wWue0rCDOphOE']

# GIFs for Yay reaction
yaym = [
    "https://giphy.com/gifs/F9hQLAVhWnL56",
    "https://giphy.com/gifs/thegifys-gifys-5xaOcLGvzHxDKjufnLW",
    "https://giphy.com/gifs/studiosoriginals-dog-josh-freydkis-bad-woof-l41Ym8O8dbIG0XvFK",
    "https://giphy.com/gifs/sherlockgnomes-sherlock-l4pTfx2qLszoacZRS",
    'https://giphy.com/gifs/foxinternational-reaction-simpsons-celebrate-26tPplGWjN0xLybiU',
    "https://giphy.com/gifs/excited-screaming-jonah-hill-5GoVLqeAOo6PK",
    "https://giphy.com/gifs/excited-yes-30-rock-I24hjk3H0R8Oc"
]



# GIFs for Yes Reaction
yesm = [
    "https://giphy.com/gifs/theoffice-MNmyTin5qt5LSXirxd",
    "https://giphy.com/gifs/DffShiJ47fPqM",
    "https://giphy.com/gifs/dYZuqJLDVsWMLWyIxJ"
]

susm = ["https://giphy.com/gifs/confused-futurama-suspicious-ANbD1CCdA3iI8","https://giphy.com/gifs/moodman-monkey-side-eye-sideeye-H5C8CevNMbpBqNqFjl","https://giphy.com/gifs/tiktok-cute-aww-jRHD367KLHU7NsPjmb",
"https://giphy.com/gifs/reaction-mood-3gNotAoIRZsb9UHPnj"]

# GIFs for No Reaction
nom = [
    "https://giphy.com/gifs/the-office-mrw-d10dMmzqCYqQ0",
    "https://giphy.com/gifs/NetflixisaJoke-netflix-iglesias-mr-h5cl6eHMvf0IQ3wJch",
    "https://giphy.com/gifs/memecandy-J46T6SB3yzwc4eBYeL"
]

# ---------------------------------------------------------------------------------------

# Use of Zenquotes API to fetch motivating quotes
def get_quote():
    res = requests.get("https://zenquotes.io/api/random")
    jsond= json.loads(res.text)
    quote = jsond[0]['q']
    auth = (jsond[0]['a'])
    return quote, auth

# ---------------------------------------------------------------------------------------

# Use of youtubesearch module to fetch youtube results
def searchyt(song):
    music_name = song
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    return clip2


client = commands.Bot(command_prefix = 'j!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot ready")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server' )

import wikipedia 

@client.command()
async def wiki(ctx, *, cont):
    """Search Wikipedia"""
    try:
        results = wikipedia.summary(cont, sentences=2) 
        await ctx.send(results)
    except Exception:
        await ctx.send('Page not found')

import pyjokes

@client.command()
async def joke(ctx):
    '''Uhh..... get a joke?'''
    jk=pyjokes.get_joke(language='en', category= 'neutral')
    await ctx.send(jk)

@client.command()
async def lyrics(ctx, *, song):
    from lyrics_extractor import SongLyrics

    sc = SongLyrics('AIzaSyCBc9vGiM-q0dIOpt0mSIdhraUGiF1pU_U', '2c0e4a26e5d598f41')
    js = sc.get_lyrics(
        song
    )
    em = discord.Embed(title=js["title"], description=js["lyrics"], color=discord.Color.dark_blue())
    await ctx.send(embed=em)


@client.command()
async def addrole(ctx, member : discord.Member, role : discord.Role):
    print(role)
    await member.add_roles(role)


@client.command()
async def verify(ctx):
# Import the following modules
    from captcha.image import ImageCaptcha
    image = ImageCaptcha(width = 280, height = 90)
    captcha_text = str(random.randint(20000,30000))
    print(captcha_text)
    data = image.generate(captcha_text)  
    image.write(captcha_text, 'CAPTCHA.png')   
    img = discord.File("CAPTCHA.png")
    await ctx.send("Solve this Captcha:",file=img)
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    print(msg.content)
    if int(msg.content.lower()) == int(captcha_text):
        member = ctx.author
        role = ctx.guild.get_role(852462898931564544)
        print(str(role))
        await ctx.author.add_roles(role)
        await ctx.send(f"Hi there, Welcome to {ctx.guild.name}")
    else:
        await ctx.send("Verification Failed, try again!")

@client.command()
async def google(ctx, *, query):
    '''Search Google from here, not from Browser'''
    from googlesearch import search # pip install google, bs4
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        await ctx.send(j)

def getmeme(topic): # Topic/Subreddit name
    reddit = praw.Reddit(client_id=REDDIT_CID,
                    client_secret=REDDIT_SCT,
                    user_agent='meme') # Initializing details

    submission = reddit.subreddit(topic).random() #finding a random post in the given subreddit
    return submission.url

@client.command()
async def meme(ctx):
    await ctx.send(getmeme("memes"))

@client.command()
async def gif(ctx, *, cont):
    import TenGiphPy
    t = TenGiphPy.Tenor(token=TKEY)
    await ctx.send(t.random(cont))

@client.command(aliases=["hi"])
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}")

@client.command()
async def yay(ctx):
    await ctx.send(choice(yaym))

@client.command()
async def lol(ctx):
    await ctx.send(choice(lolm))
@client.command()
async def yes(ctx):
    await ctx.send(choice(yesm))
@client.command()
async def no(ctx):
    await ctx.send(choice(nom))
@client.command()
async def sus(ctx):
    await ctx.send(choice(susm))
@client.command()
async def damnson(ctx):
    await ctx.send(choice(dms))


@client.command()
async def quote(ctx):
    q, a = get_quote()
    em = discord.Embed(title=a+" once said", description=q, color=discord.Color.blue())
    await ctx.send(embed=em)

@client.command()
async def sendnudes(ctx):
    await ctx.send(client.user.avatar_url)

@client.command()
async def noobuntu(ctx):
    em = discord.Embed(description=f'Ubuntu Linux is a pretty hated distro and even loved one in the market, and it has few reasons for that \n\n**Canonical**\nThis is definitely the reason you should avoid Ubuntu, it\'s their parent company, Canonical. Canonical stopped the development of Unity and Ubuntu touch because of operating cost and low company profit. People loved both ‌products, so obviously some people are still mad at this. Because this was done for financial profit losses, if it was community held, we don\'t think this would hurt them anyway. It even has some very bad business practices in history\n\nhttps://www.quora.com/What-are-the-negative-aspects-of-Ubuntu?share=1\n\n Why not use distributions like Linux Mint and Zorin instead?\nhttps://itsfoss.com/linux-mint-vs-ubuntu/\nhttps://linuxhint.com/zorin_os_vs_ubuntu/', color = discord.Color.red())
    await ctx.send(embed=em)
import asyncio
@client.command()
async def whyarch(ctx):
    contents = ["**Why people love using Arch Linux?**\n\nArch Linux, a lightweight and flexible Linux® distribution that tries to Keep It Simple.", "**The DIY approach gives you the control over every aspect of your operating system**\n\nI have always found Arch Linux as a DIY (Do It Yourself) operating system. From installing to managing, Arch Linux lets you handle everything.\n\nYou decide which desktop environment to use, which components and services to install. This granular control gives you a minimal operating system to build upon with elements of your choice.\n\nIf you are a DIY enthusiast, you’ll love Arch Linux.", "**With Arch Linux, you get a better understanding of how Linux works**\n\nIf you ever tried to install Arch Linux, you know the complexity that comes with it.\n\nBut that complexity also means that you’ll be forced to learn things that you probably never bother to in other distributions.\n\nFor example, configuring network itself while installing Arch Linux is a good learning lesson.\n\nIf you start to get overwhelmed, Arch Wiki is there for you. It is the most extensive and awesome community-managed documentation on the internet. Just browsing through [Arch Wiki](https://wiki.archlinux.org) will teach you plenty of things.", """**Latest kernel and software with rolling release model**\n\nArch Linux is a rolling release distribution. That means new kernel and application versions are rolled out to you as soon as they are released.

While most other Linux distributions serve you old Linux kernel versions, Arch is quick to provide you the latest kernel.

The same goes for software. If a new version of software in the Arch repositories is released, Arch users get the new versions before other users most of the time.

Everything is fresh and cutting edge in the rolling release model. You don’t have to upgrade operating system from one version to another. Just use the pacman command and you always have the latest version.""", '''**AUR or Arch User Repository**\n\nArch Linux has plenty of software in its repository. The AUR extends the software offering of Arch Linux. You get a huge number of software with [AUR in Arch Linux.](https://aur.archlinux.org/)

AUR is the community driven approach to provide newer applications. You can search and install applications with the help of an [AUR helper](https://itsfoss.com/best-aur-helpers/) tool.''', '''**Sense of Accomplishment**\n\nAs James Clear mentions in his book Atomic Habits, ***human brain loves a challenge, but only if it is within an optimal zone of difficulty.***

Remember the feeling when you first installed any Linux distribution even if it was installing Linux Mint? That gave you a sense of achievement. You successfully installed Linux!

If you have been using Ubuntu or Fedora or other distribution for some time and you start to get comfortable (or bored), try installing Arch Linux.

For a moderately experienced Linux user, successfully installing Arch Linux itself gives a sense of accomplishment.

It is a challenge but an achievable one. If you suggest a new Linux user to try Arch Linux or even more complicated one like Linux From Scratch, the challenge would be too difficult to achieve.

This sense of successfully completing a challenge is also one of the reasons why people use Arch Linux.''', '''**No corporate involvement! Arch is created, supported and owned by community**\n\nUbuntu is backed by Canonical, Fedora is from Red Hat (part of IBM now) and openSUSE is from SUSE. All these major distributions are corporate backed.

This is not bad or crime in itself. But a few people do not like corporate involvement in open source projects.

Like Debian, Arch Linux is one of the rare few community-only Linux distribution projects.

You may point out that many other distributions like Linux Mint etc are also not sponsored by corporate. Well, that might be true but Linux Mint itself is based on Ubuntu and uses Ubuntu’s repositories. Arch Linux is not derivative of another distribution.

In that sense, Debian and Arch Linux are more pure community-driven projects. It may not matter to many people but a few people do care about such things.''', '''Lemme share a quick meme!''']
    pages = len(contents)
    cur_page = 1
    message = await ctx.send(embed=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue()))
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=10000, check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                if cur_page==8:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                    em.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2F9aj95rwqdex41.jpg&f=1&nofb=1")
                else:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                
                await message.edit(embed=em)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                if cur_page==8:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                    em.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2F9aj95rwqdex41.jpg&f=1&nofb=1")
                else:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                
                await message.edit(embed=em)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break

import cv2

def cartoonify(img):
  
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  gray = cv2.medianBlur(gray, 7) 
  edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
  # Making a Cartoon of the image
  color = cv2.bilateralFilter(img, 12, 250, 250) 
  cartoon = cv2.bitwise_and(color, color, mask=edges)
  cartoon_image = cv2.stylization(img, sigma_s=150, sigma_r=0.25)  
  return cartoon_image
import numpy as np
@client.command()
async def cartoon(ctx, member: discord.Member = None):
	if member is None:
		a = str(ctx.author.avatar_url_as(format="jpg"))

		req = requests.get(a).content

		arr = np.asarray(bytearray(req), dtype=np.uint8)

		img = cv2.imdecode(arr, -1)
		img = cv2.resize(img, (400, 400))
		cartoon = cartoonify(img)
		cv2.imwrite('cartoon.jpg', cartoon)
		

		file = discord.File("cartoon.jpg")

		embed = discord.Embed(title="Profile Picture : {}".format(
		    ctx.author.name),
		                      color=discord.Color.blue())
		embed.set_image(url="attachment://cartoon.jpg")

	else:
		a = str(member.avatar_url)
		req = requests.get(a).content

		arr = np.asarray(bytearray(req), dtype=np.uint8)

		img = cv2.imdecode(arr, -1)

		img = cv2.resize(img, (400, 400))
		cartoon = cartoonify(img)
		cv2.imwrite('cartoon.jpg', cartoon)
		
		file = discord.File("cartoon.jpg")

		embed = discord.Embed(title="Profile Picture : {}".format(
		    ctx.author.name),
		                      color=discord.Color.blue())
		embed.set_image(url="attachment://cartoon.jpg")

	await ctx.send(file=file, embed=embed)

@client.command()
async def removebg(ctx, member: discord.Member = None):
	if member is None:
		a = str(ctx.author.avatar_url_as(format="jpg"))

		req = requests.get(a).content

		arr = np.asarray(bytearray(req), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        img = cv2.resize(img, (400, 400))

        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': img},
            data={'size': 'auto'},
            headers={'X-Api-Key': RMKEY},
        )
        if response.status_code == requests.codes.ok:
            with open('no-bg.png', 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)

		file = discord.File("no-bg.jpg")

		embed = discord.Embed(title="Profile Picture : {}".format(
		    ctx.author.name),
		                      color=discord.Color.blue())
		embed.set_image(url="attachment://cartoon.jpg")

	else:
		a = str(member.avatar_url)
		req = requests.get(a).content

		arr = np.asarray(bytearray(req), dtype=np.uint8)

		img = cv2.imdecode(arr, -1)

		img = cv2.resize(img, (400, 400))
		cartoon = cartoonify(img)
		cv2.imwrite('cartoon.jpg', cartoon)
		
		file = discord.File("cartoon.jpg")

		embed = discord.Embed(title="Profile Picture : {}".format(
		    ctx.author.name),
		                      color=discord.Color.blue())
		embed.set_image(url="attachment://cartoon.jpg")

	await ctx.send(file=file, embed=embed)

@client.command()
async def donatecal(ctx):
    don = discord.Embed(title = "Support us for our work in Buymeacoffee", description="https://www.buymeacoffee.com/team.calinix")
    don.set_image(url="https://www.mockofun.com/wp-content/uploads/2020/05/buy-me-a-coffee-logo-6100.jpg")
    await ctx.send(embed=don)
@client.command()
async def archinstall(ctx):
    contents = ["So let's install Arch! It goes pretty simple if you have a guide with you, and I'm here to help you!\n\n**Why use Arch?**\n\nAs it's an awesome linux distribution basically for people to learn linux. It's fully community-maintained and DIY so you have a lot of freedom over your system. \n\nFor more info on why use arch, type `j!whyarch`", """Install the [Arch Linux ISO](https://archlinux.org/download/) from the [Archlinux website](https://archlinux.org/).\n\n**Direct Link for 64 bit machines:** [ArchLinux-64-bit_iso](http://mirror.rackspace.com/archlinux/iso/2021.08.01/archlinux-2021.08.01-x86_64.iso)
""", """Then make a bootable USB. To do this, I recommend [etcher](https://etcher.io), Its a simple software to make USB bootable. After downloading and opening etcher, Select your disk file (the ISO), your USB Device and click on `Flash!`. You USB will become bootable soon.""", '''Now shut down your machine and start it. When you see your logo, quickly enter the BIOS (You can reach it by spamming a Function key or Esc. Mostly it's Esc.)\n\n**Common BIOS Keys**:\nASRock: F2 or DEL
ASUS: F2 for all PCs, F2 or DEL for Motherboards
Acer: F2 or DEL
Dell: F2 or F12
ECS: DEL
Gigabyte / Aorus: F2 or DEL
HP: F10
Lenovo (Consumer Laptops): F2 or Fn + F2
Lenovo (Desktops): F1
Lenovo (ThinkPads): Enter then F1.
MSI: DEL for motherboards and PCs
Microsoft Surface Tablets: Press and hold volume up button.
Origin PC: F2
Samsung: F2
Toshiba: F2
Zotac: DEL
You will see a boot tab (some have a seperate boot menu, check Esc key for that), where you can choose your boot options. CHoose your USB device there and boot through it. The boot will start, and some text will appear. Then finally a shell with `Welcome to Arch Linux` message will appear''', """First, Check if your system is [UEFI](https://uefi.org). If it's not UEFI, You should consider going the `j!archinstallbios` method instead of this. \n\nTo check if you are on UEFI, run `ls /sys/firmware/efi/efivars` in the terminal. If some output appears, your computer is UEFI, else BIOS""", '''Set Keyboard Layout
The default keyboard layout is US so if you want to use US keyboard layout then you can skip this step. You can check available layouts using this command:

```
ls /usr/share/kbd/keymaps/**/*.map.gz
```

and to modify the layout you can use loadkeys. For example, to set a german keyboard layout you can do

```
loadkeys de-latin1
```''', '''**Check your Internet**:\n\nAt the time of writing this guide, the installation ISO using IWD (Internet Wireless Daemon) to connect to wifi. You can check if you have internet connection or not by doing this

```ping google.com #or any website you like stallman.org (pretty great one)```

If there’s no internet connection, you can do:

- If you’re using ethernet, plug in the cable.
- If you’re using wifi, you can use iwctl (IWD command).

Here’s the basic command after you use iwctl (don’t forget to press enter to execute the command):

```
device list #to check the device name
station <device-name> scan #to scan the wifi
station <device-name> get-networks #to check the available networks
station <device-name> connect <wifi-name> #and then enter the password if there's any
exit #exit iwctl
```
After that check again using the ping command. You should be connected!''', '''**Update The System Clock**
After there’s an internet connection, you can update the system clock by using

```
timedatectcl set-ntp true
```
to check the service status, use `timedatectl status`''', '''**Partition Drive**\n\nTo check the disks that available, you can use `lsblk` command and pick which disk you want to install arch linux on. The disk start with `sd` and without a number at the end like `sda`

For the disk partitions, i use `cfdisk` command. For example, `cfdisk /dev/sda` (replace sda with the disk you want to use.).


The first partition is bootloader, usually around 512M (M means megabytes) depends on what bootloader you want to use. And then change the partition type to EFI System.

The second partition is swap partition, which you may want to use as VRAM or virtual RAM. Basically RAM alloted to your harddisk. Ideal size is 4-6G (G for gigabytes). Change Type to Linux Swap

The third partition is root directory. I use everything that’s left but you can spare some for another partition. And then change the partition type to Linux Filesystem.

After you’re sure about your disk partitions, then write the changes and then quit.''','''**Format The Partitions**

The next step is format the disk partition. For bootloader (1st one) partition, format it to FAT32 by using this command

```
mkfs.fat -F32 /dev/<efi-system-partition> #replace <efi-system-partition> with your bootloader partition (like sda1)
```

For root directory, format it to `ext4` by using this command

```
mkfs.ext4 /dev/<root-partition> #replace <root-partition> with your root partition (like sda3)
```

For swap partition:

```
mkswap /dev/<swap-partition>
swapon /dev/<swap-partition>
```

For example:

```
mkfs.fat -F32 /dev/sda1
mkswap /dev/sda2
swapon /dev/sda2
mkfs.ext4 /dev/sda3
```
''', '''**Mount The Filesystems**
The next step is mount the partition that we’ve made. First, mount root partition to /mnt using this command

```
mount /dev/<root-partition> /mnt
```

after that create two directories, /mnt/boot and /mnt/boot/efi (basically create efi directory inside boot directory which both of them doesn’t exist so you need to create one by one). You can create both directories using this command

```
mkdir -p /mnt/boot
mkdir -p /mnt/boot/efi
```

After that mount your bootloader to /mnt/boot/efi using this command

```
mount /dev/<efi-system-partition> /mnt/boot/efi
```

For example:

```
mount /dev/sda2 /mnt
mount /dev/sda1 /mnt/boot/efi
```''', '''**Install Essential Packages**

You can install essential package by using this command

```
pacstrap /mnt base base-devel linux linux-firmware vim
```

- `/mnt` is where you mount your root partition.
- `base` is base packages.
- `base-devel` is development tool such as `sudo` and `grep`.
- `linux` is the kernel.
- `linux-firmware` is the necessary part of linux kernel.
- `nano` is the text editor (I don’t use Vim here for keeping this beginner-friendly).
''', '''**Generate FStab**\n\nFstab is for telling the kernel what to load in the booting process.

To generate fstab use this command

```
genfstab -U /mnt >> /mnt/etc/fstab
```''','''**Change Root Into New System**

To take a look inside our new system, we can change root to our new system by using this command

```
arch-chroot /mnt
```''', '''That's basically done installing Arch! But main thing is to configure it, so let's Check it out too!''', '''**Setting Timezone**\n\nTo set the time zone, we can use this command

```
ln -sf /usr/share/zoneinfo/Region/City /etc/localtime
```

For example:

```
ln -sf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
```
You can check the region or the city by doing this

`ls /usr/share/zoneinfo/Region`

and

`ls /usr/share/zoneinfo/Region/City`

or just double click `<tab>` key while typing `ln -sf /usr/share/zoneinfo/`

After that, generate the clock using hwclock with this command

`hwclock --systohc`
''', '''**Select the OS language**\n\nFirst, you need to edit `etc/locale.gen` using your favorite text editor (which is not `nano` for me) and uncomment the language you want.

For example, you want to use US English as your OS language then what you need to uncomment is `en_US.UTF-8 UTF-8` and `en_US ISO-8859-1.`

After that, use this command to generate locales

`locale-gen ` 

and then create the locale.conf file. For example:

```
nano /etc/locale.conf #you can replace nano with your favorite text editor
```

the content of `locale.conf` is

```
LANG=en_US.UTF-8 #if you choose US English
```

If you set the keyboard layout (at the beginning of installation), then you make the changes persistent in `vconsole.conf`. For example:

```
nano /etc/vconsole.conf
```

with the content

```
KEYMAP=de-latin1
```
''', '''**Network Configuration**
For the network configuration, create the hostname file with the name you want (it’s not the user name, it’s more like your machine name). 

For example:

`nano /etc/hostname`

with the content

```
bruhtus
```
After that, add this content to `/etc/hosts`

```
127.0.0.1	localhost
::1			localhost
127.0.1.1	<yourhostname>.localdomain	<yourhostname>
```

For example:
The previous step i define my hostname as bruhtus, so what i need to do is add this content to `/etc/hosts`

```
127.0.0.1	localhost
::1			localhost
127.0.1.1	bruhtus.localdomain	bruhtus
```
If the system has a permanent IP address, it should be used instead of 127.0.1.1.

After that, install network manager using this command `pacman -S networkmanager wpa_supplicant` and then activate on startup using  `systemctl enable NetworkManager` and `systemctl enable wpa_supplicant`.
''', '''**Set The Root Password**

To set the root (or admin) password, use this command

`passwd`

and then enter your password.

**Add New User**

The default user is only root (or admin).

To create new user, use this command

```
useradd -m <username>
```
after that create the password for that username by using this command

`passwd <username>`
and then enter your password.

For example:

```
useradd -m bruhtus #i like my hostname and my username to be the same
passwd bruhtus
```
and then enter the password''', '''**Add New User To Group**
It’s so that the new user can have root access using sudo

To add new user to group, we can use this command

`usermod -aG wheel,audio,video,optical,storage <username>`
''','''
**Edit Sudoers File**
Add the wheel group to have root access with sudo

Use `visudo` and look for wheel and then uncomment those line.

The line would be like this

```
%wheel ALL=(ALL) ALL
```
By default, `visudo` using `vi` to edit the file. If you didn’t want to use `vi` then you can do

```
EDITOR=nano visudo
```''', '''**Install Bootloader**
> In my case, i use grub as the bootloader. So, i’m just gonna cover grub installation in this section.

First, install the bootloader and efibootmgr, and some other tools using this command

```
pacman -S efibootmgr os-prober dosfstools mtools grub 
grub-mkconfig -o /boot/grub/grub.cfg
```
After that, use this command to install grub on system partition

```
grub-install --target=x86_64-efi --efi-directory=/boot/efi/  --bootloader-id=grub_uefi --recheck
```

If there’s no error, then generate grub config using this command

`grub-mkconfig -o /boot/grub/grub.cfg`''', '''**Reboot**
If there’s no error, exit from chroot using `exit` command. After that, unmount the system using `umount -R /mnt` and then reboot (please make sure the disk partition is priority in bios).''', '''**CONGRATULATIONS! You have completed the Arch Installation!**

You have successfully installed Arch Linux on your system

**If you are wondering why you are booting into a text based interface, it is cuz Arch gives you a base system. To get GUI and all. and to make the desktop perfect, check out [this guide](https://itsfoss.com/things-to-do-after-installing-arch-linux/)**''']
    pages = len(contents)
    cur_page = 1
    em=discord.Embed(title='Arch Linux Installation Guide',description=f"Step {cur_page}/{pages}:\n{contents[cur_page-1]}", color=discord.Color.blue())
    if cur_page==1:
        em.set_image(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.ostechnix.com%2Fwp-content%2Fuploads%2F2016%2F02%2FArch-linux-logo.png&f=1&nofb=1")
    else:
        pass
    message = await ctx.send(embed=em)
   # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=10000, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                em=discord.Embed(title='Arch Linux Installation Guide',description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                if cur_page==1:
                    em.set_image(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.ostechnix.com%2Fwp-content%2Fuploads%2F2016%2F02%2FArch-linux-logo.png&f=1&nofb=1")
                else:
                    pass
                await message.edit(embed=em)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                em=discord.Embed(title='Arch Linux Installation Guide',description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                if cur_page==1:
                    em.set_image(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.ostechnix.com%2Fwp-content%2Fuploads%2F2016%2F02%2FArch-linux-logo.png&f=1&nofb=1")
                else:
                    pass
                
                await message.edit(embed=em)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
         
@client.command()
async def whymanjaro(ctx):
    contents = ['''Everyone who uses Linux has heard of the big names like Ubuntu, Debian, Arch, and Mint. Few people know about smaller distros like [Manjaro](https://manjaro.org/). Those people don’t know what they are missing. The article will explain ‘why I use Manjaro and you should too’.

I’ve always been interested in computers and the early history of computers. A couple years ago, I bought an older HP tower to learn about Linux. Now, I’m on my second Linux laptop. I’ve tried quite a few distros, including several Ubuntu flavors, Linux Mint, Fedora, OpenSUSE, and Debian. I installed Manjaro three years ago and haven’t looked back.''', '''**Arch without Hassle**

Manjaro is one of the few [Linux distributions that are not based on Ubuntu](https://itsfoss.com/non-ubuntu-beginner-linux/). Instead, it is built on the continually cutting edge [Arch Linux](https://www.archlinux.org/). Arch is a great distro, but unfortunately, if you want to install it you have to do a lot of work. You start off with a base system and you have to install and setup everything yourself. This can be a real pain if you just want to give Arch a spin or you’re new to Linux.

Manjaro takes all of the hassle out of installing Arch. Like most distros, all you have to do is download the ISO file, write it to a thumb drive, and install it. The Calamares installer gives you a smooth experience similar to Ubuntu’s Ubiquity installer.''', '''**Great Hardware Support**

When installing Linux, it can be a pain to get all the hardware working. When you install Manjaro, it scans the system and installs the required drivers. On one of my computers, I have an old Broadcom wireless card. Every time I install a new distro, I have to go through some extra steps to get that Broadcom chip working. When I install Manjaro, it works out of the box.''', '''**Great Hardware Support**

When installing Linux distros like Ubuntu, Fedora etc, it can be a pain to get all the hardware working. When you install Manjaro, it scans the system and installs the required drivers. On one of my computers, I have an old Broadcom wireless card. Every time I install a new distro, I have to go through some extra steps to get that Broadcom chip working. When I install Manjaro, it works out of the box.''', '''**Don’t Have to Worry About PPAs**

Before I switched to Manjaro, I used both Lubuntu and Linux Mint. The one thing that really bugged me was having to deal with PPAs (Personal Package Archive). Basically, a PPA is a repo for just a single application or a small group of applications. For those who never had to deal with this, allow me to explain.

Every time I wanted to install a piece of software that was not in the offIcial Ubuntu repos, I had to link a new PPA to my system via the terminal. Once it was linked and I had run `sudo apt-get update`, then the program was available for installation.

While adding the PPA doesn’t take a lot of time, it is a pain. When I upgraded from one version of Linux Mint to another I has a hell of a time getting the PPA I used switched over. If you use a lot of PPAs, it can quickly become a rat’s nest.

Then there’s the security aspect. There have been several times in the past when people have gotten a hold of [old and unused PPAs](https://itsfoss.com/how-to-remove-or-delete-ppas-quick-tip/) and used them to push out malware.

Since Manjaro uses Arch as a base instead of Ubuntu, it doesn’t support PPAs. Instead, you have access to the Arch User Repository. for more info, read on.''', '''**Tons of Software**

Just because Manjaro doesn’t have PPAs, don’t think that it lacks in software. The Manjaro team maintains a large software repository. Beyond that, Manjaro users also have access to the [Arch User Repository](https://aur.archlinux.org/). The AUR is made up of user created scripts to install applications not packaged for Arch (or in this case Manjaro). Quite a few of the applications in the AUR were either originally packaged for Ubuntu or are pulled directly from Github. The scripts in the AUR then modify the `.deb` files, so that they can be installed on Manjaro.

There are downsides to using the AUR. Sometimes the dependencies required by and AUR packages conflict with something already installed. You can also run into broken and out-of-date packages. But I’ve had very few problems, so far.
''', '''**Latest and Greatest without Killing Your System**

One of the problems that Arch users often have, because it is a rolling release, a new package will be released and it will break their system. The Manjaro team works to avoid that by testing new packages before making them available to users. While this might make Manjaro slightly less than bleeding edge, it also ensures that you’ll get new packages a lot sooner than distros with scheduled releases like Ubuntu and Fedora. I think that makes Manjaro a good choice to be a production machine because you have a reduced risk of downtime.
''', '''**Switching Kernels is Easy**

In order to switch kernels on most distros, you have to use some terminal wizardry. Manjaro has a nice little application that allows you to install as many kernels as you want. This is handy if you have an older laptop and it doesn’t like a new kernel. In my case, I have an HP laptop that slows way down when you use a kernel newer than 4.4. and switching kernels was just a couple of clicks away.''', '''**Friendly Community**

There are a number of distro communities (including Arch) that are known for not being very noob friendly. The same is not true for Manjaro. The [official Manjaro forum](https://forum.manjaro.org/) is a great place for new people to find help. They also have forums available in over 29 languages for non-English speakers''', '''Lemme share a quick meme!''']
    pages = len(contents)
    cur_page = 1
    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.green())
    em.set_image(url='https://manjaro.org/img/logo.svg')
    message = await ctx.send(embed=em)
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=10000, check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                if cur_page==8:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.green())
                    em.set_image(url="")
                else:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.green())
                
                await message.edit(embed=em)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                if cur_page==8:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                    em.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2F9aj95rwqdex41.jpg&f=1&nofb=1")
                else:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                
                await message.edit(embed=em)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break

@client.command()
async def whyfedora(ctx):
    contents = ['''**Fedora is Bleeding Edge**
The Fedora Operating System is called a bleeding edge Linux distribution because it is always rolling out with the latest software, driver updates, and Linux features. This contributes to the reason why you can confidently use Fedora as soon as installation is complete – it ships with the latest stable kernel along with all its benefits.

For example, Fedora is the first major distribution to use systemd as its default init system and the first major distro to use Wayland as its default display server protocol.''', '''**A Good Community**
Fedora has one of the biggest communities in the world with a forum populated by many users who will happily help you sort out any issues that might have you stuck while using the distro.

This is separate from the Fedora IRC channel and the large Reddit community which you can also access for free to learn from other users and share experiences.''', '''**Better Package Management**
Unlike Debian and Ubuntu which use dpkg with an apt official front-end, Fedora uses RPM package manager with a dnf front-end and RPM packages are typically easier to build. RPM also has more features than dpkg such as confirmation of installed packages, history and rollback, etc.''', '''**A Unique Gnome Experience**
The Fedora project works closely with the Gnome Foundation thus Fedora always gets the latest Gnome Shell release and its users begin to enjoy its newest features and integration’s before users of other distros do.''', '''**Top-Level Security**
Linux users enjoy top good security thanks to the Linux kernel underlying every distro but Fedora developers have gone further to embed advanced security features within the distro via the Security-Enhanced Linux (SELinux) module.

SELinux is a Linux kernel security module that enables support for accessing security policies e.g. managing permission rights. You can read more about SELinux here.''', '''**Prolific Hardware Support**
Fedora enjoys many benefits thanks to the communities backing it and a good example is how readily Fedora will work on PCs, with printers, scanners, cameras, etc. from different vendors straight out of the box. If you want a Linux distro that wouldn’t give you any compatibility headaches then Fedora is a good choice.''', '''**Fedora is Easy to Use**
The most common Linux distros are well-known for their ease of use and Fedora is among the easiest distributions to use. Its simple User Interface is simple enough for anyone to boot up for the first time and get used to after a couple of clicks and all of its software offer the same User Experience which gives users a feeling of consistency and familiarity.''', '''Memetime!''']
    pages = len(contents)
    cur_page = 1
    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
    message = await ctx.send(embed=em)
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=10000, check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                if cur_page==8:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                    em.set_image(url="https://i.pinimg.com/originals/b5/5d/53/b55d538e6641ecd14e560377e97e0e2e.jpg")
                    em.set_footer(text="Source: ItsFoss")
                else:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                
                await message.edit(embed=em)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                if cur_page==8:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                    em.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2F9aj95rwqdex41.jpg&f=1&nofb=1")
                else:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                
                await message.edit(embed=em)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break

# @client.command()
# async def roleselect():

@client.command()
async def poll(ctx, opt1, opt2, *, message):
    em = discord.Embed(title=message, description=f"{ctx.author.name} asks\n\n1. {opt1}\n2. {opt2}", color=discord.Color.blue())
    msg = await ctx.send(embed=em);
    await msg.add_reaction("1️⃣")
    await msg.add_reaction("2️⃣")

@client.command()
async def yt(ctx, *, url):
    await ctx.send(searchyt(url))

@client.command()
async def aur(ctx, term):
    rs = aur.search(term)
    await ctx.send(rs)

import pyjokes


@client.command()
async def getinv(ctx):
    invite = ctx.channel.create_invite()
    await ctx.send(f"Here's your invite:\n {invite}")

@client.command()
async def ping(ctx, num:int, user:discord.Member):
        i=0
        if num>20:
            await ctx.send("Ugh man it's enough!")
        else:
            while i<num:
                await ctx.send(user.mention)
                i+=1

@client.command()
async def gayrate(ctx, user:discord.Member):
    pr= random.randint(1, 100)
    em = discord.Embed(description=f"{user.name} is {pr}% gay\n:rainbow_flag: :thinking:", color=discord.Color.red())
    await ctx.send(embed=em)

# @client.command()
# async def google(ctx, *, query):
#     from googlesearch import search
#     for j in search(query, tld="co.in", num=1, stop=1, pause=2):
#         await ctx.send(j)


client.remove_command('help')
exts=['music']

for i in exts:
    client.load_extension(i)
import help
cogs=[help]

for i in range(len(cogs)):
  cogs[i].setup(client)
import help
cogs=[help]

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

@client.command(aliases=['chat'])
async def c(ctx, *, cont):
    from prsaw import RandomStuff # pip install prsaw
    rs = RandomStuff(async_mode=True,api_key=os.getenv("cbapi"))
    res = await rs.get_ai_response(cont);
    await rs.close()
    await ctx.send(res[0]["message"])

@client.command()
async def ban(ctx, un: discord.Member, *, reason):
    await un.ban(reason=reason)
    print(f"{un} was banned!")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason: str):
  if not reason:
    await user.kick()
    await ctx.send(f"**{user}** has been kicked for **no reason**.")
  else:
    await user.kick(reason=reason)
    await ctx.send(f"**{user}** has been kicked for **{reason}**.")
keep_alive()
import os
client.run(os.getenv("tk"))
