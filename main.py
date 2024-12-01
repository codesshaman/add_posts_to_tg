from dotenv import load_dotenv
from apis.messages import *
import os

load_dotenv()

group = os.getenv("group")
token = os.getenv("token")

# print(f"token: {token}")
# print(f"group: {group}")

bot = Messages(token, group)

# Получить администраторов и их права
# response = bot.get_updates()
# print(response)

# Отправить сообщение
# response = bot.send_message("Привет, группа!")
# print(response)

# Получить информацию о группе
chat_info = bot.get_chat_info()
print(chat_info)

# Удалить сообщение (например, по ID)
# message_id = 6
# delete_response = bot.delete_message(message_id)
# print(delete_response)

# Получить последние сообщения
# messages = bot.get_messages()
# print(messages)

# Изменить сообщение
# edit_response = bot.edit_message(6, "Новый текст для сообщения")
# print(edit_response)


