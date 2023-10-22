import requests
import telebot
import time
import config

# 创建Telegram Bot实例
bot = telebot.TeleBot(config.bot_token)

# 处理用户输入的位置信息
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "请输入位置信息（例如北京：101010100）：")

@bot.message_handler(func=lambda message: True)
def handle_location(message):
    location = message.text
    key = config.api_key

    # 无限循环发送数据到Telegram Bot
    while True:
        # 发送GET请求并获取JSON响应
        response = requests.get(config.url, params={"location": location, "key": key})
        data = response.json()

        # 提取主要天气数据
        daily_forecasts = data["daily"]

        # 发送数据到Telegram Bot
        for forecast in daily_forecasts:
            # 省略代码...

            bot.send_message(chat_id=config.chat_id, text=message)

        # 延时2分钟
        time.sleep(14400)

# 启动Telegram Bot
bot.polling()
