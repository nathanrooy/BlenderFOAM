#---NOTES-----------------------------
#
#   Collects the exit pressure value
#
#------------------------------------

def main(foldername_new):
    from numpy import loadtxt
    from numpy import std
    global value
    answer=[]
    
    # Collect outlet velocity data
    magU=[]    
    Ux,Uy,Uz = loadtxt(foldername_new+'/surfaces2/300/U_abOutlet.raw',unpack=True, usecols=[3,4,5])
    
    for i in range(len(Ux)):
        if Ux[i]!=0 and Uy[i]!=0 and Uz[i]!=0:
            magU.append((Ux[i]**2)+(Uy[i]**2)+(Uz[i]**2))
    SD_magU=std(magU)

    #collect inlet pressure data
    i=0
    pData=open(foldername_new+'/'+'pInlet.txt','r')         # open txt file
    lines=pData.read()                              # transfer text file into string
    for i in range(len(lines)):                     # scan text file
        if lines[i]==']' and lines[i+1]==' ' and lines[i+2]=='=':   # look for "] = "
            value=float(str(lines[i+4])+str(lines[i+5])+str(lines[i+6])+str(lines[i+7])+str(lines[i+8])+str(lines[i+9])+str(lines[i+10])) # save value
        i=i+1
        pData.close()

    answer.append(SD_magU)  # answer[0] = Standard deviation
    answer.append(value)    # answer[1] = pressure value
    
    return answer
