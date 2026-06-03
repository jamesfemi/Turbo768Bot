import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# The welcome message you requested
WELCOME_MESSAGE = """👋 Welcome!

Thanks for joining. 🚀

Use the menu below to get started and explore the available features. If you need any help, just send a message and I'll assist you.

Enjoy your experience! 😊"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message when the command /start is issued."""
    await update.message.reply_text(WELCOME_MESSAGE)

def main():
    # Render provides a PORT environment variable, defaulting to 8080 locally
    port = int(os.environ.get("PORT", 8080))
    
    # Get the token from environment variables (set later in Render)
    token = os.environ.get("TELEGRAM_TOKEN")
    
    if not token:
        print("Error: TELEGRAM_TOKEN environment variable not set.")
        return

    # Build the application
    application = Application.builder().token(token).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Run the bot using long polling (perfect for free Render web services or background workers)
    print("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
