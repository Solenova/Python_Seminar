# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
confi=2021
rnd=random.randint(0,3)

def inputGame1 ():          #ввод данных игроком
    num1=int(input('1 games '))
    while num1<1 or num1>28: num1=int(input('введите снова'))
    return (num1)

def inputRnd ():            #ввод данных ботом
    print('2 games',end='')
    numRnd=random.randint(1,28)
    return (numRnd)

while confi>0:                  #сравниваем с имеющимися конфетами и определяем победителя
    if rnd==1:
        num=int(inputGame1())
        rnd=2
        if confi<28: 
            print('победил 1 игрок') 
            break
    else:
        num=int(inputRnd())
        print(num)
        rnd=1
        if confi<28: 
            print('победил 2 игрок') 
            break
    confi-=num
    print('конфет осталось',confi)

    #     if confi<28: 
    #         print('победил 1 игрок') 
    #         break

    # while confi>0:
        
    #     num1=int(input('1 игрок, введите количество конфет от 1 до 28 '))
    #     while num1<1 or num1>28: num1=int(input('введите снова'))
    #     confi-=num1
    #     if confi<28: 
    #         print('победил 1 игрок') 
    #         break
    
    #     num2=random.randint(1,29)
    #     print('2 games',num2)
    #     while num2<1 or num2>28: 
    #         num2=random.randint(1,29) 
    #         print('2 games',num2)
    #     confi-=num2
    #     if confi<28: 
    #         print('победил 2 игрок') 
    #         break