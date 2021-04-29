import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix = ";", description = "I don't know")

@bot.command()
@commands.has_permissions(manage_messages = True) #<=== To run the command you must have the "manage_messages"
async def say(ctx, *texte):                       #permissions if you want to change this permissions, you can get the different permissions on https://discordpy.readthedocs.io/en/latest/api.html?highlight=permissions#discord.Permissions
    await ctx.message.delete() #<=== You can delete this line if you want to keep the message your order after executing it
    await ctx.send(" ".join(texte))

bot.run("**********************************************") #<=== Put the token between the quotes.
