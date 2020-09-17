# Game Time with Minutes

time_game = input().split(' ')

initial_hour = float(time_game[0])
initial_minute = float(time_game[1])
final_hour = float(time_game[2])
final_minute = float(time_game[3])

if initial_hour > final_hour:
    playing_minutes = (((24 - initial_hour) + final_hour)*60)+(60-initial_minute)+final_minute
else:
    playing_minutes = ((final_hour - initial_hour)*60)+(60-initial_minute)+final_minute

# Converter:
playing_hour = playing_minutes/60
resting_time = playing_minutes - (playing_hour*60)

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(playing_hour, resting_time))

