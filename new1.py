import telebot

TOKEN = '543732889:AAFp-OvgYs0rUPRDzbm_cEEGrqzhi6Op00Q' # полученный у @BotFather

bot = telebot.TeleBot(TOKEN) #ddd

@bot.message_handler(commands=['start'])
def start(message):
	sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
	bot.register_next_step_handler(sent, hello)
	
def hello(message):
	bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))
	
bot.polling()