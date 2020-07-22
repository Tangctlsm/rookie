#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import pyautogui
import time
import os
import os.path


def process_bar(percent, start_str='', end_str='', total_length=0):
    bar = ''.join(["\033[31m%s\033[0m"%'   '] * int(percent * total_length)) + ''
    bar = '\r' + start_str + bar.ljust(total_length) + ' {:0>4.1f}%|'.format(percent*100) + end_str
    print(bar, end='', flush=True)

print('自动升级进行中！( Automatic update in progress! )')
pyautogui.moveTo(1127,684)#屏幕升级按键
pyautogui.click()

wait_time = 70
for i in range(wait_time):
    time.sleep(1)
    print('\r'+'自动升级中, 还剩 ', wait_time-i, '秒', '( Automatic update, ', wait_time-i, 'seconds left )', end=" ")


ls = []
log_file = ''

def getAppointFile(path, ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path, tmp)
            if True==os.path.isdir(pathTmp):
                getAppointFile(pathTmp, ls)
            elif pathTmp[pathTmp.rfind('.')+1:].upper()=='LOG':
                ls.append(pathTmp)
    except PermissionError:
        pass

def main():

    path = os.getcwd()
    path = path + '/TouchUpdate/eGalaxWorks80W46~20200624-Holystone-1332-v00_T8/eGalaxUpdateLog'
    print('now path: ', path)
    if os.path.isdir(path) == True:
        pass
    else :
        print('该路径不存在！ ( The path does not exist! )')
        return

    getAppointFile(path, ls)

    log_file = ls[len(ls) - 1]
    #print(log_file)

    with open(log_file, 'r') as f:
        # str = f.readlines()
        # print(str)
        step = 0
        for eachLine in f:
            if ( 0 == step ) :
                if ( '- Version: 01_T7' in eachLine ) :
                    print('当前屏幕固件版本：T7 ( Current screen firmware version: T7 )')
                    step = 1
                elif ( '- Version: 00_T8' in eachLine) :
                    print('当前屏幕固件版本：T8 ( Current screen firmware version: T8 )')
                    step = 13

            elif ( 1 == step ) :
                if ( 'Download firmware Pass.' in eachLine ) :
                    print('固件下载完成 ( Download firmware Pass )')
                    step = 2

            elif ( 2 == step ) :
                if ( 'Verify download result Pass.' in eachLine ) :
                    print('验证下载结果完成 ( Verify download result Pass )')
                    step = 3

            elif ( 3 == step ) :
                if ( 'Reset controller Pass.' in eachLine ) :
                    print('复位控制器完成 ( Reset controller Pass )')
                    step = 4

            elif ( 4 == step ) :
                if ( 'Wait controller disconnect success.' in eachLine ) :
                    print('等待控制器断开连接完成 ( Wait controller disconnect success )')
                    step = 5

            elif ( 5 == step ) :
                if ( 'Check firmware state Pass.' in eachLine ) :
                    print('检查固件状态完成 ( Check firmware state Pass )')
                    step = 6

            elif ( 6 == step ) :
                if ( 'Hardware calibration Pass.' in eachLine ) :
                    print('硬件校准完成 ( Hardware calibration Pass )')
                    step = 7

            elif ( 7 == step ) :
                if ( 'Reset firmware Pass.' in eachLine ) :
                    print('复位固件完成 ( Reset firmware Pass )')
                    step = 8

            elif ( 8 == step ) :
                if ( ('Current Device:' in eachLine) and ('00_T8' in eachLine) ) :
                    print('当前设备版本：T8 ( Current device version: T8 )')
                    step = 9

            elif ( 9 == step ) :
                if ( ('Target Device:' in eachLine) and ('00_T8' in eachLine) ) :
                    print('目标设备版本：T8 ( Target device version: T8 )')
                    step = 10

            elif ( 10 == step ) :
                if ( 'Verfication Pass.' in eachLine ) :
                    print('校验完成 ( Verfication Pass )')
                    step = 11

            elif ( 11 == step ) :
                if ( 'Firmware update Success.' in eachLine ) :
                    print('固件升级成功！ ( Firmware update Success! )')
                    step = 99
                    break

            elif ( 13 == step ) :
                if ( ('Model: ' in eachLine ) and ('Version: 00_T8' in eachLine ) and ('already download!' in eachLine ) ) :
                    print('固件已升级！ ( Firmware halready download! )')
                    step = 99
                    break

        if (99 == step) :
            print('\r\n升级完成！10秒后将自动重启系统！ ( update completed! The system will automatically restart after 10 seconds! )\r\n')
            pyautogui.moveTo(1293, 824)
            pyautogui.click()#点击确认关闭程序
            time.sleep(10)
            # os.system("shutdown /r /t 0")
        else :
            print('\r\n升级失败！错误代码：', step, ' ( Update failed! Error code: ', step, ')\r\n')
            pyautogui.moveTo(1293, 824)
            pyautogui.click()  # 点击确认关闭程序
            print('\r\n120秒后将自动重启系统！ ( The system will automatically restart after 10 seconds! )\r\n')
            # time.sleep(50)
            wait_time = 120
            for i in range(wait_time):
                time.sleep(1)
                print('\r', wait_time-i, '秒后即将自动重启系统！ ( The system will automatically restart after ', wait_time-i, 'seconds! )', end=" ")

            # os.system("shutdown /r /t 0")


main()







# import re
# f = open("H:\eGalaxWorks80W46~20200624-Holystone-1332-v00_T8\eGalaxUpdateLog\eGalaxUpdate2-20200721-093138.log", "r")
# data = f.readlines()
# f.close()
# for line in data:
#     if "Firmware" in line:
#         print(line)
#     if "Download" in line:
#         print(line)
#     if "Current Device" in line:
#         print(line)
#     if "Target Device" in line:
#         print(line)
#     #result = re.findall(r"^.*[Download firmware Pass].*$",line)     #使用正则表达式筛选每一行的数据,自行查找正则表达式
# #print (result)


