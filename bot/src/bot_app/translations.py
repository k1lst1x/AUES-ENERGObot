from . translation_dict import translations

def _(text, lang="ru"):
    if lang == "ru":
        return text
    else:
        global translations
        try:
            return translations[lang][text]
        except:
            return text

def __(res, lang="ru"):
    if lang == "ru":
        text = res.get('text')
        text = text.replace("\\n", "\n")
        return text
    else:
        translation = res.get('translation')
        translation = translation.replace("\\n", "\n")
        return translation