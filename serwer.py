import socket
import datetime

# Ustawienia serwera
HOST = '0.0.0.0'  # Adres IP na którym serwer nasłuchuje
PORT = 12345

# Inicjalizacja gniazda serwera
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

# Wyświetlenie informacji o uruchomieniu serwera
print('Serwer uruchomiony przez: Grzegorz Łopata')
print(f'Nasłuchiwanie na porcie {PORT}')

# Pętla nasłuchująca na połączenia
while True:
    # Akceptowanie połączenia
    conn, addr = s.accept()
    print(f'Połączenie z {addr}')

    # Pobranie daty i czasu dla strefy czasowej klienta
    now = datetime.datetime.now()
    client_time = now.astimezone(datetime.timezone(datetime.timedelta(hours=+1)))

    # Przygotowanie strony HTML z informacją o adresie IP i czasie
    response = f"""<html><body><h1>Adres IP klienta: {addr[0]}</h1>
                  <p>Czas w strefie czasowej klienta: {client_time}</p></body></html>"""

    # Wysłanie strony HTML do klienta
    conn.sendall(b'HTTP/1.0 200 OK\r\n')
    conn.sendall(b'Content-Type: text/html\r\n')
    conn.sendall(b'\r\n')
    conn.sendall(bytes(response, 'utf-8'))

    # Zamknięcie połączenia
    conn.close()
