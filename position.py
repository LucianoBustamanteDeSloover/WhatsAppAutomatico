"""encuentra la posicion del maus"""
import pyautogui
import time

print("Pulsa Ctrl-C para capturar la posicion del mouse.")

try:
    while True:
        x, y=pyautogui.position()
        position_str = f"x: {x}, Y: {y}"
        print(position_str, end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:

    
    print("\n Cordenadas copiadas")