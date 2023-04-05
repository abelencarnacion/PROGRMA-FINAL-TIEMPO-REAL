import datetime
import time
import winsound

def pedir_dias():
    while True:
        dias = input("Ingrese los días de la semana separados por comas (por ejemplo, lunes,martes,miercoles,jueves,viernes,sabado,domingo): ").lower().replace(" ", "").split(",")
        if all(dia in ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"] for dia in dias):
            return dias
        else:
            print("Días inválidos. Intente nuevamente.")
            
def pedir_hora():
    while True:
        hora = input("Ingrese la hora en formato hh:mm:ss: ")
        try:
            hora_dt = datetime.datetime.strptime(hora, '%H:%M:%S').time()
            return hora_dt
        except ValueError:
            print("Hora inválida. Intente nuevamente.")

def activar_alarma(dias, hora):
    while True:
        hoy = datetime.datetime.now().date()
        hora_actual = datetime.datetime.now().time()
        if hora_actual >= hora:
            # si ya pasó la hora de la alarma, se setea para el día siguiente
            hoy = hoy + datetime.timedelta(days=1)
        if hoy.strftime("%A").lower() in dias:
            print("¡Despierta! Sonó la alarma.")
            winsound.Beep(440, 1000)  # suena una nota musical
            break
        # espera 1 minuto antes de volver a comprobar si se debe activar la alarma
        time.sleep(60)

if __name__ == '__main__':
    print("Configuración de alarma")
    dias = pedir_dias()
    hora = pedir_hora()
    print("Alarma programada para sonar a las", hora.strftime('%H:%M:%S'), "los días", ", ".join(dias))
    activar_alarma(dias, hora)
lunes