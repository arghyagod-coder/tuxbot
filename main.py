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
import numpy as np
from big_statements import *

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
    contents = why_arch
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
    contents = arch_install
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
    contents = why_manjaro
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
    contents = why_fedora
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
async def mkdir(ctx,*,category_name):
    await ctx.guild.create_category(category_name)
    await ctx.send(
        embed=discord.Embed(
            title="Done",
            description="Created a new category",
            color=discord.Color.dark_blue(),
            thumbnail=client.user.avatar_url_as(format="png")
            )
        )

@client.command()
async def mv(ctx, *, a):
    f, t = a.split('"')[1::2]
    fl, tl = f.split("/")[1].strip(), t.split("/")[1].strip()
    fc, tc = f.split("/")[3].strip(), t.split("/")[3].strip()
    if (not discord.utils.get(ctx.guild.categories, name=fl)) or not discord.utils.get(ctx.guild.channels,name=fc):
        await ctx.send(embed=discord.Embed(
            tile="Error",
            description=f"mv: cannot stat {f}: No such channel or category",
            color=discord.Color.dark_blue(),
            thumbnail=client.user.avatar_url_as(format="png")
            ))
        pass
    if not discord.utils.get(ctx.guild.categories, name=tl):
        await ctx.send(
            embed=discord.Embed(
                title="Error",
                description=f"mv: cannot move '{f}' to '{t}': No such channel or category",
                color=discord.Color.dark_blue(),
                thumbnail=client.user.avatar_url_as(format="png")
                )
            )
        pass
    
    
    
    

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
