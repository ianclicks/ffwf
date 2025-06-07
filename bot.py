import discord
from discord.ext import commands

class MobileClient(discord.Client):
    async def on_ready(self):
        print(f"Bot is online as {self.user} (mobile mode)")

    async def on_message(self, message):
        if message.author.bot:
            return

        if "discord.gg/" in message.content.lower():
            allowed_invite = "discord.gg/mandatory"
            if allowed_invite not in message.content.lower():
                try:
                    await message.guild.ban(message.author, reason="Unauthorized Discord invite", delete_message_days=1)
                    print(f"🚫 {message.author} was banned for posting an invite link.")
                except discord.Forbidden:
                    print("❌ Missing permission to ban users.")
                except Exception as e:
                    print(f"⚠️ Error banning user: {e}")

# Make the bot show as on mobile (using custom status)
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True

client = MobileClient(intents=intents)

# Set the bot status to appear as "mobile"
activity = discord.CustomActivity(name="")  # empty name avoids status text
client.run("YOUR_BOT_TOKEN", bot=True)
