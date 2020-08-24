import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def 핑(ctx):
    await ctx.send(f'퐁! {round(client.latency * 1000)}ms') # 핑을 표시

@client.command(aliases=['8ball', 'test'])
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




client.run("NzIyNjkwOTM0NjcxODAyNDQ5.Xumwvw.EHxeeTV1tWH20pIlFyLkpIO-ovQ")