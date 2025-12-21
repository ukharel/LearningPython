import time


myTime = int(input('Enter a time in seconds: '))

for i in range(myTime,0,-1):
    seconds= i % 60
    minutes= int(i / 60) % 60
    hours = int(i/3600)

    print(f'{hours}:{minutes}:{seconds:02}')
    time.sleep(1)

print('Bang Bang!!!')