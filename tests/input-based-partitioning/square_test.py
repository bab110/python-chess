import chess
import unittest
        

# Test 1: Square Distance
# def square_distance(a: Square, b: Square) -> int:
#     """
#     Gets the Chebyshev distance (i.e., the number of king steps) from square *a* to *b*.
#     """
#     return max(abs(square_file(a) - square_file(b)), abs(square_rank(a) - square_rank(b)))



# Test 2: Square Manhatten Distance
# def square_manhattan_distance(a: Square, b: Square) -> int:
#     """
#     Gets the Manhattan/Taxicab distance (i.e., the number of orthogonal king steps) from square *a* to *b*.
#     """
#     return abs(square_file(a) - square_file(b)) + abs(square_rank(a) - square_rank(b))



# Test 3: Square Knight Distance : Graph Testing
# def square_knight_distance(a: Square, b: Square) -> int:
#     """
#     Gets the Knight distance (i.e., the number of knight moves) from square *a* to *b*.
#     """
#     dx = abs(square_file(a) - square_file(b))
#     dy = abs(square_rank(a) - square_rank(b))

#     if dx + dy == 1:
#         return 3
#     elif dx == dy == 2:
#         return 4
#     elif dx == dy == 1:
#         if BB_SQUARES[a] & BB_CORNERS or BB_SQUARES[b] & BB_CORNERS:  # Special case only for corner squares
#             return 4

#     m = math.ceil(max(dx / 2, dy / 2, (dx + dy) / 3))
#     return m + ((m + dx + dy) % 2)



# Test 4: Parse Square
# def parse_square(name: str) -> Square:
#     """
#     Gets the square index for the given square *name*
#     (e.g., ``a1`` returns ``0``).

#     :raises: :exc:`ValueError` if the square name is invalid.
#     """
#     return SQUARE_NAMES.index(name)



# Test 5: Square Name
# def square_name(square: Square) -> str:
#     """Gets the name of the square, like ``a3``."""
#     return SQUARE_NAMES[square]



# Test 6: Square
# def square(file_index: File, rank_index: Rank) -> Square:
#     """Gets a square number by file and rank index."""
#     return rank_index * 8 + file_index



# Test 7: Parse File
# def parse_file(name: str) -> File:
#     """
#     Gets the file index for the given file *name*
#     (e.g., ``a`` returns ``0``).

#     :raises: :exc:`ValueError` if the file name is invalid.
#     """
#     return FILE_NAMES.index(name)



# Test 8: File Name
# def file_name(file: File) -> str:
#     """Gets the name of the file, like ``a``."""
#     return FILE_NAMES[file]



# Test 9: Parse Rank
# def parse_rank(name: str) -> File:
#     """
#     Gets the rank index for the given rank *name*
#     (e.g., ``1`` returns ``0``).

#     :raises: :exc:`ValueError` if the rank name is invalid.
#     """
#     return FILE_NAMES.index(name)



# Test 10: Rank Name
# def rank_name(rank: Rank) -> str:
#     """Gets the name of the rank, like ``1``."""
#     return FILE_NAMES[rank]



# Test 11: Square File
# def square_file(square: Square) -> File:
#     """Gets the file index of the square where ``0`` is the a-file."""
#     return square & 7



# Test 12: Square Rank
# def square_rank(square: Square) -> Rank:
#     """Gets the rank index of the square where ``0`` is the first rank."""
#     return square >> 3



