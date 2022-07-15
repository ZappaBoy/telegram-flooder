import argparse
import time
import os

from telegram.client import Telegram

import config


# https://my.telegram.org/apps
def get_connection(api_id, api_hash, phone):
    connection = Telegram(
        api_id=api_id,
        api_hash=api_hash,
        phone=phone,
        database_encryption_key='P$$WD99188235',
    )
    connection.login()
    return connection


def get_chats(connection):
    result = connection.get_chats()
    result.wait()
    if result.error:
        print(f'get chats error: {result.error_info}')
    return result.update['chat_ids']


def print_chats_description(connection, chat_ids):
    for chat_id in chat_ids:
        chat_info = connection.get_chat(chat_id)
        chat_info.wait()
        print('Title: {} - Chat ID: {}'.format(chat_info.update['title'], chat_id))


def send_message(connection, chat_id, text):
    result = connection.send_message(
        chat_id=chat_id,
        text=text,
    )

    result.wait()
    if result.error:
        print(f'send message error: {result.error_info}')
    else:
        print('message has been sent')


def main():
    print('Starting...')

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--chat_id', type=int, default=None, required=False)
    parser.add_argument('-t', '--text', default=None, required=False)
    parser.add_argument('-r', '--repeat', type=int, default=1, required=False)
    args = parser.parse_args()

    api_id = os.environ.get('TELEGRAM_FLOODER_API_ID', config.api_id)
    api_hash = os.environ.get('TELEGRAM_FLOODER_API_HASH', config.api_hash)
    phone = os.environ.get('TELEGRAM_FLOODER_PHONE', config.phone)

    connection = get_connection(api_id, api_hash, phone)
    chat_ids = get_chats(connection)
    if args.chat_id is not None and args.text is not None:
        for i in range(args.repeat):
            send_message(connection, args.chat_id, args.text)
            time.sleep(3)
    else:
        print_chats_description(connection, chat_ids)


if __name__ == '__main__':
    main()
