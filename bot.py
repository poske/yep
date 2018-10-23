import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import bot
from discord.utils import get
import asyncio
import inspect
import functools
import typing
from discord.utils import find

extensions = ['fun', 'owner', 'commands', 'moderation', 'music']

bot = commands.Bot(command_prefix='/')
bot.remove_command('help')

client = discord.Client()

bot.load_extension("commands")
bot.load_extension("fun")
bot.load_extension("moderation")
bot.load_extension("music")


owner_id = 277100410500677632

game = discord.Game("carl ver. 3.0")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Vers. 3.0')
    await bot.change_presence(activity=game)
	
@bot.event
async def on_guild_join(guild):
    await guild.create_role(name="shush", colour=discord.Colour(0x232323))

    

def check_if_it_is_me(ctx):
    return ctx.message.author.id == 277100410500677632
	
@bot.command(pass_context=True)
@commands.check(check_if_it_is_me)
async def load(ctx, extension):
    """owner only"""
    try:
        bot.load_extension(extension)
        print('Loaded {}'.format(extension))
        await ctx.send(":ok_hand:")
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))
        await ctx.send(":thumbsdown:")

@bot.command(pass_context=True)
@commands.check(check_if_it_is_me)
async def unload(ctx, extension):
    """owner only"""
    try:
        bot.unload_extension(extension)
        print('Unloaded {}'.format(extension))
        await ctx.send(":ok_hand:")
    except Exception as error:
        print('{} cannot be unloaded. [{}]'.format(extensions, error))
        await ctx.send(":thumbsdown:")
		
@bot.command(pass_context=True)
@commands.check(check_if_it_is_me)
async def reload(ctx, extension):
    """owner only"""
    try:
        bot.unload_extension(extension)
        bot.load_extension(extension)
        print('reloaded {}'.format(extension))
        await ctx.send(":ok_hand:")
    except Exception as error:
        print('{} cannot be reloaded. [{}]'.format(extensions, error))
        await ctx.send(":thumbsdown:")
		
		
@bot.command(pass_context=True)
@commands.check(check_if_it_is_me)
async def die(ctx):
    """closes the bot"""
    await ctx.send("bye")
    await bot.logout()
	
@bot.command(pass_context=True)
async def help(ctx):
	
	
    embed = discord.Embed(
        color=0x00ff80
    )
	
    embed.set_author(name='Help')
    embed.add_field(name="**---COMMANDS---**", value="** **", inline=False)
    embed.add_field(name="-about:", value="gives you information about this bot", inline=False)
    embed.add_field(name="-add:", value="basic maths retard", inline=False)
    embed.add_field(name="-info (user):", value="gives you information about mentioned user", inline=False)
    embed.add_field(name="-invite:", value="gives you this bots invite link", inline=False)
    embed.add_field(name="-mass_ping (user):", value="mass mentions a specific user", inline=False)
    embed.add_field(name="-purge (amount):", value="deletes a specific number of messages in one channel", inline=False)
    embed.add_field(name="-say:", value="say something using a bot", inline=False)
    embed.add_field(name="-avatar (user):", value="get avatar of a mentioned user", inline=False)
    embed.add_field(name="-addrole (user) (role):", value="adds a specific role to mentioned user", inline=False)
    embed.add_field(name="-removerole (user) (role):", value="removes a specific role to mentioned user", inline=False)
    embed.add_field(name="** **", value="** **", inline=False)
    embed.add_field(name="**---FUN---**", value="** **", inline=False)
    embed.add_field(name="-daddy:", value="daddy", inline=False)
    embed.add_field(name="-follow:", value="follow me on twitter lol", inline=False)
    embed.add_field(name="-gamemode 1:", value="go play minecraft idiot", inline=False)
    embed.add_field(name="-hang:", value="hang some niggers idk", inline=False)
    embed.add_field(name="-insult (user):", value="insult a user", inline=False)
    embed.add_field(name="-love (user):", value="spread some love", inline=False)
    embed.add_field(name="-kill (user):", value="fucking kill someone", inline=False)
    embed.add_field(name="-ramen:", value="🍜", inline=False)
    embed.add_field(name="-rape (user):", value="rape people for fun", inline=False)
    embed.set_footer(text="For more commands use '/help2'")

    await ctx.send(embed=embed)
	
	
@bot.command(pass_context=True)
async def help2(ctx):
	
    embed = discord.Embed(
        color=0x00ff80
    )
	
    embed.set_author(name='Help2')
    embed.add_field(name="**---MODERATION---**", value="** **", inline=True)
    embed.add_field(name="-ban (user):", value="ban someone using this command", inline=False)
    embed.add_field(name="-kick (user):", value="kick someone using this command", inline=False)
    embed.add_field(name="-mute(user):", value="mute a mentioned user", inline=False)
    embed.add_field(name="-unmute (user):", value="unmute a mentioned user", inline=False)
	
    await ctx.send(embed=embed)
		
# @bot.command(pass_context=True)
# async def servers(ctx):
  # servers = list(bot.servers)
  # await ctx.send(f"Connected on {str(len(servers))} servers:")
  # await ctx.send('\n'.join(server.name for server in servers))

		
		
	

bot.run('NDY4ODg3Mzk2NjA4Mzc2ODQy.DprNRQ.tOLmEC3MgIgy0K_YefQc-ITmqxY')
