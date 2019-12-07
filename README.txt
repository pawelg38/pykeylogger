# pykeylogger
Prosty keylogger napisany w języku python

Zadaniem programu jest rejestrowanie wciskanych klawiszy na klawiaturze przez użytkownika systemu.
W momencie uruchomienia tworzony jest plik o nazwie "newLogs". W nim zapisywane są wszystkie zarejestrowane wciśnięcia klawiszy.
Po zamknięciu programu i ponownym uruchomieniu, program sprawdza czy istniały wcześniej zapisane pliki z logami do 7dni wstecz.
Jeśli tak to wysyła je na wskazany w kodzie źródłowym adres email, po czym usuwa je z dysku oraz opróżnia kosz.
Program staje się samodzielny po konfiguracji w systemie tak aby uruchamiał się wraz z nim.

Program działa w tle i jest widoczny wśród listy procesów użytkownika.

Przykładowa linia zapisana w pliku z logami według schematu: data godzina: 'klawisz'
2018-12-07 22:37:46,851: 'z'
