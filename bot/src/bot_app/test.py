from aiogram import types
from . app import dp, db
from . keyboards import inline_kb, langMenu, mainMenu, studMenu, applicMenu, gradMenu, staffMenu
from . data_fetcher import get_random, get_text
from .translations import _, __

'''
@dp.message_handler(commands='start1')
async def train_ten(message: types.Message):
    lang = db.get_lang(message.from_user.id)
    res = await get_randon()
    await message.reply(_(res.get('name'), lang), reply_markup=inline_kb)
'''

@dp.message_handler()
async def mess(message: types.Message):
    lang = db.get_lang(message.from_user.id)
    if message.text == _('Смена языка', lang):
        await message.reply(_('Выберите язык', lang), reply_markup=langMenu)
    elif message.text == _('Восстановить ID-карту', lang):
        res = await get_text(0)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('Социальные сети', lang):
        res = await get_text(1)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('Контакты', lang):
        res = await get_text(2)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('Предложения, замечания по Боту', lang):
        res = await get_text(3)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    

    elif message.text == _('Студентам', lang):
        await message.reply(_('Студентам', lang), reply_markup=studMenu(lang))
    elif message.text == _('Platonus', lang):
        res = await get_text(4)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('Корпоративная почта', lang):
        res = await get_text(5)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('ЦАК', lang):
        res = await get_text(6)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('Сброс пароля', lang):
        res = await get_text(7)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('Бухгалтерия', lang):
        res = await get_text(8)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    

    elif message.text == _('Абитуриентам', lang):
        await message.reply(_('Абитуриентам', lang), reply_markup=applicMenu(lang))
    elif message.text == _('Бакалавриат', lang):
        res = await get_text(9)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('Магистратура', lang):
        res = await get_text(10)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('Докторантура', lang):
        res = await get_text(11)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('Колледж', lang):
        res = await get_text(12)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('Курсы ЕНТ', lang):
        res = await get_text(13)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    

    elif message.text == _('Выпускникам', lang):
        await message.reply(_('Выпускникам', lang), reply_markup=gradMenu(lang))
    elif message.text == _('Заполнить Анкету', lang):
        res = await get_text(14)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('Мероприятия', lang):
        res = await get_text(15)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == _('Документы', lang):
        res = await get_text(16)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)
    

    elif message.text == _('Сотрудникам', lang):
        await message.reply(_('Сотрудникам', lang), reply_markup=staffMenu(lang))
    elif message.text == _('Заявка в ДИТ', lang):
        res = await get_text(17)
        await message.reply(__(res, lang), parse_mode="Markdown", disable_web_page_preview=True)


    elif message.text == _('Назад', lang):
        await message.reply(_('Вы вернулись в основное меню', lang), reply_markup=mainMenu(lang))
