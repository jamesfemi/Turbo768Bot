import os
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Your welcome message
WELCOME_MESSAGE = """👋 Welcome!

Thanks for joining. 🚀

Use the menu below to get started and explore the available features. If you need any help, just send a message and I'll assist you.

Enjoy your experience! 😊"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message when the command /start is issued by ANY user."""
    await update.message.reply_text(WELCOME_MESSAGE)

def main():
    # Fetch the token from Render's environment variables
    token = os.environ.get("TELEGRAM_TOKEN")
    
    if not token:
        print("Error: TELEGRAM_TOKEN environment variable not set.", file=sys.stderr)
        sys.exit(1)

    # Build the application
    application = Application.builder().token(token).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Start long polling to listen for messages continuously
    print("Bot is up and listening for /start commands...")
    application.run_polling()

if __name__ == "__main__":
    main()
