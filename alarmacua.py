import datetime
import time
from plyer import notification

def tomar_tiempo():
    """Toma la hora actual del sistema."""
    tiempo_actual = datetime.datetime.now().strftime("%H:%M:%S")
    return tiempo_actual

def mostrar_mensaje():
    """Muestra una ventana emergente con el mensaje '¡Hora de despertar!'."""
    notification.notify(title="Alarma", message="¡Hora de despertar!", timeout=10)

def alarma(hora, dias):
    """Configura la alarma para que muestre un mensaje en una hora y días específicos."""
    while True:
        tiempo_actual = tomar_tiempo()
        dia_actual = datetime.datetime.now().strftime("%A")
        if tiempo_actual == hora and dia_actual in dias:
            mostrar_mensaje()
            break
        elif tiempo_actual != hora and dia_actual in dias:
            print(f"La hora actual es {tiempo_actual}. La alarma está programada para sonar a las {hora}.")
        else:
            print(f"Es {dia_actual} y la alarma no está programada para hoy.")
        time.sleep(60)

# Configura la hora y los días de la alarma
hora_alarma = "12:00:00"
dias_alarma = ["Monday", "Tuesday"]

# Inicia la alarma
alarma(hora_alarma, dias_alarma)


