import threading
import time 
def hola_mundo(nombre):
    print("hola mundo"+ nombre)
    time.sleep(4)

if __name__ == '__main__':

        hilo1 = threading.Thread(target=hola_mundo, args=("Luis",)) 
        hilo1.start()
        hilo2 = threading.Thread(target=hola_mundo, args=("Ana",))
        hilo2.start()
        hilo3 = threading.Thread(target=hola_mundo, args=("roberto",))
        hilo3.start()
    
   