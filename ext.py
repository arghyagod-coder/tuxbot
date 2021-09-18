import discord

def cembed(title="", description="", thumbnail="", picture="", color=discord.Color.dark_theme()):
    embed = discord.Embed()
    if color != discord.Color.dark_theme():
        embed = discord.Embed(color=discord.Color(value=color))
    if title != "":
        embed.title = title
    if description != "":
        embed.description = description
    if thumbnail != "":
        embed.set_thumbnail(url=thumbnail)
    if picture != "":
        embed.set_image(url=picture)
    return embed

