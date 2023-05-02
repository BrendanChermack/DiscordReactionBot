Discord Role Assignment Bot
This Python script is a Discord bot that listens to specific messages and assigns roles to members based on their reaction to the messages. The bot is built using the discord.py library.

Setup
Before running the bot, make sure you have Python 3.7 or higher installed on your system. You will also need to install the discord.py library using pip. To install the required dependencies, run the following command:

pip install -r requirements.txt
Next, create a Discord bot and obtain its token. You can follow the instructions in the Discord Developer Portal to create a new bot and obtain its token.

Create a new file named .env in the same directory as the script, and add the following line to it:

makefile
Copy code
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
Replace YOUR_DISCORD_BOT_TOKEN with your bot token.

Usage
To start the bot, run the following command in your terminal:

css
Copy code
python main.py
The bot will log in to Discord and start listening for messages. When a member reacts to a specific message with a specific emoji, the bot will assign the corresponding role to the member.

Configuration
You can modify the message ID and emoji-role mappings in the on_raw_reaction_add event handler to customize the bot's behavior. Make sure to update the message_id and emoji values to match the message and emoji you want to listen for. You can also update the role name to match the role you want to assign to the member.

python

if payload.message_id == MESSAGE_ID and str(payload.emoji) == 'EMOJI':
    guild = await client.fetch_guild(payload.guild_id)
    member = await guild.fetch_member(payload.user_id)
    role = discord.utils.get(guild.roles, name='ROLE_NAME')
    if role:
        await member.add_roles(role)
        print(f"Added role {role.name} to {member.display_name}")
Logging
The bot logs its activity to a file named discord.log. The log file is rotated when it reaches 32 MB, and up to 5 backup files are kept. The log messages include a timestamp, log level, logger name, and message.

You can modify the log level by updating the logger.setLevel and logging.getLogger('discord.http').setLevel lines. The available log levels are DEBUG, INFO, WARNING, ERROR, and CRITICAL.

Conclusion
This bot is a simple example of how to use the discord.py library to build a Discord bot that listens for reactions and assigns roles. You can use this code as a starting point to build more complex bots with additional functionality.
