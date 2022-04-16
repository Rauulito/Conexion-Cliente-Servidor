import socket

#iniciamos al servidor

host = socket.gethostname() # Esta función nos da el nombre de la máquina
port = 12345
BUFFER_SIZE = 1024 # Usamos un número pequeño para tener una respuesta rápida

# Creamos un objeto socket tipo TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:

    socket_tcp.bind((host, port))
    socket_tcp.listen(5) # Esperamos la conexión del cliente
    conn, addr = socket_tcp.accept() # Establecemos la conexión con el cliente
    with conn:
        print('[*] Conexión establecida')
        while True:
            # Recibimos bytes, convertimos en str
            data = conn.recv(BUFFER_SIZE)
            # Verificamos que hemos recibido datos
            if not data:
                break
            #como la conexión ha sido establecida, es decir, recibe peticiones de conexión, devolvemos valores correspondintes(float)
            temperatura_minima = float(input("Temperatura minima:"))
            temperatura_maxima = float(input("Temperatura máxima:"))
            presion = float(input("Presión:"))
            plumiometría = float(input("Pluviometría:"))
            else:
                print('[*] Datos recibidos: {}'.format(data.decode('utf-8')))
            conn.send(data) # Hacemos echo convirtiendo de nuevo a bytes

