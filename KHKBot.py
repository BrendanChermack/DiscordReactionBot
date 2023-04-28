import discord
import logging
import logging.handlers

intents = discord.Intents(messages=True, guilds=True)
intents.typing = False
intents.presences = False

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG) 
logging.getLogger('discord.http').setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler( 
    filename='discord.log',
    encoding = 'utf-8',
    maxBytes = 32 * 1024 * 1024,
    backupCount = 5,                                              
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

TOKEN = '[REDACTED]'

@client.event
async def on_ready():
    print(f"We have logged in as {client.user.name}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('Yo' or 'yo'):
        await message.channel.send('Yo')
@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 1100996109511430164 and str(payload.emoji) == '💻':
        guild = await client.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = discord.utils.get(guild.roles, name = 'Computer Science')
        if role:
            await member.add_roles(role)
            print(f"Added role {role.name} to {member.display_name}")
    if payload.message_id == 1100996109511430164 and str(payload.emoji) == '👴':
        guild = await client.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = discord.utils.get(guild.roles, name = 'Alumni')
        if role:
            await member.add_roles(role)
            print(f"Added role {role.name} to {member.display_name}")
    if payload.message_id == 1100996109511430164 and str(payload.emoji) == '🌩️':
        guild = await client.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = discord.utils.get(guild.roles, name = 'Electrical Engineering')
        if role:
            await member.add_roles(role)
            print(f"Added role {role.name} to {member.display_name}")
    if payload.message_id == 1100996109511430164 and str(payload.emoji) == '🖱️':
        guild = await client.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = discord.utils.get(guild.roles, name = 'Software Engineering')
        if role:
            await member.add_roles(role)
            print(f"Added role {role.name} to {member.display_name}")
    if payload.message_id == 1100996109511430164 and str(payload.emoji) == '🏎️':
        guild = await client.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = discord.utils.get(guild.roles, name = 'Mechanical Engineering')
        if role:
            await member.add_roles(role)
            print(f"Added role {role.name} to {member.display_name}")
    if payload.message_id == 1100996109511430164 and str(payload.emoji) == '🖥️':
        guild = await client.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = discord.utils.get(guild.roles, name = 'Computer Engineering')
        if role:
            await member.add_roles(role)
            print(f"Added role {role.name} to {member.display_name}")
    if payload.message_id == 1100996109511430164 and str(payload.emoji) == '🤓':
        guild = await client.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = discord.utils.get(guild.roles, name = 'Math/Stats')
        if role:
            await member.add_roles(role)
            print(f"Added role {role.name} to {member.display_name}")
    if payload.message_id == 1100996109511430164 and str(payload.emoji) == '✅':
        guild = await client.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = discord.utils.get(guild.roles, name = 'Pledge/Potential')
        if role:
            await member.add_roles(role)
            print(f"Added role {role.name} to {member.display_name}")
    if payload.message_id == 1100996109511430164 and str(payload.emoji) == '🏠':
        guild = await client.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = discord.utils.get(guild.roles, name = 'IHC/Resident')
        if role:
            await member.add_roles(role)
            print(f"Added role {role.name} to {member.display_name}")
try:
    client.run(TOKEN)
except Exception as e:
    print(f"Error: {e}")
