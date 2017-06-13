def parse_time(a):
    b = a.split(':')
    return [int(b[0]), int(b[1])]

def read_line(a):
    return a.readline().replace('\n', '')

def digit(a):
    if a < 10:
        a = '0' + str(a)
    else:
        a = str(a)
    return a

finput = open('input.txt', 'r')
foutput = open('output.txt', 'w')

line = read_line(finput)
foutput.write(line)

flight_time = parse_time(line.split('/')[1])

while True:
    line = read_line(finput)

    if not line:
        break

    take_off_time = parse_time(line)

    arrival_time = [take_off_time[0] + flight_time[0], take_off_time[1] + flight_time[1]]

    if arrival_time[1] > 59:
        arrival_time[0] += 1
        arrival_time[1] -= 60

    if arrival_time[0] > 23:
        arrival_time[0] -= 24

    foutput.write('\n' + digit(arrival_time[0]) + ':' + digit(arrival_time[1]))