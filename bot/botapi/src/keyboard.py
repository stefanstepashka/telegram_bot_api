from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

inline_button_m = InlineKeyboardButton('Мужской род', callback_data='Male')
inline_button_w = InlineKeyboardButton('Женский род', callback_data='Female')
inline_button_s = InlineKeyboardButton('Средний род', callback_data='Med')

inline_keyboard = InlineKeyboardMarkup()

inline_keyboard.add(inline_button_m)
inline_keyboard.add(inline_button_w)
inline_keyboard.add(inline_button_s)