f_input = open('input.txt', 'r')
f_output = open('output.txt', 'w')

# 첫 줄은 그대ㅡ로 출력 ^^
line = f_input.readline().replace('\n', '')
f_output.write(line)

flight_time = line.split('/ ', 1)[1].split(':')

flight_hour = int(flight_time[0])
flight_minute = int(flight_time[1])

while True:
    line = f_input.readline().replace('\n', '')

    # 더 이상 읽을 줄이 없으면 반복문 종료
    if not line: break

    take_off_time = line.split(':')

    take_off_hour = int(take_off_time[0])
    take_off_minute = int(take_off_time[1])

    landing_hour = take_off_hour + flight_hour
    landing_minute = take_off_minute + flight_minute

    # 시간은 00~23, 분은 00~59, 2자리씩 출력이므로
    if landing_minute >= 60:
        landing_hour += 1
        landing_minute -= 60
    
    if landing_minute < 10:
        landing_minute = '0' + str(landing_minute)
    else:
        landing_minute = str(landing_minute)
        

    if landing_hour >= 24:
        landing_hour -= 24

    if landing_hour < 10:
        landing_hour = '0' + str(landing_hour)
    else:
        landing_hour = str(landing_hour)


    f_output.write('\n' + landing_hour + ':' + landing_minute)

f_input.close()
f_output.close()