import subprocess
import sys

#home_dir = os.system("pwd")

#print(home_dir)


result = subprocess.Popen(["redis-cli", "INFO","MEMORY"], text=True,stdout=subprocess.PIPE)

#print("stdout:", result.stdout)

i=0
for linea in result.stdout :   
    if i>0 :
        Parametros,Values = linea.rstrip().split(":")
        print (str(i)+") Paramtros " + Parametros + " : " + Values )
        i+=1
    else : 
        i+=1



