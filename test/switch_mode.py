import pyautogui
import time
#secs_between_keys = 0.0.5
def B_mode():
    pyautogui.hotkey('alt','b')
    time.sleep(0.5)
def Color_mode():
    pyautogui.hotkey('alt','c')
    time.sleep(0.5)
def Power_mode():
    pyautogui.hotkey('alt','o')
    time.sleep(0.5)
def M_mark_mode():
    pyautogui.hotkey('alt','m')
    time.sleep(0.5)
def Pw_mark_mode():
    pyautogui.hotkey('alt','p')
    time.sleep(0.5)
def Cw_mark_mode():
    pyautogui.hotkey('alt','e')
    time.sleep(0.5)
def AMM_mark_mode():
    pyautogui.hotkey('ctrl','alt','e')
    time.sleep(0.5)
def Dual_mode():
    pyautogui.hotkey('alt','u')
    time.sleep(0.5)
def Holo_mode():
    pyautogui.hotkey('alt','n')
    time.sleep(0.5)
def Quad_mode():
    pyautogui.hotkey('alt','q')
    time.sleep(0.5)
def TDI_mode():
    pyautogui.hotkey('alt','n')
    time.sleep(0.5)

def switch_mode():
    n=0.5
    while n>0:
        n=n+0.5
        [Color_mode(), Power_mode(), B_mode(), M_mark_mode(), M_mark_mode(), B_mode(), Pw_mark_mode(),
                Pw_mark_mode(), B_mode(), Cw_mark_mode(), Cw_mark_mode(), B_mode()]
        #if n >50:
        #    continue
        #if n>70:break
        print(n)
switch_mode()

f = open("H:\eGalaxWorks80W46~20200624-Holystone-1332-v00_T8\eGalaxUpdateLog\eGalaxUpdate2-20200721-093138.log", "r")
data = f.readlines()
f.close()
for line in data:
    if "Firmware" in line:
        print(line)
    if "Download" in line:
        print(line)
    if "Current Device" in line:
        print(line)
    if "Target Device" in line:
        print(line)
    #result = re.findall(r"^.*[Download firmware Pass].*$",line)     #使用正则表达式筛选每一行的数据,自行查找正则表达式
#print (result)
