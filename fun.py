import discord
import random
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


class fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")
		
    @commands.command(pass_context=True)
    async def daddy(self, ctx):
        """daddy"""
        await ctx.send("{} what the fuck".format(ctx.message.author.mention)) 
		
    @commands.command(pass_context = True)
    async def love(self, ctx, member: discord.Member):
        """Spread some love."""
        await ctx.send('{} loves <@{}> fucking fags..'.format(ctx.message.author.mention, member.id))
		
    @commands.command(pass_context = True)
    async def ramen(self, ctx):
        """🍜"""
        await ctx.send("🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜🍜")
		
    @commands.command(pass_context = True)
    @has_permissions(administrator=True)
    async def follow(self, ctx):
        """follow me on twitter lol"""
        await ctx.send("follow my twitter lol https://twitter.com/___Poske___")
		
    @commands.command()
    async def hang(self, ctx, amount: typing.Optional[int] = 99, *, liquid="niggers"):
        """hang some niggers"""
        await ctx.send('{} {} have been hanged!'.format(amount, liquid))
		
    @commands.command()
    async def rape(self, ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
        """Rape people idk for fun."""
        raped = ", ".join(x.name for x in members)
        await ctx.send('{} just got raped for {}. kinky..'.format(raped, reason))
# remember you fucking idiot replace the @bot.command with @commands.command spastic

    @commands.command(pass_context=True)
    async def insult(self, ctx, member: discord.Member):
	    await ctx.send("<@{}> you're awesome".format(member.id))
		
    @commands.command(pass_context=True)
    async def gamemode(self, ctx):
	    await ctx.send("this isn't minecraft retard")
		
    @commands.command(pass_context=True)
    async def kill(self, ctx, user: discord.Member):
        options = ["got fucking gamershotted", "got fucking game ended"]
        msg = random.choice(options)
        await ctx.send("<@{}> {} by {}".format(user.id, msg, ctx.author.mention))
		
		
# @okick.error
# async def okick_error(ctx, error):
	# if isinstance(error, CheckFailure):
	    # await ctx.send("You don't have the required permissions. Loser..")









def setup(bot):
    bot.add_cog(fun(bot))