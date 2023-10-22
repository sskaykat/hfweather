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
            date = forecast["fxDate"]
            temp_max = forecast["tempMax"]
            temp_min = forecast["tempMin"]
            weather_day = forecast["textDay"]
            weather_night = forecast["textNight"]
            wind_day = forecast["windDirDay"]
            wind_night = forecast["windDirNight"]
            uv_index = forecast["uvIndex"]

            message = f"🃏📢📢📢📢📢📢🀄\n\n位置: {location}\n日期: {date}\n最高温度: {temp_max}°C\n最低温度: {temp_min}°C\n白天天气: {weather_day}\n夜间天气: {weather_night}\n白天风向: {wind_day}\n夜间风向: {wind_night}\n紫外线指数: {uv_index}\n-_--_--_--_--_--_--_--_--_--_-\n---空山新雨后，天气晚来秋---"
            bot.send_message(chat_id=config.chat_id, text=message)

        # 延时2分钟
        time.sleep(14400)

# 启动Telegram Bot
bot.polling()
