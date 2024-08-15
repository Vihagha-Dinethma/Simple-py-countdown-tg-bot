import datetime
import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()} !")



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("• /start\n• /help\n• /time\n• /now")
    
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    difference = datetime.datetime(2024, 11, 25, 0, 0, 0) - datetime.datetime.now()
    await update.message.reply_text(f"• Months : {int(difference.days/30)}\n• Weeks : {int(difference.days/7)}\n• Days : {difference.days}\n• Hours (total) : {(difference.days)*24 + int(difference.seconds/3600)}\n\n• {difference.days} days, {int(difference.seconds/3600)} hours")
    
async def now_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    x = datetime.datetime.now()
    await update.message.reply_text(f"• Today : {x.year} / {x.month:02} / {x.day:02}\n• Time (now) : {x.hour:02}:{x.minute:02}:{x.second:02}")
    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("enter valid command.")


def main() -> None:
  
    application = Application.builder().token("TOKEN").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("time", time_command))
    application.add_handler(CommandHandler("now", now_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
