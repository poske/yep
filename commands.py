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

bot = commands.Bot(command_prefix='/')


def check_if_it_is_me(ctx):
    return ctx.message.author.id == 277100410500677632
	

class commands:
    def __init__(self, bot):
        self.bot = bot
		
    @commands.command(pass_context=True)
    async def info(self, ctx, user: discord.Member):
		
        embed = discord.Embed(
            color=0x00ff80
        )
		
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name=user, value="** **", inline=False)
        embed.add_field(name="users id", value=user.id, inline=False)
        embed.add_field(name="account created since:", value='{0.joined_at}'.format(user), inline=False)
		
    
        await ctx.send(embed=embed)
	
# fmt = '{0} joined on {0.joined_at} and has {1} roles.'
# await ctx.send(fmt.format(member, len(member.roles)))

    @info.error
    async def info_error(self, ctx, error):
        await ctx.send('I could not find that nigger...')
		
		
    @bot.command(pass_context = True)
    @has_permissions(manage_channels=True)
    async def purge(self, ctx, amount: int):
        """Delete specific amount of messages."""
        await ctx.channel.purge(limit=amount)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have the required permissions. Loser..")
			
    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def say(self, ctx, arg):
        """Say something using a bot."""
        await ctx.send(arg)
		
    @commands.command(pass_context=True)
    async def add(self, ctx, a: int, b: int):
        """Basic maths retard."""
        await ctx.send(a + b)
		
    @commands.command(pass_context=True)
    async def argument(self, ctx, *args):
        """Counts how many arguments are in your sentance."""
        await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
		
    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def mass_ping(self, ctx, member: discord.Member):
        await ctx.send("<@{}>".format(member.id))
        await ctx.send("<@{}>".format(member.id))
        await ctx.send("<@{}>".format(member.id))
        await ctx.send("<@{}>".format(member.id))
        await ctx.send("<@{}>".format(member.id))


		
    @mass_ping.error
    async def mass_ping_error(self, ctx, error):
	    if isinstance(error, MissingPermissions):
	        await ctx.send("You don't have the required permissions. Loser..")
			
    @commands.command(pass_context=True)
    async def invite(self, ctx):
	    """bots invite link"""
	    await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=468887396608376842&permissions=8&scope=bot")
		
    @commands.command(pass_context=True)
    async def neck(self, ctx):
	    await ctx.send("https://cdn.discordapp.com/attachments/476391534476918804/503644799614844937/neck.png")
		
		
    # @client.command(pass_context=True)
    # async def displayembed():
	    # embed = discord.Embed(
            # title = 'Title',
            # description = 'This is a description.',
            # colour = discord.Colour.blue()
        # )
		
        # embed.set_footer(text='This is a footer.')
        # embed.set_image(url='https://cdn.discordapp.com/attachments/467457126659391498/503648362403463188/Snapchat-1477071008-1.png')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/467457126659391498/503648362403463188/Snapchat-1477071008-1.png')
        # embed.set_author(name='Author name',
        # icon_ulr='https://cdn.discordapp.com/attachments/467457126659391498/503648362403463188/Snapchat-1477071008-1.png'
        # embed.add_field(name='Field name', value='Field Value', inline=False)
        # embed.add_field(name='Field name', value='Field value', inline=True)
        # embed.add_field(name='Field name', value='Field value', inline=True)
		
		# await client.say(embed=embed)
		
    @commands.command(pass_context=True)
    async def about(self, ctx):
        embed=discord.Embed(title="About the bot:", color=0x00ff80, description="He's cool i guess")
        embed.set_author(name="poske#3363", icon_url="https://cdn.discordapp.com/attachments/315447202501754880/503668967051624448/0e5152917a473debb830715dbc4c4f99--hand-reference-kaneoya-sachiko.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/503850829149896714/503970546804064276/8d3934f0e36fd142ef9fb23aa4d69dd52.jpg")
        embed.add_field(name="Created on:", value="8.10.2018", inline=True)
        embed.add_field(name="Honestly", value="Fuck this bot", inline=False)
        embed.add_field(name="Fun fact:", value="This bot took way to long to make him.", inline=True)
        embed.add_field(name="** **", value="** **", inline=True)
        embed.add_field(name="** **", value="** **", inline=False)
        embed.add_field(name="** **", value="** **", inline=False)
        embed.set_footer(text="Enjoy.")
        await ctx.send(embed=embed)
		
    @commands.command(pass_context=True)
    async def avatar(self, ctx, user: discord.Member):
        await ctx.send("{}'s avatar: {}".format(user, user.avatar_url))
		
    @commands.command(pass_context=True)
    @has_permissions(manage_roles=True)
    async def addrole(self, ctx, user: discord.Member, lol):
        role = discord.utils.get(ctx.guild.roles, name=lol)
        await user.add_roles(role)
        await ctx.send("done :ok_hand:")
		
    @addrole.error
    async def addrole_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have the required permissions. Loser..")
			
    @commands.command(pass_context=True)
    @has_permissions(manage_roles=True)
    async def removerole(self, ctx, user: discord.Member, lol1):
        role = discord.utils.get(ctx.guild.roles, name=lol1)
        await user.remove_roles(role)
        await ctx.send("done :ok_hand:")
		
    @removerole.error
    async def removerole_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have the required permissions. Loser..")







def setup(bot):
    bot.add_cog(commands(bot))