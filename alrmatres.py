import threading
import time

def get_alarm_time():
    valid_input = False
    while not valid_input:
        alarm_time = input("Ingresa la hora de la alarma (formato HH:MM): ")
        try:
            hours, minutes = alarm_time.split(":")
            hours = int(hours)
            minutes = int(minutes)
            if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
                print("Hora de alarma inválida. Inténtalo de nuevo.")
            else:
                valid_input = True
        except ValueError:
            print("Formato de hora de alarma inválido. Inténtalo de nuevo.")
    return (hours, minutes)

def get_alarm_days():
    days = input("Ingresa los días de la semana en los que quieres que suene la alarma (separados por comas): ")
    days = [d.strip().capitalize() for d in days.split(",")]
    valid_days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for day in days:
        if day not in valid_days:
            print("Día de la semana inválido. Inténtalo de nuevo.")
            return get_alarm_days()
    return days

def alarm():
    print("¡¡¡Alarma activada!!!")
    for i in range(5):
        print("\a")
        time.sleep(1)

def main():
    alarm_time = get_alarm_time()
    alarm_days = get_alarm_days()

    now = time.localtime()
    weekday = time.strftime("%A", now)
    while weekday not in alarm_days:
        print("Es", weekday, "y la alarma no está programada para hoy.")
        time.sleep(60)
        now = time.localtime()
        weekday = time.strftime("%A", now)

    alarm_time_struct = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, alarm_time[0], alarm_time[1], 0, now.tm_wday, now.tm_yday, now.tm_isdst))
    alarm_timestamp = time.mktime(alarm_time_struct)

    print("Alarma programada para las", alarm_time[0], ":", alarm_time[1], "en los días:", alarm_days)

    # Creamos dos hilos para manejar la alarma y la entrada del usuario en paralelo
    alarm_thread = threading.Thread(target=alarm)
    alarm_thread.start()

    input_thread = threading.Thread(target=input, args=("Presiona enter para cancelar la alarma",))
    input_thread.start()

    # Esperamos hasta que la alarma suene o se cancele
    while True:
        if not alarm_thread.is_alive():
            input_thread.join()
            break
        time.sleep(1)

    print("Alarma cancelada")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario") 
