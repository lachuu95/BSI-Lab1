# BSI-Lab1
Bezpieczństwo Systemów Informatycznych
- Lab-1 szyfrowanie i deszyfrowanie tekstu i plików
## Przygotownaie środowiska
```bash
$ python3 -m venv .env
```
```bash
$ python3 -m venv .env
```
```bash
$ . .env/bin/scripts
```
```bash
$ pip install -U -r requirements.txt
```
## Uruchomienie serwera mySQL
```bash
$ cd resource/
```
```bash
$ docker-compose up
```
## Użycie
```bash
$ ./src/scripts/runnme.py "Lorem ipsum dolor sit amet, consectetur adipiscing elit." "resource/image.jpg"
```
## Obsługa serwera mySQL
- logowanie do serwera
```bash
$ mysql -u qwerty -p -h 127.0.0.1 -P 3306
```
- wejście do bazy danych datadb
```sql
USE datadb;
```
- wyświetlenie wszystkich tabel w bazie danych
```sql
SHOW TABLES;
```
- wyświetlenie parametrów tabeli data_table.
```sql
DESCRIBE data_table;
```
- wybranie wszystkich rekordów z tabeli data_table.
```sql
SELECT * FROM data_table;
```
- usunięcie tabeli data_table;
```sql
DROP TABLE data_table;
```
- wyświetlenie wszystkich rekordów (tylko 3 pierwsze znaki z kolumny data)
```sql
SELECT Id, LEFT(Data , 3) FROM data_table;
```