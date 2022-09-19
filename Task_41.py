# Транслитирация вводимого текста
# from re import S


# translit={}
# translit=\
#     {'а': 'a',
#     'б':'b',
#     'в':'v',
#     'г':'g',
#     'д':'d',
#     'е':'e',
#     'ё':'yo',
#     'ж': 'g',
#     'з': 'z',
#     'и': 'i',
#     'й': 'y',
#     'к': 'k',
#     'л': 'l',
#     'м': 'm',
#     'н': 'n',
#     'о': 'o',
#     'п': 'p',
#     'р': 'r',
#     'с': 's',
#     'т': 't',
#     'у': 'u',
#     'ф': 'f',
#     'х': 'h',
#     'ц': 'c',
#     'ч': 'ch',
#     'ш': 'sh',
#     'щ': '',
#     'ъ': '',
#     'ы': 'y',
#     'ь': '',
#     'э': 'a',
#     'ю': 'yu',
#     'я': 'ya'
#     }

# list=input('введите слова: ')
# for k in range(len(list)):
#     print(translit[list[k]],end = "")

# 2 способ (изначально дан текст список t)
t=['a','b','v','g','d','e','zh','z','i','y','k','l','m','n','o','p','r','s','t','u','f','kh','ts','ch','sh','shch','','y','','e','yu','ya']
start_index=ord('a')
title='Переводим этот текст сейчас!'  
print(())
slug=""
title.lower
for s in range(len(title)):
    if ord('а')<=ord(s)<=ord('я'):                 # буквы а и я русские 
        slug += t[ord(s)-ord('а')]
        print(ord(s),ord('а'),ord(s)-ord('а'))      # для наглядности распечатка кодов символов
    else:
        slug+=s
print(slug)                