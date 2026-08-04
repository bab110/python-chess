### 5.2.1 Input Domain Modeling Test Cases

#### **5.2.1.1	Get Chebyshev Distance IDM Test Cases**

**Function:** `def square_distance(a: Square, b: Square) -> int`

This function calculates the Chebyshev distance (i.e. the number of king steps) between two chessboard spaces. It determines the distance by comparing the file and rank differences for the two squares and returns the larger number.

**List of Input Variables**

| Input Variable   |  Type  |       Definition       |
| ---------------- | ------ | ---------------------- |
|  a  | Square |The starting square on the chessboard. |
|  b  | Square | The ending square on the chessboard.|

**Characteristics of Input Variables:**

| Variable   |  Characteristics    |
| ---------  | ------- |
|  a  | Is Square a the same as Square b? Is the input an integer? Is the square valid? Is the square rank the same as Square b? Is the square file the same as Square b? |
|  b  | Is Square b the same as Square a? Is the input an integer? Is the square valid? Is the square rank the same as Square a? Is the square file the same as Square a? |

**Partition the Characteristics into Blocks and Define Values:**
| Characteristic   |  b1   | b2 | b3 | b4 |
| ---------  | ------- |---------  | ------- |---------  |
|  q1 = “range of square a” | < 0 (invalid) | 0-63 (valid) | > 63 (invalid) | - |
|  q2 = “range of square b”  | < 0 (invalid) | 0-63 (valid) | > 63 (invalid) | - |
|  q3 = “relative position of a and b” | same square | same rank | same file | different rank and file |
|  q4 = “comparison of dx and dy” | dx > dy | dx = dy | dx < dy | - |

**Coverage Criteria:**

Base Choice Coverage (BCC) was chosen since I’m able to change one characteristic at a time while also keeping the other characteristics at their base value, for instance the base value for q1 and q2 would be 0-63(valid).

**Test Set Definition:**
| Test ID | Description |  q1   | q2 | q3 | q4 |
| --------| ------- |---------  | ------- | --------- | ---------  |
|  IDM-SD-01 | Test both a valid Square a and Square b with default. | 0-63 | 0-63 | different rank and file | dx = dy |
|  IDM-SD-02  | Test an invalid Square a that is below 0. | < 0 | 0-63 | different rank and file | dx = dy | 
|  IDM-SD-03 | Test an invalid Square a that is above chess.H8 or 63. | > 63 | 0-63 | different rank and file | dx = dy | 
|  IDM-SD-04 | Test an invalid Square b that is below 0. | 0-63 | < 0 | different rank and file | dx = dy | 
|  IDM-SD-05 | Test an invalid Square b that is above chess.H8 or 63. | 0-63 | > 63 | different rank and file | dx = dy | 
|  IDM-SD-06 | Test a valid Square a and Square b where they have the same square. | 0-63 | 0-63 | same square | dx = dy | 
|  IDM-SD-07 | Test a valid Square a and Square b where they have the same rank. | 0-63 | 0-63 | same rank | dx = dy | 
|  IDM-SD-08 | Test a valid Square a and Square b where they have the same file. | 0-63 | 0-63 | same file | dx = dy | 
|  IDM-SD-09 | Test a valid Square a and Square b where dx > dy. | 0-63 | 0-63 | different rank and file | dx > dy | 
|  IDM-SD-10 | Test a valid Square a and Square b where dx < dy. | 0-63 | 0-63 | different rank and file | dx < dy | 

**Test Results:**
| Test ID | Description |  Input Blocks   | Expected Output | Test Result | 
| --------| ------- |---------  | ------- | --------- | 
|  IDM-SD-01 | Test both a valid Square a and Square b with default. | q1b2, q2b2, q3b4, q4b2 | 7 | Pass |
|  IDM-SD-02  | Test an invalid Square a that is below 0. | q1b1, q2b2, q3b4, q4b2 | Invalid Square | Needs follow up | 
|  IDM-SD-03 | Test an invalid Square a that is above chess.H8 or 63. | q1b3, q2b2, q3b4, q4b2 | Attribute Error | Needs follow up | 
|  IDM-SD-04 | Test an invalid Square b that is below 0. | q1b2, q2b1, q3b4, q4b2 | Invalid Square | Needs follow up | 
|  IDM-SD-05 | Test an invalid Square b that is above chess.H8 or 63. | q1b2, q2b3, q3b4, q4b2 | Attribute Error | Needs follow up | 
|  IDM-SD-06 | Test a valid Square a and Square b where they have the same square. | q1b2, q2b2, q3b1, q4b2 | 0 | Pass | 
|  IDM-SD-07 | Test a valid Square a and Square b where they have the same rank. | q1b2, q2b2, q3b2, q4b2 | 7 | Pass | 
|  IDM-SD-08 | Test a valid Square a and Square b where they have the same file. | q1b2, q2b2, q3b3, q4b2 | 7 | Pass | 
|  IDM-SD-09 | Test a valid Square a and Square b where dx > dy. | q1b2, q2b2, q3b4, q4b1 | 7 | Pass | 
|  IDM-SD-10 | Test a valid Square a and Square b where dx < dy. | q1b2, q2b2, q3b4, q4b3 | 7 | Pass |  


#### **5.2.1.2 Find Legal Move  IDM Test Cases**

**Function:** `def find_move(self, from_square: Square, to_square: Square, promotion: Optional[PieceType] = None) -> Move`

This function is responsible for locating legal chess moves based on the starting square, the ending square, and optional promotion piece. It’s able to handle special cases like automatic pawn promotion, castling normalization, Chess960 move conversion, and move validation before returning a Move object.

**List of Input Variables**

| Input Variable   |  Type  |       Definition       |
| ---------------- | ------ | ---------------------- |
|  from_square  | Square | The starting square where the current piece is on the chess board. |
|  to_square  | Square | The ending square where the current piece wants to move on the chess board. |
|  promotion | Optional[PieceType] = None | If no promotion piece type is inputted, then piece type defaults to pawn.  |

**Characteristics of Input Variables:**

| Variable   |  Characteristics    |
| ---------  | ------- |
|  from_square  | Is the starting square valid? Is the input an integer?  |
|  to_square  | Is the ending square valid? Is the input an integer? Is the move a legal move? Is there another piece in that square? |
|  promotion  | Is the promotion specified? |

**Partition the Characteristics into Blocks and Define Values:**
| Characteristic   |  b1   | b2 | b3 | b4 |
| ---------  | ------- |---------  | ------- |---------  |
|  q1 = “range of from_square” | < 0 (invalid) | 0-63 (valid) | > 63 (invalid) | - |
|  q2 = “range of to_square”  | < 0 (invalid) | 0-63 (valid) | > 63 (invalid) | - |
|  q3 = “move context | normal move | castling move | promotion with default promotion | promotion with specified promotion |
|  q4 = “move legality” | legal move | illegal move | - | - |
|  q5 = “board context” | standard chess | chess960 | - | - |

**Coverage Criteria:**

Pair-Wise Coverage (PWC) was selected since it is able to cover all pairs of blocks for the characteristics. Even with this coverage, there are some infeasible tests cases, for instance, castling requires valid squares, which means that IDM-FM-10 is infeasible.

**Test Set Definition:**
| Test ID | Description |  q1   | q2 | q3 | q4 | q5 |
| --------| ------- |---------  | ------- | --------- | ---------  | ---------  |
|  IDM-FM-01 | Test a valid legal move in standard chess. | 0-63 (valid) | 0-63 (valid) | normal move | promotion with specified promotion | standard chess |
|  IDM-FM-02  | Test normal, illegal move in chess960. | 0-63 (valid) | 0-63 (valid) | normal move | illegal move | chess960 |
|  IDM-FM-03 | Test a valid legal castling move in standard chess. | 0-63 (valid) | 0-63 (valid) | castling move | promotion with specified promotion | standard chess |
|  IDM-FM-04 | Test an illegal castling move in chess960. | 0-63 (valid) | 0-63 (valid) | castling move | illegal move | chess960 |
|  IDM-FM-05 | Test a valid legal move where pawn moves to back rank and is promoted in standard chess. | 0-63 (valid) | 0-63 (valid) | promotion with default promotion | legal move | chess960 |
|  IDM-FM-06 | Test a valid illegal move where pawn moves to back rank in chess960. | 0-63 (valid) | 0-63 (valid) | promotion with default promotion | illegal move | chess960 |
|  IDM-FM-07 | Test a valid legal move where promotion is specified to Rook in chess960. | 0-63 (valid) | 0-63 (valid) | promotion with specified promotion | legal move | chess960 |
|  IDM-FM-08 | Test an illegal move where promotion is specified to Rook in standard chess. | 0-63 (valid) | 0-63 (valid) | promotion with specified promotion | illegal move | standard chess |
|  IDM-FM-09 | Test an invalid previous square input that is below 0 in standard chess. | < 0 (invalid) | 0-63 (valid) | normal move | illegal move | standard chess |
|  IDM-FM-10 | Test an invalid previous square input that is greater than 63 in chess960. | > 63 (invalid) | 0-63 (valid) | castling move | illegal move | chess960 |
|  IDM-FM-11 | Test an invalid to_square input that is below 0 in standard chess. | 0-63 (valid) | < 0 (invalid) | promotion with default promotion | illegal move | standard chess |
|  IDM-FM-12 | Test an invalid to_square input that is greater than 63 in chess960. | 0-63 (valid) | > 63 (invalid) | promotion with specified promotion | illegal move | chess960 |

**Test Results:**
| Test ID | Description |  Input Blocks   | Expected Output | Test Result | 
| --------| ------- |---------  | ------- | --------- | 
|  IDM-FM-01 | Test a valid legal move in standard chess. | q1b2, q2b2, q3b1, q4b1, q5b1 | "e2e3” | Pass |
|  IDM-FM-02  | Test normal, illegal move in chess960. | q1b2, q2b2, q3b1, q4b2, q5b2 | IllegalMoveError | Pass | 
|  IDM-FM-03 | Test a valid legal castling move in standard chess. | q1b2, q2b2, q3b2, q4b1, q5b1 | “e1g1” | Pass | 
|  IDM-FM-04 | Test an illegal castling move in chess960. | q1b2, q2b2, q3b2, q4b2, q5b2 | IllegalMoveError | Pass | 
|  IDM-FM-05 | Test a valid legal move where pawn moves to back rank and is promoted in standard chess. | q1b2, q2b2, q3b3, q4b1, q5b1 | “e7e8q” | Pass | 
|  IDM-FM-06 | Test a valid illegal move where pawn moves to back rank in chess960. | q1b2, q2b2, q3b3, q4b2, q5b2 | IllegalMoveError | Needs follow up | 
|  IDM-FM-07 | Test a valid legal move where promotion is specified to Rook in chess960. | q1b2, q2b2, q3b4, q4b1, q5b2 | “e7e8r” | Pass | 
|  IDM-FM-08 | Test an illegal move where promotion is specified to Rook in standard chess. | q1b2, q2b2, q3b4, q4b2, q5b1 | IllegalMoveError | Pass | 
|  IDM-FM-09 | Test an invalid previous square input that is below 0 in standard chess. | q1b1, q2b2, q3b1, q4b2, q5b1 | IllegalMoveError | Pass | 
|  IDM-FM-10 | Test an invalid previous square input that is greater than 63 in chess960. | q1b3, q2b2, q3b2, q4b2, q5b2 | IndexError | Pass |  
|  IDM-FM-11 | Test an invalid to_square input that is below 0 in standard chess. | q1b2, q2b1, q3b3, q4b2, q5b1 | IllegalMoveError | Pass |  
|  IDM-FM-12 | Test an invalid to_square input that is greater than 63 in chess960. | q1b2, q2b3, q3b4, q4b2, q5b2 | IndexError | Pass | 

#### **5.2.1.3	Get Pieces on Board IDM Test Cases**

**Function:** `def pieces(self, piece_type: PieceType, color: Color) -> SquareSet`

This function is responsible for retrieving the squares that are occupied by the specified piece type and color on the current chessboard. It’s able to generate and return a SquareSet containing the locations of the matching pieces based on the provided inputs. 

**List of Input Variables**

| Input Variable   |  Type  |       Definition       |
| ---------------- | ------ | ---------------------- |
|  piece_type  | PieceType | An integer to get the specified piece types: pawn, knight, bishop, rook, queen, and king. |
|  color  | Color | A bool to see if the color is either White or Black. |

**Characteristics of Input Variables:**

| Variable   |  Characteristics    |
| ---------  | ------- |
|  piece_type  | Is the piece type a valid type? Is there multiple pieces on the board? |
|  color  | Is the piece color a valid color? |

**Partition the Characteristics into Blocks and Define Values:**
| Characteristic   |  b1   | b2 | b3 | b4 | b5 | b6 | b7 |
| ---------  | ------- |---------  | ------- |---------  |---------  |---------  |---------  |
|  q1 = ”piece type” | pawn | knight | bishop | rook | queen | king | invalid piecetype |
|  q2 = ”color”  | white |	black |	invalid color |	- | - | - | - |
|  q3 = ”matching pieces on board” | 0 | 1 | > 1 | - | - | - | - |

**Coverage Criteria:**

Pair-Wise Coverage (PWC) was selected since it’s able to cover every piece type, color, and matching pieces without the need for having redundant test cases. 

**Test Set Definition:**
| Test ID | Description |  q1   | q2 | q3 |
| --------| ------- |---------  | ------- | --------- |
|  IDM-PC-01 | Test that white pawns are present in multiple squares. | pawn | white | > 1 |
|  IDM-PC-02  | Test that black knight is present on exactly one square. | knight | black | 1 |
|  IDM-PC-03 | Test that white bishops are absent from the board. | bishop | white | 0 |
|  IDM-PC-04 | Test that black rooks are present in multiple squares. | rook | black | > 1 | 
|  IDM-PC-05 | Test that white queen is present on exactly one square. | queen| white | 1 | 
|  IDM-PC-06 | Test that black king is present on exactly one square. | king | black | 1 |
|  IDM-PC-07 | Test that black pawns are absent from the board. | pawn | black | 0 |
|  IDM-PC-08 | Test that white knights are present in multiple squares. | knight | white | > 1 |
|  IDM-PC-09 | Test that black bishop is present on exactly one square. | bishop | black | 1 |
|  IDM-PC-10 | Test that white rooks are absent from the board. | rook | white | 0 | 
|  IDM-PC-11 | Test that black queen is present on multiple squares. | queen | black | > 1 | 
|  IDM-PC-12 | Test that white king is absent on the board. | king | white | 0 | 
|  IDM-PC-13 | Test an invalid input for piece type with valid color. | invalid piece type | white | - | 
|  IDM-PC-14 | Test a valid piece type with an invalid color. | pawn | invalid color | - | 
|  IDM-PC-15 | Test both an invalid piece type and invalid color. | invalid piece type | invalid color | - | 

**Test Results:**
| Test ID | Description |  Input Blocks   | Expected Output | Test Result | 
| --------| ------- |---------  | ------- | --------- | 
|  IDM-PC-01 | Test that white pawns are present in multiple squares. | q1b1, q2b1, q3b3 | chess.SquareSet(chess.BB_RANK2) | Pass |
|  IDM-PC-02  | Test that black knight is present on exactly one square. | q1b2, q2b2, q3b2 | chess.SquareSet(chess.BB_F6)  | Pass |
|  IDM-PC-03 | Test that white bishops are absent from the board. | q1b3, q2b1, q3b1 | chess.SquareSet(chess.BB_EMPTY)	Pass |
|  IDM-PC-04 | Test that black rooks are present in multiple squares. | q1b4, q2b2, q3b3 | chess.SquareSet([chess.A8, chess.H8]) | Pass | 
|  IDM-PC-05 | Test that white queen is present on exactly one square. | q1b5, q2b1, q3b2 | chess.SquareSet(chess.BB_D1) | Pass | 
|  IDM-PC-06 | Test that black king is present on exactly one square. | q1b6, q2b2, q3b2 | chess.SquareSet(chess.BB_E8) | Pass |
|  IDM-PC-07 | Test that black pawns are absent from the board. | q1b1, q2b2, q3b1 | chess.SquareSet(chess.BB_EMPTY) | Pass |
|  IDM-PC-08 | Test that white knights are present in multiple squares. | q1b2, q2b1, q3b3 | chess.SquareSet([chess.B1, chess.G1]) | Pass |
|  IDM-PC-09 | Test that black bishop is present on exactly one square. | q1b3, q2b2, q3b2 | chess.SquareSet(chess.BB_C8) | Pass |
|  IDM-PC-10 | Test that white rooks are absent from the board. | q1b4, q2b1, q3b1 | chess.SquareSet(chess.EMPTY) | Pass | 
|  IDM-PC-11 | Test that black queen is present on multiple squares. | q1b5, q2b2, q3b3 | chess.SquareSet([chess.B8, chess.D8]) | Pass | 
|  IDM-PC-12 | Test that white king is absent on the board. | q1b6, q2b1, q3b1 | chess.SquareSet(chess.BB_EMPTY) | Pass| 
|  IDM-PC-13 | Test an invalid input for piece type with valid color. | q1b7, q2b1 | AssertionError | Pass | 
|  IDM-PC-14 | Test a valid piece type with an invalid color. | q1b1, q2b3 | NameError | Pass| 
|  IDM-PC-15 | Test both an invalid piece type and invalid color. | q1b7, q2b3 | AssertionError | Pass | 