#kututphaneler cagrılır import edilir
import numbers
from tkinter import *
import math
import numpy as np
from ornek import delete

#region methodların veya fonskiyonların tanımlanması

#girilen degisken turleri
def button_click(char):
    global CalculatorOperator
    CalculatorOperator += str(char)
    text_input.set(CalculatorOperator)
    

#tüm line'i silme
def button_clear_all():
    global CalculatorOperator
    CalculatorOperator = ""
    text_input.set("")

#delete islemleri
def button_delete():
    global CalculatorOperator
    text = CalculatorOperator[:-1]
    CalculatorOperator = text
    text_input.set(text)

#Faktoriel fonkisyon
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
def fact_func():
    global CalculatorOperator
    result = str(factorial(int(CalculatorOperator)))
    CalculatorOperator = result
    text_input.set(result)

#region trigonometriFunctionlarrın yazılması
def trig_sin():
    global CalculatorOperator
    result = str(math.sin(math.radians(int(CalculatorOperator))))
    CalculatorOperator = result
    text_input.set(result)

def trig_cos():
    global CalculatorOperator
    result = str(math.cos(math.radians(int(CalculatorOperator))))
    CalculatorOperator = result
    text_input.set(result)

def trig_tan():
    global CalculatorOperator
    result = str(math.tan(math.radians(int(CalculatorOperator))))
    CalculatorOperator = result
    text_input.set(result)

def trig_cot():
    global CalculatorOperator
    result = str(1/math.tan(math.radians(int(CalculatorOperator))))
    CalculatorOperator = result
    text_input.set(result)

#endregion

#karekök functionnu yazılması
def square_root():
    global CalculatorOperator
    if int(CalculatorOperator)>=0:
        temp = str(eval(CalculatorOperator+'**(1/2)'))
        CalculatorOperator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)


# Function to change the sign of number
def sign_change():
    global CalculatorOperator
    if CalculatorOperator[0]=='-':
        temp = CalculatorOperator[1:]
    else:
        temp = '-'+CalculatorOperator
    CalculatorOperator = temp
    text_input.set(temp)    

#yüzde fonksiyonun tanimlama
def percent():
    global CalculatorOperator
    temp = str(eval(CalculatorOperator+'/100'))
    CalculatorOperator = temp
    text_input.set(temp)

#esittir operatorun tanimlanması
def button_equal():
    global CalculatorOperator
    temp_op = str(eval(CalculatorOperator))
    text_input.set(temp_op)
    CalculatorOperator = temp_op

#endregion

#trigonometrik degiskenleri cagırıp atama yapma
sin, cos, tan = math.sin, math.cos, math.tan

#pencerelernin ozellikleri
calculator = Tk()
calculator.configure(bg="#222831")
calculator.title("Scientific Calculator")
calculator.maxsize(650,450)
calculator.minsize(650,450)


calc_operator = ""
text_input = StringVar()

#sayıların giris yapıldıgı kısım
lineEdit = Entry(calculator, font=('Sanserif', 40), textvariable=text_input,bd=0.5, width = 18)
lineEdit.grid(pady=10,row=0,sticky="w",padx=100)

#Stillerin değişkenler üzerinden tanımlanması
ButonNumber={'bd':0.5, 'fg':'#000','bg':'#EEEEEE', 'font':('Sanserif'),'width':"5","height":"2","relief":"solid"}
ButonFourTransactions={'bd':0.5, 'fg':'#000','bg':'#A5C9CA', 'font':('Sanserif'),'width':"5","height":"2","relief":"solid"}
ButonTrigonometri={'bd':0.5, 'fg':'#000','bg':'#A5C9CA', 'font':('Sanserif'),'width':"5","height":"2","relief":"solid"}
ButonOtherOperations={'bd':0.5, 'fg':'#000','bg':'#00ADB5', 'font':('Sanserif'),'width':"5","height":"2","relief":"solid"}
ButonPar={'bd':0.5, 'fg':'#000','bg':'#00ADB5', 'font':('Sanserif'),'width':"3","height":"2","relief":"solid"}

#region numbers
button_0 = Button(calculator, ButonNumber, text='0',command=lambda:button_click('0'))
button_0.grid(row=4,sticky="w",padx=220,pady=8)
button_1 = Button(calculator, ButonNumber, text='1',command=lambda:button_click('1'))
button_1.grid(row=3,sticky="w",padx=290,pady=8)
button_2 = Button(calculator, ButonNumber, text='2',command=lambda:button_click('2'))
button_2.grid(row=3,sticky="w",padx=220,pady=8)
button_3 = Button(calculator, ButonNumber, text='3',command=lambda:button_click('3'))
button_3.grid(row=3,sticky="w",padx=150,pady=8)
button_4 = Button(calculator, ButonNumber, text='4',command=lambda:button_click('4'))
button_4.grid(row=2,sticky="w",padx=290,pady=8)
button_5 = Button(calculator, ButonNumber, text='5',command=lambda:button_click('5'))
button_5.grid(row=2,sticky="w",padx=220,pady=8)
button_6 = Button(calculator, ButonNumber, text='6',command=lambda:button_click('6'))
button_6.grid(row=2,sticky="w",padx=150,pady=8)
button_7 = Button(calculator, ButonNumber, text='7',command=lambda:button_click('7'))
button_7.grid(row=1,sticky="w",padx=290)
button_8 = Button(calculator, ButonNumber, text='8',command=lambda:button_click('8'))
button_8.grid(row=1,sticky="w",padx=220)
button_9 = Button(calculator, ButonNumber, text='9',command=lambda:button_click('9'))
button_9.grid(row=1,sticky="w",padx=150)
#endregion
#region operations
add = Button(calculator, ButonFourTransactions, text='+',command=lambda:button_click('+'))
add.grid(row=4,sticky="w",padx=360)
sub = Button(calculator, ButonFourTransactions, text='-',command=lambda:button_click('-'))
sub.grid(row=3,sticky="w",padx=360,pady=8)
mul = Button(calculator, ButonFourTransactions, text='*',command=lambda:button_click('*'))
mul.grid(row=2,sticky="w",padx=360,pady=8)
div = Button(calculator, ButonFourTransactions, text='/',command=lambda:button_click('/'))
div.grid(row=1,sticky="w",padx=360,pady=8)
#endregion
#region Trigonometrik
sintri = Button(calculator, ButonTrigonometri, text='sin',command=trig_sin)
sintri.grid(row=1,sticky="w",padx=430)
costri = Button(calculator, ButonTrigonometri, text='cos',command=trig_cos)
costri.grid(row=2,sticky="w",padx=430,pady=8)
tantri = Button(calculator, ButonTrigonometri, text='tan',command=trig_tan)
tantri.grid(row=3,sticky="w",padx=430,pady=8)
cottri = Button(calculator,ButonTrigonometri, text='cot',command=trig_cot)
cottri.grid(row=4,sticky="w",padx=430,pady=8)
#endregion
#region delete
delete_one = Button(calculator,ButonOtherOperations,text='DEL', command=button_delete)
delete_one.grid(row=2,sticky="w",padx=80)
delete_all = Button(calculator, ButonOtherOperations,text='AC', command=button_clear_all)
delete_all.grid(row=1,sticky="w",padx=80)
#endregion
#region OtherOperations
percentage = Button(calculator, ButonOtherOperations, text='%',command=percent)
percentage.grid(row=3,sticky="w",padx=80,pady=8)
point = Button(calculator, ButonOtherOperations, text='.',command=lambda:button_click('.'))
point.grid(row=4,sticky="w",padx=150,pady=8)
equal = Button(calculator, ButonOtherOperations, text='=',command=button_equal)
equal.grid(row=4,sticky="w",padx=290,pady=8)
#endregion
#region par
leftPar = Button(calculator,ButonPar, text='(',command=lambda:button_click('('))
leftPar.grid(pady=10,row=0,sticky="w",padx=10)                  
rightPar = Button(calculator, ButonPar, text=')',command=lambda:button_click(')'))
rightPar.grid(pady=10,row=0,sticky="w",padx=55)  
#endregion
#region other
sqrtnumber = Button(calculator,ButonOtherOperations, text='\u221A',command=lambda:button_click('**(1/'))
sqrtnumber.grid(row=4,sticky="w",padx=80,pady=8) 
Pi = Button(calculator,ButonTrigonometri, text='π',command=lambda:button_click(str(math.pi)))
Pi.grid(row=1, sticky="w",padx=500,pady=8)
kup = Button(calculator,ButonTrigonometri, text='x^n',command=lambda:button_click('**'))
kup.grid(row=2, sticky="w",padx=500,pady=8)
factorialOper = Button(calculator, ButonTrigonometri, text='x!',command=fact_func)
factorialOper.grid(row=3,sticky="w",padx=500,pady=8)
tenus= Button(calculator, ButonTrigonometri, text='10^x',command=lambda:button_click('10**'))
tenus.grid(row=4,sticky="w",padx=500,pady=8)
#endregion

calculator.mainloop() #ekranda gosterme
