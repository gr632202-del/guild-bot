import discord
from discord.ext import commands
import requests
import os
from flask import Flask
from threading import Thread

# --- RENDER KO KHUSH RAKHNE KE LIYE FAKE WEBSITE ---
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ----------------------------------------------------

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

# Fake website ko chalu karo
keep_alive()

# Bot ko chalu karo
if TOKEN:
    bot.run(TOKEN)
else:
    print("Token nahi mila! Render par token check karein.")
    
