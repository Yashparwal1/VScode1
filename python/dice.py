import random
import telegram
from telegram.ext import Updater, CommandHandler

# Replace <your_bot_token> with your bot token obtained from BotFather
# bot = telegram.Bot(token='5818555834:AAF61oPhhWUcmdNtW72mqIk3_vqgvpg2Kp4', parse_mode=telegram.ParseMode.HTML)
bot = telegram.Bot(token='5818555834:AAF61oPhhWUcmdNtW72mqIk3_vqgvpg2Kp4')

def roll_dice(update, context):
    # Generate a random number between 1 to 6
    dice_number = random.randint(1, 6)
    # Reply to the message with the dice number
    update.message.reply_text(f"You rolled a {dice_number}!")

def main():
    # Create an Updater object with your bot token
    updater = Updater(bot=bot, use_context=True)
    # Get the Dispatcher to register handlers
    dp = updater.dispatcher
    # Register the "/roll_dice" command
    dp.add_handler(CommandHandler('roll_dice', roll_dice))
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
