# Tic Tac Toe - Gra w Kółko i Krzyżyk

## Opis
Gra w Kółko i Krzyżyk stworzona w Pythonie z wykorzystaniem biblioteki **pygame**. Gracz mierzy się z komputerem sterowanym przez algorytm **Minimax** (z wbudowaną losowością, aby był mniej przewidywalny).

---

## Jak grać? 
1. Uruchom grę za pomocą Pythona.
2. Gracz **X** zaczyna pierwszy.
3. Kliknij w puste pole, aby postawić "X".
4. Komputer (grający "O") wykona swój ruch automatycznie.
5. Gra kończy się, gdy:
   - Jeden z graczy ułoży trzy symbole w rzędzie, kolumnie lub na ukos.
   - Nie ma dostępnych ruchów (remis).
6. Po zakończeniu rundy wynik zostanie wyświetlony, a gra automatycznie zrestartuje się po 2 sekundach.

---

## Instalacja i uruchomienie 
### Wymagania:
- **Python 3**
- **pygame**

### Instalacja pygame:
```bash
pip install pygame
```

### Uruchomienie gry:
```bash
python tic_tac_toe.py
```

---

## Struktura kodu 
### Kluczowe funkcje:
- **drawGrid()** – rysuje siatkę planszy 3x3.
- **draw_symbol(x, y, player)** – rysuje "X" lub "O" na planszy.
- **check_winner()** – sprawdza, czy ktoś wygrał lub czy jest remis.
- **minimax(board, depth, is_maximizing)** – algorytm Minimax do podejmowania decyzji przez AI.
- **best_move()** – wybiera najlepszy ruch dla AI (czasami popełnia losowy błąd).
- **show_winner_screen(text)** – wyświetla ekran końcowy z wynikiem.

---

## Mechanika AI 
Komputer korzysta z algorytmu **Minimax**, aby analizować możliwe ruchy i wybierać najlepsze decyzje. Jednak aby był mniej przewidywalny:
- **20% szans na błąd** – AI czasem wybiera losowy ruch zamiast najlepszego.
- **Przewidywanie tylko na kilka ruchów wprzód** – zmniejsza trudność gry.

---

## Możliwe ulepszenia
- Tryb multiplayer (gra przeciwko drugiemu graczowi) 
- Interfejs graficzny z menu startowym 
- Poziomy trudności dla AI 

---

## Autor 
Projekt stworzony przez Magdalena Marszałek 


