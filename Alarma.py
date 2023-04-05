import datetime
import time
import threading

class Alarm(threading.Thread):
    def __init__(self, alarm_time, recurr_list):
        super().__init__()
        self.alarm_time = alarm_time
        self.recurr_list = recurr_list
        self.stop_event = threading.Event()

    def run(self):
        print("La alarma se ha configurado para sonar a las", self.alarm_time, "en los siguientes días:", self.recurr_list)
        while not self.stop_event.is_set():
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            current_day = datetime.datetime.now().strftime("%A").lower()
            print("La hora actual es", current_time, "y el día actual es", current_day)
            if current_time == self.alarm_time and current_day in self.recurr_list:
                print("¡Despierta! Es hora de levantarse.")
                self.stop()
            else:
                time.sleep(1)

    def stop(self):
        self.stop_event.set()

def set_alarm():
    while True:
        try:
            alarm_time = input("Ingrese la hora en formato HH:MM:SS: ")
            datetime.datetime.strptime(alarm_time, "%H:%M:%S")
            return alarm_time
        except ValueError:
            print("Hora inválida. Intente nuevamente.")

def set_recurr():
    while True:
        try:
            days = input("Ingrese los días de la semana en formato abreviado separados por comas (por ejemplo, lun,mar,mie,jue,vie,sab,dom): ")
            recurr_list = [d.strip().lower() for d in days.split(',')]
            for day in recurr_list:
                if day not in ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']:
                    raise ValueError
            return recurr_list
        except ValueError:
            print("Días inválidos. Intente nuevamente.")

def main():
    print("Configuración de alarma")
    alarm_time = set_alarm()
    recurr_list = set_recurr()
    print("La alarma está configurada para sonar a las", alarm_time, "en los siguientes días:", recurr_list)

    alarm = Alarm(alarm_time, recurr_list)
    alarm.start()

    while True:
        try:
            time.sleep(1)
            print("La alarma está en ejecución:", alarm.is_alive())
        except KeyboardInterrupt:
            print("Deteniendo la alarma...")
            alarm.stop()
            break

if __name__ == '__main__':
    main()
