from machine import Pin, PWM
from time import sleep

servo0 = PWM(Pin(26), freq=50, duty_u16=32768)
servo1 = PWM(Pin(25), freq=50, duty_u16=32768)
servo2 = PWM(Pin(33), freq=50, duty_u16=32768)
servo3 = PWM(Pin(32), freq=50, duty_u16=32768)

m = 8000 // 180
b = 1400

def posicion(servo, angulo): # Ajusta el cálculo del duty cycle para que esté en el rango 0-65535
    duty = int(m * angulo + b)
    duty = max(0, min(duty, 65535))  # Asegura que el duty cycle esté en el rango permitido
    servo.duty_u16(duty)
    print(angulo)
'''
#Servo_0 = Servo - (180°)
for i in range(36):
    posicion(servo0, 5*i)
    sleep(0.1)
    
for i in range(35,1,-1):
    posicion(servo0, 5*i)
    sleep(0.05)
'''

#Servo1 = Servo - Lateral izquierdo (0°,80°)
for i in range(0,11):
    posicion(servo1, 10*i)
    sleep(0.5)
    
for i in range(10,0,-1):
    posicion(servo1, 10*i)
    sleep(0.5)


#Servo_2 = Servo - Lateral izquierdo 
for i in range(36):
    posicion(servo2, 5*i)
    sleep(0.1)
    
for j in range(36,1,-1):
    posicion(servo2, 5*j)
    sleep(0.05)


#Servo_3 = Servo - Garra (100°,180°
for i in range(10,18):
    posicion(servo3, 10*i)
    sleep(0.5)
    
sleep(1)

for i in range(36,15,-1):
    posicion(servo3, 5*i)
    sleep(0.2)



'''
x=int(imput("angulo:"))
posicion(servo0, x)
ser1(
while True:
    posicion(servo0, 0)
    sleep(2)
    posicion(servo0, 180)
    sleep(2)
'''