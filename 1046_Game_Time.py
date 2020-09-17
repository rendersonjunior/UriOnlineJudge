# Game Time

hours_in_game = input().split(' ')

initiated_hour, finished_hour = hours_in_game

initiated_hour = int(initiated_hour)
finished_hour = int(finished_hour)

if initiated_hour > finished_hour:
    # Passou para o 2º dia
    playing_time = (24 - initiated_hour) + finished_hour
else:
    # Finalizou no mesmo dia
    playing_time = finished_hour - initiated_hour
    if playing_time == 0:
        playing_time = 24

print("O JOGO DUROU %d HORA(S)"%(playing_time))