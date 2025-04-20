import os
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

IMAGE_DIR = "images"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salam! Zəhmət olmasa təkər naxış kodunu göndərin (məsələn: KNK50).")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip().upper()
    image_path = os.path.join(IMAGE_DIR, f"{code}.png")
    if os.path.exists(image_path):
        with open(image_path, 'rb') as img:
            await update.message.reply_photo(photo=InputFile(img), caption=f"Naxış kodu: {code}")
    else:
        await update.message.reply_text("Bağışlayın, bu naxış koduna uyğun şəkil tapılmadı.")

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot işə düşdü...")
    app.run_polling()

if __name__ == "__main__":
    main()