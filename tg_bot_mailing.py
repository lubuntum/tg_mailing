import os.path

import telebot
import re
from config import BOT_TOKEN

bot = telebot.TeleBot(token=BOT_TOKEN)

def sendMessageWithFiles(userIds, message, paths):
    for user in userIds:
        try:
            bot.send_message(user, message)
            print(f'Message send to user: {user}')
        except Exception as e:
            print(f'Failed to send message to user: {user}. Key error: {str(e)}')

    for user in userIds:
        try:
            for file in paths:
                with open(file, 'rb') as f:
                    bot.send_document(user, f,visible_file_name= re.sub(r'_\d*$', '', os.path.basename(file)), disable_notification=True)
                print(f'File: {file} succesfuly send to user: {user}')
        except Exception as e:
            print(f'Failed to send files to user: {user}. Key error: {str(e)}')



def sendMessageWithoutFiles(userIds, message):
    for user in userIds:
        try:
            bot.send_message(user, message)
            print(f'Message send to user: {user}')
        except Exception as e:
            print(f'Failed to send message to user: {user}. Key error: {str(e)}')