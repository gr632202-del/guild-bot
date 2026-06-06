import discord
from discord.ext import commands
import requests
import os

# Token ab GitHub par nahi, hum Render website par daalenge
TOKEN = os.environ.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def guild(ctx, uid: str):
    await ctx.send(f"⏳ Wait, UID {uid} ki guild check kar raha hoon...")
    
    api_url = f"https://free-ff-api-src-5plp.onrender.com/api/v1/account?region=IND&uid={uid}"
    
    try:
        response = requests.get(api_url).json()
        if "guild" in response:
            g_name = response["guild"]["guildName"]
            g_level = response["guild"]["guildLevel"]
            g_glory = response["guild"]["guildGlory"]
            
            await ctx.send(f"🛡️ **Guild:** {g_name} | ⭐ **Level:** {g_level} | 🏆 **Glory:** {g_glory}")
        else:
            await ctx.send("❌ Yeh player kisi guild mein nahi hai.")
    except:
        await ctx.send("⚠️ API Server down hai, baad mein try karein.")

if TOKEN:
    bot.run(TOKEN)
else:
    print("Token nahi mila! Render par token check karein.")
  
