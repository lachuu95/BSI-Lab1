# BSI-Lab1
Bezpieczństwo Systemów Informatycznych
- Lab-1 szyfrowanie i deszyfrowanie tekstu i plików
---
## Przygotownaie środowiska
- Unix
    ```console
    $ python3 -m venv .env
    ```
    ```console
    $ . .env/bin/activate
    ```
    ```console
    (.env)$ pip install -U -r requirements.txt -r test-requirements.txt
    ```
- Win
    ```powershell
    > python -m venv .env
    ```
    ```powershell
    > .\.env\Scripts\Activate.ps1
    ```
    ```powershell
    (.env)> pip install -U -r .\requirements.txt -r .\test-requirements.txt
    ```
---
## Użycie
- Unix
    ```console
    $ ./src/scripts/runnme.py "Lorem ipsum dolor sit amet, consectetur adipiscing elit." "resource/image.jpg"
    ```
- Win
    ```powershell
    > python .\src\scripts\runnme.py "Lorem ipsum dolor sit amet, consectetur adipiscing elit." .\resource\image.jpg
    ```
---
## Uruchomienie testów
- Testy
    ```powershell
    (.env)> pytest
    ```
- Pokrycie kodu testami
    ```powershell
    (.env)> pytest --cov-report term --cov=src
    ```
