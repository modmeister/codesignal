def bishopAndPawn(bishop, pawn):
    return (ord(bishop[0]) + int(bishop[1]) + ord(pawn[0]) + int(pawn[1])) % 2 == 0 and ord(bishop[0]) != ord(pawn[0]) and int(bishop[1]) != int(pawn[1])
