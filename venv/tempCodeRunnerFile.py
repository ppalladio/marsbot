if __name__ == '__main__':
    
    print('Bot started')
    app = Application.builder().token(TOKEN).build()
    
#commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    
    #message
    app.add_handler(MessageHandler(filter.TEXT,handle_message))
    
    #error
    app.add_error_handler(error)
    
    #polling
    print('Bot polling')
    app.run_polling(poll_interval=3)