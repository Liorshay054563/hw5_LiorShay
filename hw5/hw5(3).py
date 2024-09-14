# start

height: float = float(input("Enter your height: "))

while height < 0.4 or height > 2.5:
    print(height, 'wrong input')
    height = float(input('try again'))
print('ok height')

# end

#start input number,for_loop

number_1: int = int(input('Enter number:'))
number_2: int = int(input('Enter a second number:'))

if number_1 < number_2:
    for i in range(number_1, number_2 + 1):
        print(i, end=" ")
if number_2 < number_1:
    for i in range(number_2, number_1, -1):
        print(i, end=" ")

#end

#start input number, while loop/ עשיתי בנוסף

# start
number_1: int = int(input('Enter number:'))
number_2: int = int(input('Enter a second number:'))
counter= number_2-number_1


while number_1 < number_2:
    print(number_1)
    number_1 += 1
    counter += 1


while number_2 < number_1:
    print(number_1)
    number_1 -= 1
    counter = counter + 1
print('good')

#end

#start pie


print('pie = ?')
pie: float= 3.14
x : float= float(input('how much pie:'))
counter: int=1

while x != pie and counter <3:
    print('try again')
    x: float= float(input('How much pie?:'))
    counter += 1
if x == pie:
    print("you are correct pie = 3.14")
else:
    print('not ok')

#start while True

while True:
    num1: int = int(input('Enter number:'))
    num2: int = int(input('Enter second number:'))
    num3: int = int(input('Enter another number:'))
    avg_num: int = (num1 + num2 + num3) / 3
    if 0 <= num1 <= 10 and 11 <= num2 <= 60 and 61 <= num3 <= 100 and num2 == avg_num :
        print('Good job')

        break
    else:
        print('try again')

# end