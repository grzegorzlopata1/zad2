# Wykorzystaj oficjalny obraz Python w wersji 3.9
FROM python:3.9

# Dodanie informacji o autorze pliku
LABEL author="Grzegorz Lopata"

# Skopiuj plik z kodem aplikacji do kontenera
COPY serwer.py /app/serwer.py

# Ustaw katalog roboczy
WORKDIR /app

# Zainstaluj zależności
RUN pip install datetime

# Uruchom aplikację
CMD ["python", "serwer.py"]
