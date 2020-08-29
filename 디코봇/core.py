import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

token = 'NzIyNjkwOTM0NjcxODAyNDQ5.XumwYQ.3UIiSSLsldV8kOo0CAM6Aemx6rY'

EMBED_URL = "https://cdn.discordapp.com/attachments/697450184875049010/747816940625723502/Screenshot_20200825-224051_Love_LiveAS.jpg"

client = commands.Bot(command_prefix='.')
status_url = 'https://www.youtube.com/watch?v=1cb8klW1hxs'
status = cycle(['와 샌증', '뀽뀽'])

client.remove_command('help') # 기존 help 명령어 제거

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

# @client.event
# async def on_command_error(ctx, error):
    # if isinstance(error, commands.MissingRequiredArgument):
        # await ctx.send('제대로 써 빙구야')

# @client.event
# async def on_command_error(ctx, error):
    # if isinstance(error, commands.CommandNotFound):
        # await ctx.send('잘못된 명령어임')

@tasks.loop(seconds=5)
async def change_status(): # start()는 필수
    await client.change_presence(activity=discord.Streaming(name=next(status), url=status_url))

@client.command()
async def 핑(ctx):
    await ctx.send(f'퐁! {round(client.latency * 1000)}ms') # 핑을 표시

@client.command()
async def 삭제(ctx, amount : int): # ".삭제" 까지 지움
    await ctx.channel.purge(limit=amount)

@삭제.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('삭제 뒤에 숫자를 써야지 뭐하냐')


@client.command()
async def 킥(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def 밴(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def 언밴(ctx, *, member): # member 은 '유저#0001' 이런 형식
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#');

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return

@client.command()
async def displayembed(ctx):
    embed = discord.Embed(
    title = 'Title',
    description = 'This is a description.',
    color = discord.Color.blue()
    )
    embed.set_footer(text='This is a footer.')
    embed.set_image(url=EMBED_URL)
    embed.set_thumbnail(url=EMBED_URL)
    embed.set_author(name='Author Name',
    icon_url=EMBED_URL)
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=True)
    embed.add_field(name='Field Name', value='Field Value', inline=True)

    await ctx.send(embed=embed)

@client.command()
async def help(ctx): # 개인 메세지
    author = ctx.message.author

    embed = discord.Embed(
    color = discord.Color(0x7289da) # Hex Color
    )
    embed.set_author(name='Help')
    embed.add_field(name='.ping', value='Returns Pong!', inline=False)

    await author.send(embed=embed)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes – definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
    await ctx.send(f'Question : {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
