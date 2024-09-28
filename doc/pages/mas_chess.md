## Functions

### def isInProgressGame(filename, mth)

Checks if the pgn game with the given filename is valid and in progress.

**Parameters:**
- `filename` &mdash; filename of the pgn game
- `mth` &mdash; monika twitter handle. pass it in since I'm too lazy to find context from a store


**Returns:**<br>
tuple of the following format: [0]: Text to display on button [1]: chess.pgn.Game of the game OR NONE if this is not a valid pgn game

### def select_piece(remaining_points, selected_pieces_count_dict)

Selects a piece according to random

**Parameters:**
- `remaining_points` &mdash; amount of points left to be allocated


**Returns:**<br>
a chess piece (str) based on available

### def generate_random_fen(is_player_white=True)

Generates a random fen

**Parameters:**
- `is_player_white` &mdash; whether or not the player is playing white this game


### def generate_960_fen()

This function returns a random chess960 opening fen.  Chess960 rules are basically: 1. One rook must stay on the left side of king, and another one stay on the right side. Due to this, the king can never be placed on a-file or h-file. 2. Bishops must stay on different color square. 3. Pawns must stay like the normal chess game. 4. The position of player A's pieces must be the 'reversed version' of player B's. See chess960 wiki to get more exact information.

**Returns:**<br>
A random chess960 opening fen.

### def enqueue_output(out, queue, lock)

### def isInProgressGame(filename, mth)

Checks if the pgn game with the given filename is valid and in progress.

**Parameters:**
- `filename` &mdash; filename of the pgn game
- `mth` &mdash; monika twitter handle. pass it in since I'm too lazy to find context from a store


**Returns:**<br>
tuple of the following format: [0]: Text to display on button [1]: chess.pgn.Game of the game OR NONE if this is not a valid pgn game

### def select_piece(remaining_points, selected_pieces_count_dict)

Selects a piece according to random

**Parameters:**
- `remaining_points` &mdash; amount of points left to be allocated


**Returns:**<br>
a chess piece (str) based on available

### def generate_random_fen(is_player_white=True)

Generates a random fen

**Parameters:**
- `is_player_white` &mdash; whether or not the player is playing white this game


### def generate_960_fen()

This function returns a random chess960 opening fen.  Chess960 rules are basically: 1. One rook must stay on the left side of king, and another one stay on the right side. Due to this, the king can never be placed on a-file or h-file. 2. Bishops must stay on different color square. 3. Pawns must stay like the normal chess game. 4. The position of player A's pieces must be the 'reversed version' of player B's. See chess960 wiki to get more exact information.

**Returns:**<br>
A random chess960 opening fen.

### def enqueue_output(out, queue, lock)

