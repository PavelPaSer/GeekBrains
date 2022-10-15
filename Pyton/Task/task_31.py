# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".




#text = 'ыфвфывцабвбавбвывабвв'
# print(text)
# if text.find('абв') == -1:
#     print('Данный нобор текста не обнаружен')
# else:
#     text = text.replace('абв','')
# print(text)
def Del_Word(s):
    return False if 'абв' in s else True

a = 'ыфвфывцабвбавбвывабввабв абв'

a = a.split()
print(a)
a = list(filter(Del_Word,a))
print(a)