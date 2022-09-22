# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# rle-encode.py 
 
import itertools

def compress(text):
    for char, same in itertools.groupby(text):
        count = sum(1 for _ in same)                # number of repetitions
        yield char if count == 1 else str(count)+char

print(''.join(compress("aaabccccCCaB")))




# def rle_encode(data): 
#     encoding = '' 
#     prev_char = '' 
#     count = 1 
#     # if not data: return '' 
 
#     for char in data: 
#         if char != prev_char: 
#             if prev_char: 
#                 encoding += str(count) + prev_char 
#                 count = 1 
#                 prev_char = char 
#             else: 
#                 count += 1 
#         else: 
#             encoding += str(count) + prev_char 
#             print(encoding)
#         return encoding 

# encoded_val = rle_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE') 
# print(encoded_val) 



# line = 'AAABBCCCCD'
# print(line)
# words = line.split(' ')             # разделили строку на список
# print (words)

# new_words = []                      # убириаем слова, содержащие 'кава'
# count=0
# for i in range(len(words)-1):
#     while words[i]==words[i+1]:
#         count+=1 
#         continue
#     element=count*words[i]
#     new_words.append(element)

# print(new_words)
# res=' '.join(new_words)             # собираем строку используя в качестве разделителя пробел
# print(res)