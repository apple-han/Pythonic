# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/25 19:38'

###############################
# 通过添加空格 使代码更优雅      #
#############################

''''
    布局清晰、整洁、优雅的代码能给阅读它的人带来愉悦感，
    而且它能够帮助开发者之间进行良好的沟通。
    在一个团队中，保持良好的代码格式需要团队成员在选取
    一套合适的代码格式规则的基础上遵从和应用。同时它需要
    每个团队成员树立正确的态度，因为实际工作中有很多开发
    者抱着这样的想法：‘代码能工作才是最重要的’，但往往代
    码会不断的修改，且可读性直接关系到可维护性和可扩展性。
    
    为了让读者更加深入地理解代码布局的重要性，我们先来个
    猜数字的示例，下面两段代码，编码完全相同，只是排版不同
    你觉得哪个更加容易阅读呢？
'''
# 示例一

import random
guesses_made = 0
name = input('Hello! What is your name?\n')
number = random.randint(1, 20)
print('Well, {0}, T an thinking of a number between 1 and 20.'.format(name))
while guesses_made < 6:
    guess = int(input('Take a guess: '))
    guesses_made += 1
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    print('Good job, {0}! You guessed my number un {1} guesses!'
          .format(name, guesses_made))
else:
    print('Nope. The number I was thinking of was {0}'.format(number))

# 示例二

import random

guesses_made = 0
name = input('Hello! What is your name?\n')
number = random.randint(1, 20)
print('Well, {0}, T an thinking of a number between 1 and 20.'.format(name))
while guesses_made < 6:
    guess = int(input('Take a guess: '))
    guesses_made += 1
    if guess < number:print('Your guess is too low.')
    if guess > number:print('Your guess is too high.')
    if guess == number:break
if guess == number: print('Good job, {0}! You guessed my number un {1} guesses!'.
                          format(name, guesses_made))
else:print('Nope. The number I was thinking of was {0}'
           .format(number))
'''
    看到上面两个例子，相信很多的读者都倾向于阅读第一个例子，这就是
    代码布局和排版带给我们最直观的感受
'''

'''
    Python代码布局规范
        1)在一组代码表达完一个完整的思路之后，应该用空白进行间隔
            if guess == number:
                print('Good job, {0}'.format(number))
        2)尽量保持上下文语义的一致性。比如我们在进行函数调用的时候
          尽量保证两个函数放在一起最好是调用者在上，被调用者在下比
          如
          def A():
              B()
          def B():
              pass
        3)尽量不要写过长的字符，每行最好不要超过80个字符。以每屏能够
          显示完整代码而不需要拖动滚动条为最佳，超过部分用圆括号，方
          括号和花括号进行连接，并且保证连接的元素垂直对其。例如下面
          >>> x = (this is very long string)
          ... 'it is used for testing line limited characters'
          >>> print(x)
          this is very long stringit is used for testing line limited characters
          >>> def Draw_Line(pointX1,pointY1,pointY2=2,
                            color='green',width=2,style='bold')          
'''


