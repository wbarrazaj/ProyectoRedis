Comando =  'redis-cli'
Servidor =  "Aquiles"
Usuario = "monitor"
Clave = "Emilita01"
Puerto = 6379
Comando_REDIS = "INFO MEMORY"
Comando_REDIS_Split  = Comando_REDIS.split()

mensaje = [Comando,"-h", Servidor, "--user",Usuario, "--pass",Clave ,"-p" ,str(Puerto)]

print(mensaje)

#mensaje2 = Comando_REDIS.split()

for xx_comando in Comando_REDIS_Split :
    mensaje.append(xx_comando)

print(mensaje)
