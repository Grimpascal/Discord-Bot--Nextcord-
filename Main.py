import nextcord
import aiohttp
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} berhasil Online!')

    Cstatus = bot.get_channel(1392437843875332177)
    if Cstatus:
        global aktivitas
        aktivitas = nextcord.Activity(
            name = "Mr. Robot",
            type = nextcord.ActivityType.watching
        )
        await bot.change_presence(activity=aktivitas, status=nextcord.Status.online)
        await Cstatus.send('Bot Online 🟢, Melakukan aktivitas...')
    else:
        print('Channel tidak Ditemukan!')


@bot.event
async def on_message(message):
    general = 1392443769386963075
    activityBot = 1392587936045862923
    konten = message.channel.id 

    if message.author.bot:
        return
    
    if konten == general:
        if general and message.content.strip().lower() == 'p':
            await message.reply('apa')

    if konten == activityBot:
        if activityBot and message.content.strip().lower() == 'dnd':
            await bot.change_presence(status=nextcord.Status.dnd, activity=aktivitas)
            await message.add_reaction('🔴')
        elif activityBot and message.content.strip().lower() == 'on':
            await bot.change_presence(status=nextcord.Status.online, activity=aktivitas)
            await message.add_reaction('🟢')
        elif activityBot and message.content.strip().lower() == 'inv':
            await bot.change_presence(status=nextcord.Status.invisible, activity=None)
            await message.add_reaction('👻')
        elif activityBot and message.content.strip().lower() == 'idle':
            await bot.change_presence(status=nextcord.Status.idle, activity=None)
            await message.add_reaction('💤')
        else:
            await message.reply('Tidak ada')

    await bot.process_commands(message)


bot.run('TOKEN')