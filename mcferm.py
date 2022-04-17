import time
from pynput.mouse import Button, Controller

mouse = Controller()
cikls=1

#ievade
#delay
print('Gaidīšana starp sitieniem(sekundēs): ')
while(1<2):
    delay=input('>')
    if '.' in delay:
        delays=delay.split('.')

        if delays[0].isdigit() and delays[1].isdigit():
            if float(delay)>0:
                break

            else:
                print('nepareiza ievade!')
        else:
            print('nepareiza ievade!')

    else:
        if delay.isdigit():
            if float(delay) > 0:
                break

            else:
                print('nepareiza ievade!')
        else:
            print('nepareiza ievade!')

#ieroca veids
print('ieroča veids: ')
print('zobens(1)')
print('roka(2)')
print('cirvis(3)')
while(1<2):
    veids=input('>')
    if veids=='1':
        veids=0.625
        break

    elif veids=='2':
        veids=0.3
        break

    elif veids=='3':
        veids=1.25
        break

    else:
        print('nepareiza ievade!')

#sisanas ilgums
print('sišanas reizes')
while(1<2):
    reizes=input('>')
    if reizes.isdigit():
        if int(reizes)>0:
            break

        else:
            print('nepareiza ievade!')

    else:
        print('nepareiza ievade!')



#automatika
print('sāksies pēc 5 sekundēm')
time.sleep(5)

tgtlaiks=time.localtime()
tgtlaiksf=time.strftime("%H:%M:%S", tgtlaiks)
print('{}. cikls'.format(cikls) + '('+tgtlaiksf+')')
while(1<2):

    i=int(reizes)
    while(i>0):
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(float(veids))
        i=i-1

    time.sleep(float(delay))
    cikls = cikls + 1
    tgtlaiks=time.localtime()
    tgtlaiksf=time.strftime("%H:%M:%S", tgtlaiks)
    print('{}. cikls'.format(cikls) + '('+tgtlaiksf+')')