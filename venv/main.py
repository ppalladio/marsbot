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
    
    if 'BNB' in processed:
        return 'https://docs.google.com/spreadsheets/d/1EvV8WY-s_rYNvPPT8EgrFVW0Dd5jCLy0Oz6w7WFlj9A/edit#gid=0'
    if 'ai' in processed:
        return 'ai research report: https://drive.google.com/drive/u/1/folders/0ABaUtiGsh3VTUk9PVA'
    if 'ai tools' in processed:
        return 'https://docs.google.com/spreadsheets/d/1ATBQENAEHtLmP4h4RJefUiv7pML9oI9V-2Y2lz7aGnM/edit#gid=0'
    if 'ai报告' in processed:
        return 'https://docs.google.com/spreadsheets/d/1dVk2zVbGT6iNj-ywl_3ixgIpbHHL1mikrOJ7748cSOU/edit#gid=0'
    if '收支' in processed:
        return 'https://docs.google.com/spreadsheets/d/15lMm6VzwVN3FSw9nN87_SC9_j8eJlZNd/edit?rtpof=true'
    if '预算' in processed:
        return 'https://docs.google.com/spreadsheets/d/1xFFMMdH74LSfFfGQzpIZZGXsk7Y2yIyQ5gGCD51uTns/edit'
    if '会议' in processed:
        return 'https://meet.google.com/xjj-iasz-acj'
    if '运营' in processed:
        return 'https://docs.google.com/spreadsheets/d/1QrgsbOyqqyFgwbBWuNLhegvOKsv9zWIF-pk5f-ubMuE/edit#gid=0'
    return '请输入 BNB ai "ai tools" ai报告 收支 预算 会议 运营'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type:str=update.message.chat.type
    text:str=update.message.text
    
    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text:str=text.replace(BOT_USERNAME, '').strip()
            response:str=handel_response(new_text)
        else:
            return
    else:
        response:str=handel_response(text)
        
        
    print('Bot:',response)
    await update.message.reply_text(response)
    
    
    
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context,error}')