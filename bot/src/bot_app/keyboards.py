from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from .translations import _

inline_button_test = InlineKeyboardButton('Test', callback_data='test')
inline_kb = InlineKeyboardMarkup()

inline_kb.add(inline_button_test)

def studMenu(lang):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(_('Platonus', lang))
    btn2 = KeyboardButton(_('Корпоративная почта', lang))
    btn3 = KeyboardButton(_('ЦАК', lang))
    btn4 = KeyboardButton(_('Сброс пароля', lang))
    btn5 = KeyboardButton(_('Бухгалтерия', lang))
    btnBack = KeyboardButton(_('Назад', lang))
    keyboard.add(btn1, btn2, btn3, btn4, btn5)
    keyboard.add(btnBack)
    return keyboard

def applicMenu(lang):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(_('Бакалавриат', lang))
    btn2 = KeyboardButton(_('Магистратура', lang))
    btn3 = KeyboardButton(_('Докторантура', lang))
    btn4 = KeyboardButton(_('Колледж', lang))
    btn5 = KeyboardButton(_('Курсы ЕНТ', lang))
    btnBack = KeyboardButton(_('Назад', lang))
    keyboard.add(btn1, btn2, btn3, btn4, btn5)
    keyboard.add(btnBack)
    return keyboard

def gradMenu(lang):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(_('Заполнить Анкету', lang))
    btn2 = KeyboardButton(_('Мероприятия', lang))
    btn3 = KeyboardButton(_('Документы', lang))
    btnBack = KeyboardButton(_('Назад', lang))
    keyboard.add(btn1, btn2, btn3)
    keyboard.add(btnBack)
    return keyboard

def staffMenu(lang):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(_('Заявка в ДИТ', lang))
    btn2 = KeyboardButton(_('Корпоративная почта', lang))
    btn3 = KeyboardButton(_('Сброс пароля', lang))
    btnBack = KeyboardButton(_('Назад', lang))
    keyboard.add(btn1, btn2, btn3)
    keyboard.add(btnBack)
    return keyboard

langMenu = InlineKeyboardMarkup(row_width=2)

langRU = InlineKeyboardButton(text='Русский', callback_data='lang_ru')
langKZ = InlineKeyboardButton(text='Қазақша', callback_data='lang_kz')

langMenu.insert(langRU)
langMenu.insert(langKZ)

def mainMenu(lang):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btnChangeLang = KeyboardButton(_('Смена языка', lang))
    btnStud = KeyboardButton(_('Студентам', lang))
    btnApplic = KeyboardButton(_('Абитуриентам', lang))
    btnGrad = KeyboardButton(_('Выпускникам', lang))
    btnStaff = KeyboardButton(_('Сотрудникам', lang))
    btnIdCard = KeyboardButton(_('Восстановить ID-карту', lang))
    btnSocial = KeyboardButton(_('Социальные сети', lang))
    btnInfo = KeyboardButton(_('Контакты', lang))
    btnFb = KeyboardButton(_('Предложения, замечания по Боту', lang))
    keyboard.add(btnChangeLang)
    keyboard.add(btnStud, btnApplic)
    keyboard.add(btnGrad, btnStaff)
    keyboard.add(btnIdCard)
    keyboard.add(btnSocial)
    keyboard.add(btnInfo)
    keyboard.add(btnFb)
    return keyboard
