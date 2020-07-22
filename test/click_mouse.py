import os
import time
import pyautogui
'''def window_gui(x,y):
    pyautogui.PAUSE=2.5     #函数延迟2.5s
    screeWidth,screenHeight=pyautogui.size()    #当前屏幕分辨率
    print(screeWidth,screenHeight)
    currentMouseX, currentMouseY = pyautogui.position()     #获取当前鼠标坐标
    print(currentMouseX,currentMouseY)
    pyautogui.moveTo(x,y);pyautogui.click()     #移动到坐标位置并且鼠标左键点击

window_gui(200,200)
'''

'''
#按住左键矩形运动并且每循环一次后像素距离缩小5
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, None, duration=0.5) # 隔0.5秒向右 ,如果传入none，当前光标的对象轴坐标值
    distance -= 5
    pyautogui.dragRel(None, distance, duration=0.5) # 隔0.5秒向下
    pyautogui.dragRel(-distance, None, duration=0.5) # 隔0.5秒向左
    distance -= 5
    pyautogui.dragRel(None, -distance, duration=0.5) # 隔0.5秒向上
'''

'''
#键盘函数
secs_between_keys=0.1
pyautogui.typewrite('ctrl','c',interval=secs_between_keys)     #按键输入间隔为0.1s，输入ctrl和C键，复制当前鼠标悬停行
pyautogui.typewrite('Hello world!', interval=secs_between_keys)     #鼠标当前悬停行输入Hello world!
pyautogui.typewrite( ['left', '?', 'right' ,'enter'],interval=secs_between_keys)    #光标左移，输入？，光标右移，换行
'''

import pyautogui
import time
secs_between_keys = 0.1
def B_mode():
    pyautogui.typewrite(['a','b'],interval=secs_between_keys)

def switch_mode():
    n=1
    while n>0:
        B_mode()
        n = n + 1
        if n == 5:
            continue
        if n>7:break
        print(n)

switch_mode()

'''file_object = open('H:\eGalaxWorks80W46~20200624-Holystone-1332-v00_T8\eGalaxUpdateLog\eGalaxUpdate2-20200721-093138.log','r', encoding='UTF-8')
f = open('H:\eGalaxWorks80W46~20200624-Holystone-1332-v00_T8\eGalaxUpdateLog\eGalaxUpdate2-20200721-093138.log','a', encoding='UTF-8')
g = re.search("\[Firmware update resource release].*\]*")
print(g)

import re
f = open("H:\eGalaxWorks80W46~20200624-Holystone-1332-v00_T8\eGalaxUpdateLog\eGalaxUpdate2-20200721-093138.log", "r", encoding='utf-8')     #打开test.txt文件，以只读得方式，注意编码格式，含中文
data = f.readlines()                            #循环文本中得每一行，得到得是一个列表的格式<class 'list'>
f.close()                                       #关闭test.txt文件
for line in data:
    result = re.match('.*?(Firmware.*\d).*',line)     #使用正则表达式筛选每一行的数据,自行查找正则表达式
    t = (result.group(1))                        #group(1)将正则表达式的(\d.*\d)提取出来
    f1 = open("test1.txt", "a+", encoding='utf-8')        #新建一个test1.txt文本，已追加的方式写入
    f1.write(t+'\n')                                      #将每一行打印进test1.txt文件并换行
f1.close()
'''