
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from parse import courses  

BOT_TOKEN = ""

keyboard = [["Python", "JavaScript", "DevOps"]]
markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Բարի գալուստ Top 5 Education Center Bot 🤖\n\n"
        "Ընտրիր ծրագրավորման լեզուն․",
        reply_markup=markup
    )
async def handle_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = update.message.text.lower()
    if lang in courses:
        text = f"📚 {lang.upper()} դասընթացներ՝\n\n"
        for c in courses[lang]:
            text += f"🏫 {c['center']}\n⏳ {c['months']} ամիս\n💰 {c['price']}\n\n"
        await update.message.reply_text(text)
    else:
        await update.message.reply_text("❌ Այդ լեզվով տվյալ չունեմ")


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_language))


if __name__ == "__main__":
    print("🤖 Bot is starting...")
    app.run_polling(poll_interval=1.0, timeout=20)
