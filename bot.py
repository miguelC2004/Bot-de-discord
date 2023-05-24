import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

# Evento de inicio del bot
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')

# Comando para lanzar un dado
@bot.command()
async def roll(ctx, sides: int):
    import random
    result = random.randint(1, sides)
    await ctx.send(f'Has lanzado un dado de {sides} caras y has obtenido {result}.')

# Comando para saludar a un jugador
@bot.command()
async def greet(ctx):
    await ctx.send('¡Saludos aventurero!')

# Comando para atacar a un enemigo
@bot.command()
async def attack(ctx, enemy: str):
    await ctx.send(f'¡Has atacado a {enemy}!')

# Comando para usar una habilidad especial
@bot.command()
async def use_ability(ctx, ability: str):
    await ctx.send(f'¡Has usado la habilidad {ability}!')

# Comando para mostrar la hoja de personaje
@bot.command()
async def character_sheet(ctx):
    character_info = {
        'Nombre': 'Gandalf',
        'Clase': 'Mago',
        'Nivel': 10,
        'Vida': 100,
        'Ataque': 50,
        'Defensa': 20
    }
    sheet = '\n'.join([f'{key}: {value}' for key, value in character_info.items()])
    await ctx.send(f'Hoja de personaje:\n```{sheet}```')

bot.run('TOKEN_DEL_BOT')  # Reemplaza con el token de tu bot de Discord
