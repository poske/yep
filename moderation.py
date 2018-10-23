import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import bot_has_permissions, BotMissingPermissions
from discord.ext.commands import bot
from discord.utils import get
import asyncio
import inspect
import functools
import typing

bot = commands.Bot(command_prefix='/')


def check_if_it_is_me(ctx):
    return ctx.message.author.id == 277100410500677632
	

class moderation:
    def __init__(self, bot):
        self.bot = bot
		
    @commands.command(pass_context = True)
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member):
        await ctx.guild.ban(member)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
	        await ctx.send("You don't have the required permissions. Loser..")
			
    # @commands.command(pass_context=True)
    # @has_permissions(ban_members=True)
    # async def unban(self, ctx):
        # banned = await bot.get_user_info(mesg)
        # await ctx.guild.unban(banned)
	
    @commands.command(pass_context = True)
    @has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member):
        await ctx.guild.kick(user)
        await ctx.send("done")

    @kick.error
    async def kick_error(self, ctx, error):
	    if isinstance(error, MissingPermissions):
	        await ctx.send("You don't have the required permissions. Loser..")
			
    @commands.command(pass_context=True)
    @has_permissions(manage_roles=True)
    async def mute(self, ctx, user: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="shush")
        await user.add_roles(role)
        await ctx.send("done :ok_hand:")
		
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have the required permissions. Loser..")
			
    @commands.command(pass_context=True)
    @has_permissions(manage_roles=True)
    async def unmute(self, ctx, user: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="shush")
        await user.remove_roles(role)
        await ctx.send("done :ok_hand:")
		
	
		
		
def setup(bot):
    bot.add_cog(moderation(bot))