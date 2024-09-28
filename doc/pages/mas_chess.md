## Functions

### def isInProgressGame(filename, mth)

Checks if the pgn game with the given filename is valid and in progress.

**Parameters:**
- `filename` &mdash; filename of the pgn game
- `mth` &mdash; monika twitter handle. pass it in since I'm too lazy to find context from a store


**Returns:**<br>
tuple of the following format: [0]: Text to display on button [1]: chess.pgn.Game of the game OR NONE if this is not a valid pgn game

---

### def select_piece(remaining_points, selected_pieces_count_dict)

Selects a piece according to random

**Parameters:**
- `remaining_points` &mdash; amount of points left to be allocated


**Returns:**<br>
a chess piece (str) based on available

---

### def generate_random_fen(is_player_white=True)

Generates a random fen

**Parameters:**
- `is_player_white` &mdash; whether or not the player is playing white this game


---

### def generate_960_fen()

This function returns a random chess960 opening fen.  Chess960 rules are basically: 1. One rook must stay on the left side of king, and another one stay on the right side. Due to this, the king can never be placed on a-file or h-file. 2. Bishops must stay on different color square. 3. Pawns must stay like the normal chess game. 4. The position of player A's pieces must be the 'reversed version' of player B's. See chess960 wiki to get more exact information.

**Returns:**<br>
A random chess960 opening fen.

---

### def enqueue_output(out, queue, lock)

---

### def isInProgressGame(filename, mth)

Checks if the pgn game with the given filename is valid and in progress.

**Parameters:**
- `filename` &mdash; filename of the pgn game
- `mth` &mdash; monika twitter handle. pass it in since I'm too lazy to find context from a store


**Returns:**<br>
tuple of the following format: [0]: Text to display on button [1]: chess.pgn.Game of the game OR NONE if this is not a valid pgn game

---

### def select_piece(remaining_points, selected_pieces_count_dict)

Selects a piece according to random

**Parameters:**
- `remaining_points` &mdash; amount of points left to be allocated


**Returns:**<br>
a chess piece (str) based on available

---

### def generate_random_fen(is_player_white=True)

Generates a random fen

**Parameters:**
- `is_player_white` &mdash; whether or not the player is playing white this game


---

### def generate_960_fen()

This function returns a random chess960 opening fen.  Chess960 rules are basically: 1. One rook must stay on the left side of king, and another one stay on the right side. Due to this, the king can never be placed on a-file or h-file. 2. Bishops must stay on different color square. 3. Pawns must stay like the normal chess game. 4. The position of player A's pieces must be the 'reversed version' of player B's. See chess960 wiki to get more exact information.

**Returns:**<br>
A random chess960 opening fen.

---

### def enqueue_output(out, queue, lock)

---

### Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

#### def _checkInProgressGame(pgn_game, mth)

Checks if the given pgn game is valid and in progress.

**Parameters:**
- `pgn_game` &mdash; pgn game to check
- `mth` &mdash; monika twitter handle. pass it in since I'm too lazy to find context from a store


**Returns:**<br>
SEE isInProgressGame

---

#### def _increment_chess_difficulty()

Increments chess difficulty

---

#### def _decrement_chess_difficulty()

Decrements chess difficulty

---

#### def _get_player_color(loaded_game)

Gets player color

**Parameters:**
- `loaded_game` &mdash; pgn representing the loaded game


**Returns:**<br>
The player's color

---

#### def _get_piece_chance(piece_type, selected_pieces_count_dict, available_points)

Gets the piece chance and returns the piece and weight in tuple form for a `mas_utils.weightedChoice` selection

**Parameters:**
- `piece_type` &mdash; type of the piece ('b', 'r', 'n', 'q')


**Returns:**<br>
tuple - (piece_type, weight) of the piece

---

#### def _gen_side(white=True, max_side_value=14)

Generates a player's side

**Parameters:**
- `white` &mdash; whether or not we should generate for white (Default: True)
- `max_side_value` &mdash; The current upper limit for piece selection (Default: 14 -- minimum weight, most pieces are pawns)


**Returns:**<br>
2 strings representing a random assortment of pieces (front row and back row)

---

#### def _validate_sides(white_front, white_back, black_front, black_back)

Validates sides for really bad chess so we don't end up in a check/check mate after the first turn

**Parameters:**
- `white_front` &mdash; front row for white
- `white_back` &mdash; back row for white
- `black_front` &mdash; front row for black
- `black_back` &mdash; back row for black


**Returns:**<br>
boolean, whether or not both sides are good to go

---

#### def _checkInProgressGame(pgn_game, mth)

Checks if the given pgn game is valid and in progress.

**Parameters:**
- `pgn_game` &mdash; pgn game to check
- `mth` &mdash; monika twitter handle. pass it in since I'm too lazy to find context from a store


**Returns:**<br>
SEE isInProgressGame

---

#### def _increment_chess_difficulty()

Increments chess difficulty

---

#### def _decrement_chess_difficulty()

Decrements chess difficulty

---

#### def _get_player_color(loaded_game)

Gets player color

**Parameters:**
- `loaded_game` &mdash; pgn representing the loaded game


**Returns:**<br>
The player's color

---

#### def _get_piece_chance(piece_type, selected_pieces_count_dict, available_points)

Gets the piece chance and returns the piece and weight in tuple form for a `mas_utils.weightedChoice` selection

**Parameters:**
- `piece_type` &mdash; type of the piece ('b', 'r', 'n', 'q')


**Returns:**<br>
tuple - (piece_type, weight) of the piece

---

#### def _gen_side(white=True, max_side_value=14)

Generates a player's side

**Parameters:**
- `white` &mdash; whether or not we should generate for white (Default: True)
- `max_side_value` &mdash; The current upper limit for piece selection (Default: 14 -- minimum weight, most pieces are pawns)


**Returns:**<br>
2 strings representing a random assortment of pieces (front row and back row)

---

#### def _validate_sides(white_front, white_back, black_front, black_back)

Validates sides for really bad chess so we don't end up in a check/check mate after the first turn

**Parameters:**
- `white_front` &mdash; front row for white
- `white_back` &mdash; back row for white
- `black_front` &mdash; front row for black
- `black_back` &mdash; back row for black


**Returns:**<br>
boolean, whether or not both sides are good to go

---

