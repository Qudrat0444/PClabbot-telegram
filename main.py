from tkinter import PhotoImage

import telebot
from telebot import types

TOKEN = '7639902205:AAHt8ffbmdqB8V7pP2BRSsVjTW40j51aUK8'
ADMIN_ID = 7146790168

bot = telebot.TeleBot(TOKEN)
user_lang = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🇺🇿 O'zbekcha"), types.KeyboardButton("🇷🇺 Русский"))
    bot.send_message(message.chat.id, "Tilni tanlang / Выберите язык:", reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text in ["🇺🇿 O'zbekcha", "🇷🇺 Русский"])
def set_language(message):
    lang = 'uz' if "O'zbekcha" in message.text else 'ru'
    user_lang[message.chat.id] = lang
    send_main_menu(message)

def send_main_menu(message):
    lang = user_lang.get(message.chat.id, 'uz')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton("/location"),
        types.KeyboardButton("/contact"),
        types.KeyboardButton("/instagram"),
        types.KeyboardButton("/telegram"),
        types.KeyboardButton("/SSD"),
        types.KeyboardButton("/DDR"),
        types.KeyboardButton("/Display"),
        types.KeyboardButton("/callback"),
        types.KeyboardButton("/Laptop"),
        types.KeyboardButton("/CPU"),
        types.KeyboardButton("/help")
    )
    text = "👋 Assalomu aleykum! Quyidagi menyudan tanlang:" if lang == 'uz' else "👋 Здравствуйте! Выберите пункт меню:"
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    lang = user_lang.get(message.chat.id, 'uz')
    text = (
        "/location - Manzilimiz haqida malumot olish uchun\n"
        "/contact - Biz bilan bog'lanish uchun\n"
        "/instagram - Instagram haqida malumot olish uchun\n"
        "/telegram - Telegram orqali bog'lanish uchun\n"
        ""

    )




@bot.message_handler(commands=['CPU'])
def cpu(message):
    lang = user_lang.get(message.chat.id, 'uz')
    photo_url = 'https://overclockers.ru/st/legacy/blog/413830/584241_O.jpg'

    caption = (
        "INTEL CORE I9 14900K" if lang == 'uz'
        else "INTEL CORE I9 14600KF"
    )

    bot.send_photo(message.chat.id, photo=photo_url, caption=caption)




@bot.message_handler(commands=['Laptop'])
def laptop(message):
    lang = user_lang.get(message.chat.id, 'uz')
    photo_url = 'https://www.iphones.ru/wp-content/uploads/2024/10/IMG_4728.jpeg'

    caption = (
        "💻 MACBOOK M4 PRO 2300$!" if lang == 'uz'
        else "💻 MAC BOOK M4 PRO 2300$!"
    )

    bot.send_photo(message.chat.id, photo=photo_url, caption=caption)




@bot.message_handler(commands=['Display'])
def display(message):
    lang = user_lang.get(message.chat.id, 'uz')
    text = (
        "Display 15,6 HD frame $?\n"
        "Display 15,6 HD noframe $?\n"
        "Display 15,6 FullHD IPS frame $?\n"
        "Display 15,6 FullHD IPS noframe $?\n"
        "APLLE DISPLAY +998334470444\n"
        "Agar boshqa ekran kerak bo'lsa \u261b /callback"
        if lang == 'uz' else
        "Display 15,6 HD frame $?\n"
        "Display 15,6 HD noframe $?\n"
        "Display 15,6 FullHD IPS frame $?\n"
        "Display 15,6 FullHD IPS noframe $?\n"
        "APLLE DISPLAY +998334470444\n"
        "Если нужен другой тип экрана \u261b /callback"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['SSD'])
def ssd(message):
    lang = user_lang.get(message.chat.id, 'uz')
    text = (
        "SSD sata:\n"
        "SSD Lexar sata 128gb 14$\n"
        "SSD lexar sata 256gb 19$\n"
        "SSD lexar sata 512gb 29$\n"
        "SSD kingfast sata 128gb 12$\n"
        "SSD kingfast sata 256gb 16$\n"
        "SSD kingfast sata 512gb 26$\n"
        "(SSA m2 nvme lexar)\n"
        "SSD M2nvme Lexar 256gb 20$\n"
        "SSD M2nvme Lexar 512gb 30$\n"
        "SSD M2nvme Lexar 1tr 51$\n"
        "CADDY 3$\n"
        "!!!HAMMASIGA UZTANOVKA 100.000!!!"
        if lang == 'uz' else
        "SSD sata:\n"
        "SSD Lexar sata 128gb 14$\n"
        "SSD lexar sata 256gb 19$\n"
        "SSD lexar sata 512gb 29$\n"
        "SSD kingfast sata 128gb 12$\n"
        "SSD kingfast sata 256gb 16$\n"
        "SSD kingfast sata 512gb 26$\n"
        "(SSA m2 nvme lexar)\n"
        "SSD M2nvme Lexar 256gb 20$\n"
        "SSD M2nvme Lexar 512gb 30$\n"
        "SSD M2nvme Lexar 1tr 51$\n"
        "CADDY 3$\n"
        "!!!Установка всему 100.000!!!"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['DDR'])
def ddr(message):
    text = (
        "(So DDR2,3,4,5)\n"
        "So DDR2 2gb 7$\n"
        "So DDR3 8gb Kingston 9$\n"
        "So DDR4 8gb Kingston 13$\n"
        "So DDR4 16gb Kingston 20$\n"
        "So DDR5 8gb Crucial 23$\n"
        "So DDR5 16gb Kingston 34$\n"
        "(DDR 2,3,4)\n"
        "DDR2 2gb kingston 7$\n"
        "DDR3 8gb Kingston 9$\n"
        "DDR4 8gb Kingston 13$\n"
        "DDR4 16gb Lexar 25$"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['location'])
def location(message):
    lang = user_lang.get(message.chat.id, 'uz')
    text = "📍 Manzil: https://yandex.uz/maps/-/CHrLuRZb" if lang == 'uz' else "📍 Адрес: https://yandex.uz/maps/-/CHrLuRZb"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['contact'])
def contact(message):
    lang = user_lang.get(message.chat.id, 'uz')
    text = (
        "📞 Aloqa raqamlari:\n"
        "+998 91 144 04 44 (Xikmat)\n"
        "+998 33 447 04 44 (Qudrat)\n"
        "+998 98 143 04 44 (Abdullo)"
        if lang == 'uz' else
        "📞 Контактные номера:\n"
        "+998 91 144 04 44 (Хикмат)\n"
        "+998 33 447 04 44 (Кудрат)\n"
        "+998 98 143 04 44 (Абдулло)"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['instagram'])
def instagram(message):
    lang = user_lang.get(message.chat.id, 'uz')
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Instagram sahifamiz" if lang == 'uz' else "Наша страница в Instagram", url="https://www.instagram.com/pclabuz")
    markup.add(btn)
    bot.send_message(message.chat.id, "📸 Instagram sahifamiz:" if lang == 'uz' else "📸 Наша страница в Instagram:", reply_markup=markup)

@bot.message_handler(commands=['telegram'])
def telegram(message):
    lang = user_lang.get(message.chat.id, 'uz')
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Telegram kanalimiz" if lang == 'uz' else "Наш Telegram канал", url="https://t.me/pclabuz")
    markup.add(btn)
    bot.send_message(message.chat.id, "📱 Telegram kanalimiz:" if lang == 'uz' else "📱 Наш Telegram канал:", reply_markup=markup)

@bot.message_handler(commands=['callback'])
def callback_help(message):
    lang = user_lang.get(message.chat.id, 'uz')
    text = "📞 Raqamingizni yuborish uchun tugmani bosing:" if lang == 'uz' else "📞 Нажмите кнопку ниже, чтобы отправить свой номер:"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    contact_btn = types.KeyboardButton("📱 Raqamni yuborish / Отправить номер", request_contact=True)
    markup.add(contact_btn)
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    lang = user_lang.get(message.chat.id, 'uz')
    bot.send_message(
        message.chat.id,
        f"📲 Rahmat! Sizning raqamingiz qabul qilindi: {message.contact.phone_number}" if lang == 'uz' else f"📲 Спасибо! Ваш номер получен: {message.contact.phone_number}"
    )

    full_name = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip()
    username = f"@{message.from_user.username}" if message.from_user.username else "❌ Username yo‘q"
    admin_msg = (
        f"📥 Yangi kontakt:\n"
        f"👤 F.I.SH: {full_name}\n"
        f"🔗 Username: {username}\n"
        f"📞 {message.contact.phone_number}"
    )
    try:
        bot.send_message(ADMIN_ID, admin_msg)
    except Exception as e:
        print("Xatolik:", e)

@bot.message_handler(commands=['myid'])
def myid(message):
    bot.send_message(message.chat.id, f"🆔 Sizning Telegram ID: {message.chat.id}")

@bot.message_handler(func=lambda msg: True)
def unknown(message):
    lang = user_lang.get(message.chat.id, 'uz')
    text = "❗ Nomaʻlum buyruq. Iltimos, menyudan foydalaning." if lang == 'uz' else "❗ Неизвестная команда. Пожалуйста, используйте меню."
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
