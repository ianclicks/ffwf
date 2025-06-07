import discord
import os

class InviteBanBot(discord.Client):
    async def on_ready(self):
        print(f"✅ Bot is online as {self.user} with streaming status.")

    async def on_message(self, message):
        if message.author.bot:
            return

        if "discord.gg/" in message.content.lower():
            if "discord.gg/mandatory" not in message.content.lower():
                try:
                    await message.guild.ban(
                        message.author,
                        reason="Unauthorized Discord invite",
                        delete_message_days=1
                    )
                    print(f"🚫 {message.author} was banned for posting an invite link.")
                except discord.Forbidden:
                    print("❌ Missing permission to ban users.")
                except Exception as e:
                    print(f"⚠️ Error banning user: {e}")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

# Streaming status
streaming_activity = discord.Streaming(
    name="🔗 join /mandatory",
    url="https://twitch.tv/example"  # Replace with your actual Twitch link
)

client = InviteBanBot(intents=intents, activity=streaming_activity)

# Get token from Railway secret
client.run(os.environ["TOKEN"])
