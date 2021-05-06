import time
#ааааа трындец сложнА
def timer(seconds):
    timenow=time.asctime()
    timee=[int(timenow[11]+timenow[12]),int(timenow[14]+timenow[15]),int(timenow[17]+timenow[18])]
    timee[2]+=seconds
    if timee[2]>59:
        timee[1]+=1
        timee[2]-=60
        if timee[1]>59:
            timee[0]+=1
            if time[0]>23:
                timee[0]=00
    for i in range(len(timee)):
        timee[i]=str(timee[i])
        if len(timee[i])==1:
            timee[i]="0"+timee[i]
    while 1:
        timenow=time.asctime()
        if timenow[11]+timenow[12]+timenow[14]+timenow[15]+timenow[17]+timenow[18]==timee[0]+timee[1]+timee[2]:
            break
#ураааа час спустя я это сделал
