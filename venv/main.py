from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, Filters, ContextTypes

TOKEN: Final ='5951771627:AAE4ZQNGZA5iH1dyApaKs1aRpHE-j8dRqqQ'
BOT_USERNAME: Final = '@MarsTeamBot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('welcome to mars team bot')
        
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('list of commands:')
        
#response

def handel_response(text:str)->str:
    processed:str=text.lower()