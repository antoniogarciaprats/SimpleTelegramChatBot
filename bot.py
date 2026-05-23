from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# --- FUNCIONES DEL BOT ---

# Esta función asíncrona se ejecuta cuando un usuario escribe /start
async def comando_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # update.message.reply_text envía un mensaje de vuelta al usuario
    await update.message.reply_text('¡Hola desde Ubuntu! Soy tu bot de prueba. Escríbeme algo y te lo repetiré.')


# Esta función se ejecuta cuando el usuario envía texto normal
async def responder_eco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Guardamos en una variable lo que el usuario ha escrito
    texto_recibido = update.message.text

    # Respondemos con el mismo texto
    await update.message.reply_text(f'Has dicho: "{texto_recibido}"')


# --- CONFIGURACIÓN PRINCIPAL ---
if __name__ == '__main__':
    # 1. Reemplaza 'TU_TOKEN_AQUI' con el token real que te dio BotFather
    TOKEN = '8833769428:AAEtfk8y5Iu0BNsbZzehX6J05oJ9zC7eUAs'

    # 2. Construimos la aplicación del bot
    app = ApplicationBuilder().token(TOKEN).build()

    # 3. Le decimos al bot qué funciones usar para cada acción
    # Si recibe el comando /start, usa la función comando_start
    app.add_handler(CommandHandler('start', comando_start))

    # Si recibe un texto que NO es un comando, usa la función responder_eco
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_eco))

    print("Bot encendido. Ve a Telegram y envíale un mensaje...")

    # 4. Ponemos al bot a "escuchar" los mensajes constantemente
    app.run_polling()