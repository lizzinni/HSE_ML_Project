import telebot
from tgbot_token import bot
import joblib

model_filename = '../model/flood_model.cbm'
model = joblib.load(model_filename)


@bot.message_handler(commands=['start'])
def handle_start(message):
    chat = message.chat.id
    username = message.from_user.username
    try:
        bot.send_message(chat, f"Привет, @{username}!\n"
                               f"Это бот для предсказания вероятности потопа в регионе, в зависимости от значений "
                               "параметров: \n"
                               "1) MonsoonIntensity (от 0 до 16)\n"
                               "2) TopographyDrainage (от 0 до 18)\n"
                               "3) RiverManagement (от 0 до 16)\n"
                               "4) Deforestation (от 0 до 17)\n"
                               "5) Urbanization (от 0 до 17)\n"
                               "6) ClimateChange (от 0 до 17)\n"
                               "7) DamsQuality (от 0 до 16)\n"
                               "8) Siltation (от 0 до 16)\n"
                               "9) AgriculturalPractices (от 0 до 16)\n"
                               "10) Encroachments (от 0 до 18)\n"
                               "11) IneffectiveDisasterPreparedness (от 0 до 16)\n"
                               "12) DrainageSystems (от 0 до 17)\n"
                               "13) CoastalVulnerability (от 0 до 17)\n"
                               "14) Landslides (от 0 до 16)\n"
                               "15) Watersheds (от 0 до 16)\n"
                               "16) DeterioratingInfrastructure (от 0 до 17)\n"
                               "17) PopulationScore (от 0 до 18)\n"
                               "18) WetlandLoss (от 0 до 19)\n"
                               "19) InadequatePlanning (от 0 до 16)\n"
                               "20) PoliticalFactors (от 0 до 16)\n"
                               "Пожалуйста, введите значения для каждого парамера в нужном диапазоне через пробел")
    except Exception as e:
        print(e)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    chat = message.chat.id
    try:
        input_values = [int(x) for x in message.text.split() if x.isdigit()]
        if len(input_values) != 20:
            bot.send_message(chat, "Ошибка: Введите ровно 20 значений.")
            return
        input_data = [input_values]
        prediction = model.predict(input_data)[0]
        bot.send_message(chat, f"Вероятность потопа: {prediction:.4}")
    except Exception as e:
        print(e)
        bot.send_message(chat, "Ошибка: Проверьте правильность ввода.")


bot.polling(none_stop=True)
