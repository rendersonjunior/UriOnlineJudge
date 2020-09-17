# Event Time
import datetime


def main():
    ini_event_day = int(str(input()).replace('Dia ', ''))
    ini_event_hour = input().replace(' ', '').split(':')
    fin_event_day = int(str(input()).replace('Dia ', ''))
    fin_event_hour = input().replace(' ', '').split(':')

    # Processo para transformar para date e time
    aux_date = datetime.date(1, 4, ini_event_day)
    aux_hour = datetime.time(int(ini_event_hour[0]), int(ini_event_hour[1]), int(ini_event_hour[2]))
    date_initial = datetime.datetime.combine(aux_date, aux_hour)

    # Processo para transformar para date e time
    aux_date = datetime.date(1, 4, fin_event_day)
    aux_hour = datetime.time(int(fin_event_hour[0]), int(fin_event_hour[1]), int(fin_event_hour[2]))
    date_final = datetime.datetime.combine(aux_date, aux_hour)

    difference_time = (date_final - date_initial)

    # Para calculo de hora
    x_date = datetime.date(1, 1, 1)
    x_hour = datetime.time(0, 0, 0)
    date_pivot = datetime.datetime.combine(x_date, x_hour)

    # Obtem hora
    time = date_pivot + difference_time

    print("%d dia(s)" % difference_time.days)
    print("%d hora(s)" % time.hour)
    print("%d minuto(s)" % time.minute)
    print("%d segundo(s)" % time.second)

if __name__ == "__main__":
    main()
