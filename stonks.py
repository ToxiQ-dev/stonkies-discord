import discord
import json
import random
from discord.ext import commands, tasks
from itertools import cycle
import os
import logging



logging.basicConfig(level=logging.INFO)



logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#prefixes
stonks = commands.Bot(command_prefix = ['~', 'stonks ', 'skeet ', 'tofee ', 'darling ', '002 ', 's!', 's1', 's2'])
status = cycle([f'with {stonks.guilds} servers', '~help'])
stonks.remove_command('help')



pog = "NzY1MjcwOTg5NTU3NzI3MjM0.X4SYJQ.iR1ik6oqvjLPRCaP7aTMwU5GhnU"
# normal code
@stonks.event
async def on_ready():
    change_status.start()
    print('pp small')






@tasks.loop(seconds=60)
async def change_status():
  await stonks.change_presence(activity=discord.Game(next(status)))


@stonks.command()
async def ping(ctx):
  await ctx.send(f'why does it matter? `{round(stonks.latency * 1000)}ms` :/')


@stonks.command()
async def embedtest(ctx):
  test_embed = discord.Embed(title="test", color=0x000000)
  test_embed.description = """I am an embed!"""
  await ctx.send(embed=test_embed)


@stonks.command()
async def help(ctx):
  # og
  help_embed = discord.Embed(title=" ", color=0x49fc03, timestamp=ctx.message.created_at)

  help_embed.description = """Stonkies\' prefixes are `~`, `stonks`, `skeet`, `tofee`, `darling`, `002`, `s1`, `s2`, and `s!`, you can use `~prefix` to see them in a line"""
  # commands
  help_embed.add_field(name="Commands", value="""``~help``- sends this embed
  ``~ping``- latency test
  ``~randomnumber``- gives u a random number from 1-100 we might make a higher capacity idk
  ``~credits``- credits, uhh yea
  ``~info <@user>``- user info yuh
  ``~veryspotify``- very spotify kek
  ``~qotd``- qotd
  ``~news``- news""")
  # support
  help_embed.add_field(name="Support", value="""``~suggest``- sends u inv to server to suggest something
    ``~botto``- just support botto alr
    ``~invite``- just invite me loser
    ``~supportserver``- just join the support server loser
    ``~TeachMyProgrammer``- pls teach him
    `~darling`- some stuff.""")
    # fun
  help_embed.add_field(name="Fun", value="""``~8ball``- 8ball, ofc
    ``~inspirationalspeech``- it really inst an inspirational speech but we can still keep it
    ``~diarrhea``- some stuff, very funni
    ``~doggy``-roleplay doggy
    ``~ismellpennies``- gives u a random msg about pennies.
    ``~ritual``- why did u do it tofee
    ``~nomoresayingcusswords``- NO MORE GUYS! IT IS NOT GOOD
    ``~kill <@user>``- shoot him again timmy **pulls out shotgun**
    ``~introduction``- e
    ``~roast``- wow very epic
    ``~truth``- truth""")
    # exclusive
  help_embed.add_field(name="Server", value="""``~epicinfo``- epic points for alexpooo#1378 server unless u want to add the system
  ``~ping``- test
  ``~embedtest``- test""")
  # messages
  help_embed.add_field(name="Messages", value="""``~say <message>``- sends a message
  ``~bold <message>``- sends a bold message
  ``~spoiler <message>``- sends a spoiler message
  ``~italic``- sends italic message
  ``~italicbold``- sends italic and bold message
  ``~cross``- sends cross message idk what its called
  ``~crossbold``- cross bold :smiley:
  ``~idk``- e
  ``~bully me``- wow bully""")
  help_embed.add_field(name="Economy", value="CHILL IM STILL WORKING ON IT")
  help_embed.add_field(name="Nationality Crap", value="""`~flag <abb.>`- flag of a thing or wutever, it ees wut it ees.""")
  await ctx.send(embed=help_embed)





@stonks.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = ["Sure ig",
              "Hey karen! Put on your mask and ask again later!",
              "Get out of here trash",
              "dame da ne dame yo dame no yo",
              "Did you know that this will never happen?",
              "Don\'t ask me, ask ur mother",
              "Mom! Some random kid is asking me some random question!",
              "Leave me alone, I just wanna sleep",
              "Stonkies isn\'t home",
              "Ask ur father kid",
              "I hate children",
              "Yes, ofc",
              "This is the only time I\'m saying yes to a karen, this better be worth it",
              "Hazy PP",
              "Yea sure now leave me alone",
              "Yes, and no",
              "yea sure now let me go back to bed",
              "Yessir!",
              "For sure",
              "Just find out yourself.",
              "That wont happen Gold Digger",]
  await ctx.send(f'{random.choice(responses)}')





@stonks.command()
async def inspirationalspeech(ctx):
    responces = ["Poggers",
                "Dont sub to Cocomelon",
                "WeirdChamp",
                "KEKW",
                "PP small",
                "Dont listen to that vegan teacher",
                "Eating animals rocks, karen, eating animals rocks, karen, share this song and stop abusing ur dog and ppl that have mental issues so they cant go vegan!",
                "stfu karen"]
    await ctx.send(f'{random.choice(responces)}')



@stonks.command()
async def suggest(ctx):
    suggest_embed = discord.Embed(title="Suggest something!")
    suggest_embed.url = "https://discord.gg/w4v3bNU"
    suggest_embed.description = """Join my support server, and go to the <#772850480379723807> channel to suggest something! Join it now."""
    await ctx.send(embed=suggest_embed)

@stonks.command()
async def diarrhea(ctx):
  await ctx.send(f'Diarrhea is loose, watery stools (bowel movements). You have diarrhea if you have loose stools three or more times in one day. Acute diarrhea is diarrhea that lasts a short time. It is a common problem. It usually lasts about one or two days, but it may last longer.')

@stonks.command()
async def doggy(ctx):
  answers = ["***happy doggy noises***",
             "***sad doggy noises***",
             "***wags tail***",
             "***licks ur mother and father and gf***",
             "***licks u***"]
  await ctx.send(f'{random.choice(answers)}')

@stonks.command()
async def randomnumber(ctx):
  number_embed = discord.Embed(title="Random Number Generator", description=(random.randint(1, 100)), color=0xF85252)
  await ctx.send(embed=number_embed)

@stonks.command()
async def say(ctx, *, question):
  await ctx.send(f'{question}')

@stonks.command()
async def snipe(ctx):
  snipe_embed = discord.Embed(title='snipe', color = 0x000000)
  snipe_embed.description = """give me a break, at least sus tried"""
  await ctx.send(embed=snipe_embed)

@stonks.command()
async def ismellpennies(ctx):
  pennies = ["eh, just 1 cent",
            "same.",
            "prob just the dog\'s poop, dont mind it",
            "i wish i was an embed."]
  await ctx.send(f'{random.choice(pennies)}')


@stonks.event
async def on_command_error(ctx, error):
  pass



@stonks.command()
async def ritual(ctx):
  ritual_embed = discord.Embed(title='Very Ritual')
  ritual_embed.description = """Tofee broke the ritual :sob:"""
  await ctx.send(embed=ritual_embed)

@stonks.command()
async def pp(ctx):
  peepees = ["small", "big"]
  await ctx.send(f'{random.choice(peepees)}')

@stonks.command()
async def info(ctx, member: discord.Member):

  


  if member == None:
    member == ctx.author
  roles = [role for role in member.roles]

  user_embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

  user_embed.set_author(name=f"User Info = {member}")
  user_embed.set_thumbnail(url=member.avatar_url)
  user_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  user_embed.add_field(name="ID", value=member.id)
  user_embed.add_field(name="Name", value=member.display_name)

  user_embed.add_field(name="Created at:", value=member.created_at)
  user_embed.add_field(name="Joined at:", value=member.joined_at)

  user_embed.add_field(name="Roles:", value=" ".join([role.mention for role in roles]))
  user_embed.add_field(name="Top role:", value=member.top_role.mention)

  user_embed.add_field(name="Bot", value=member.bot)


  await ctx.send(embed=user_embed)


@stonks.command()
async def nomoresayingcusswords(ctx):
  await ctx.send(f"No. More. Saying. Cuss words! It. Is. Not. Good. I'm putting a video on YouTube about no more saying cuss words. No more saying cuss words guys! It's inappropriate and violent! If you say a cuss word then you're like, going to jail, and you're like, and when you go to jail, i- ba- when you go to jail, if you say, if you say a cuss word you go to jail and if you go to jail cause you said a cuss word, then... You're only gonna eat BROCCOLI and OTHER VEGETABLES for your WHOLE LIFE. You don't want to eat vegetables. Sometimes people like eating sweets but, I eat broccoli. So, I'm okay with broccoli but I do not want to go to jail. You can not go to jail. And saying cuss words is ILLEGAL. They are now gonna make a law about that. It is illegal, it is inappropriate, it is really violent. I better warn my school about that.")

@stonks.command()
async def epicinfo(ctx):
  epic_info = discord.Embed(title="Embed Info")
  epic_info.description = """Today\'s phrase is HI!
  :arrow_right: https://docs.google.com/document/d/13UKNcck9-DgNGzHopvSeftD8CatXegtBYCMaNy_jIXI/edit# :arrow_left:"""
  await ctx.send(embed=epic_info)

@stonks.command()
async def kill(ctx):
  await ctx.send(f"use a different bot, i dont kill innocent ppl")

@stonks.command()
async def bold(ctx, *, question):
  await ctx.send(f'**{question}**')

@stonks.command()
async def spoiler(ctx, *, question):
  await ctx.send(f'|| {question} ||')

@stonks.command()
async def italic(ctx, *, question):
  await ctx.send(f'*{question}*')

@stonks.command()
async def italicbold(ctx, *, question):
  await ctx.send(f'***{question}***')

@stonks.command()
async def cross(ctx, *, question):
  await ctx.send(f"~~{question}~~")

@stonks.command()
async def prefixes(ctx):
  prefixes_embed = discord.Embed(title="Stonkie\'s prefixes")
  prefixes_embed.description = """``~``
  ``stonks``
  ``skeet``
  ``tofee``
  ``darling``
  ``002``
  ``s!``
  ``s1``
  ``s2``"""
  await ctx.send(embed=prefixes_embed)

@stonks.command()
async def botto(ctx):
  advertise_embed = discord.Embed(title="Support Botto and Tofee!")
  advertise_embed.url = "https://discordbotlist.com/bots/botto"
  advertise_embed.add_field(name="Join his support server!", value="https://discord.gg/YrSdqr5zUy")
  advertise_embed.description = """I made this command to support Tofee#1331, he helped me to reach this accomplishment, use the ~credits command for more info"""
  await ctx.send(embed=advertise_embed)

@stonks.command()
async def crossbold(ctx, *, question):
  await ctx.send(f"**~~{question}~~**")

@stonks.command()
async def idk(ctx):
  await ctx.send(f"and idk what u dont understand")

@stonks.command()
async def introduction(ctx):
  intro_embed = discord.Embed(title="Introduction")
  intro_embed.description = """**Stonkies** is a bot made by Darling#0002, and he started on the 12th of October, 2020
  **Stonkies** favorite anime is Darling in The FranXX.
  **Stonkies** favorite person is Tofee#1331
  **Stonkies** favorite bot is Botto
  **Stonkies** Programmer is Darling#0202
  **Stonkies** wants to be hokage
  **Stonkies** says E
  **Stonkies** says hokage dattebayo
  **Stonkies** says hokage dattebayo again
  **Stonkies** says hello"""
  await ctx.send(embed=intro_embed)

@stonks.command()
async def veryroast(ctx):
  roasts = ["If someone says ur gay, say that ur straighter than the pole their mum dances on",
            "If someone says that they kissed your gf, say that u got u got ur first kiss, if they say ur mum dosent count, say yeah, but urs does"]
  await ctx.send(f'{random.choice(roasts)}')


@stonks.command()
async def veryspotify(ctx):
  await ctx.send(f'https://open.spotify.com/playlist/4w7Fq6WfhrgaQNGCgcPZVV?si=NBCtew0-Tu-2EI1bN9Xkiw')


@stonks.command()
async def qotd(ctx):
  qotd_embed = discord.Embed(title="qotd")
  qotd_embed.description = """Why does ThatVeganTeacher say she dosent abuse animals after she made a dog
  go vegan?"""
  qotd_embed.add_field(name="Answer", value="use `~answer` to submit an answer")
  await ctx.send(embed=qotd_embed)

@stonks.command()
async def answer(ctx, *, question):
  await ctx.send(f'{question} is a user\'s answer idk how to code it sorry')

@stonks.command()
async def news(ctx):
  news_embed = discord.Embed(title="newssss")
  news_embed.description = """My programmer is using the discord.py documentation for the first time!"""
  await ctx.send(embed=news_embed)

@stonks.command()
async def bully(ctx, me):
  bully = ["haha get noobed",
           "u suck booty butt"]
  if me == "me":
    await ctx.send(f'{random.choice(bully)}')


@stonks.command()
async def invite(ctx):
  invite_embed = discord.Embed(title="invite me!")
  invite_embed.description = """Hello there! You tired of bots that are only made for moderation? Is your server full of moderation bots?
  And dosen\'t have any fun bots? **Stonkies** is just for you! **Stonkies** was made by `Darling#0202` with help from `Tofee#1331`
  `Darling#0202` is 13, while `Tofee#1331` is 14. **Stonkies** started off as a discord.js bot, but it went through problems
  so I had to move to Python. I hope you have fun with it! And stay safe!1"""
  invite_embed.url = "https://discordbotlist.com/bots/stonkies"
  await ctx.send(embed=invite_embed)

@stonks.command()
async def supportserver(ctx):
  server_embed = discord.Embed(title="Join my support server!")
  server_embed.description = """helo. do you want a good server m8? my support server is exactly wut u need!
  it has a bunch of crap from coding, to anime, to uhhh crap! go join now or u wont get tteokbokki!"""
  server_embed.url = "https://discord.com/invite/MMChUH6HjT"
  await ctx.send(embed=server_embed)


@stonks.command()
async def dream(ctx, something):
  if something == "speedrun":
    await ctx.send("""3 of my friends will be beating me up
    will they win or will they lose? minecraft manhunt!
    ohhhh dreammmmmmmmmmmmm
    ohh dreamy boiiii
    oh dreammm
    WHAT
    YOU HAVE IRON ALR????????
    DREAMYYYYYYY
    hah i got u with fist dummy
    NOOOOOO
    NOOQUERPQUIEWOURQOPWEFR
    EQURPOIEQUROIQUR
    QWEROIUQPOEWURPOQEWR""")




@stonks.command()
async def credits(ctx):
  credits_embed = discord.Embed(title="POGGERS CREDITS WHOWEROIQUOIRUOIQP")
  credits_embed.description = "don\'t give Darling#0202 all the credits, read this to find out how"
  credits_embed.add_field(name="coders", value="Tofee#1331, and Darling#0202, Darling was the one typing the bot, but Tofee helped him.")
  credits_embed.add_field(name="API", value="discord.py")
  credits_embed.add_field(name="Supporters", value="xea#0341, Tofee#1331, my mom, my dad, pant#0469, monopoly bee#3824")
  credits_embed.add_field(name="Partners", value="My partners are")
  credits_embed.add_field(name="Lonely Man", value="""Join for big man fun, bully ppl (dont actually bully them tho) https://discord.gg/xVDNrp57Fx it is very pog loser""")
  await ctx.send(embed=credits_embed)


@stonks.command()
async def TeachMyProgrammer(ctx):
  teaching_embed = discord.Embed(title="Teach him pls :pleading_face:")
  teaching_embed.description = "Teach my programmer! He is very bad at discord.py, maybe u can teach him something! Just go to <#778401113862832138> its not that hard ;-;"
  teaching_embed.url = "https://discord.com/invite/MMChUH6HjT"
  teaching_embed.set_footer(text="can u join it pls")
  await ctx.send(embed=teaching_embed)

@stonks.command()
async def darling(ctx):
    others_embed = discord.Embed(title=" ")
    others_embed.description = "Darling\'s bots are..."
    others_embed.add_field(name="Stonkies", value= """Hello there! You tired of bots that are only made for moderation? Is your server full of moderation bots?
    And doesn't have any fun bots? Stonkies is just for you! Stonkies was made by Darling#0202 with help from Tofee#1331
    Darling#0202 is 13, while Tofee#1331 is 14. Stonkies started off as a discord.js bot, but it went through problems
    so I had to move to Python. I hope you have fun with it! And stay safe!1""")
    others_embed.add_field(name="Stonkies 2", value="""Stonkies 2 is originally a test bot, but we made it official, it is just like Stonkies, but with a little more action, it\'s more of an early access. Have fun with it!""")
    others_embed.add_field(name="GBP Bot", value="GBP Bot or GamerBoyPlays Bot, exclusive to the GBP server only!!!!1")
    await ctx.send(embed=others_embed)


@stonks.command()
async def flag(ctx, flag):
  if flag == "ph":
    await ctx.send(":flag_ph:")

  if flag == "iq":
    await ctx.send(":flag_iq:")

  if flag == "ac":
    await ctx.send(":flag_ac:")

  if flag == "ad":
    await ctx.send(":flag_ad:")

  if flag == "uae":
    await ctx.send(":flag_ae:")

  if flag == "af":
    await ctx.send(":flag_af:")

  if flag == "ag":
    await ctx.send(":flag_ag:")

  if flag == "ai":
    await ctx.send(':flag_ai:')

  if flag == "al":
    await ctx.send(':flag_al:')

  if flag == "am":
    await ctx.send(':flag_am:')

  if flag == "ao":
    await ctx.send(":flag_ao")

  if flag == "aq":
    await ctx.send(":flag_aq:")

  if flag == "ar":
    await ctx.send(":flag_ar:")


@stonks.command()
async def dice(ctx):
  await ctx.send(random.randint(1, 100))

stonks.run(pog)