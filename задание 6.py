class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def determine_winner(move1, move2):
    if move1 == move2:
        return 0  # Ничья, побеждает первый
    
    rules = {
        'R': {'S': True, 'P': False},  # Камень бьет ножницы
        'P': {'R': True, 'S': False},  # Бумага бьет камень
        'S': {'P': True, 'R': False}   # Ножницы бьют бумагу
    }
    
    return 1 if rules[move1][move2] else 2

def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError()
    
    valid_moves = {'R', 'P', 'S'}
    moves = []
    
    for player in players:
        name, move = player
        move = move.upper()
        
        if move not in valid_moves:
            raise NoSuchStrategyError()
        
        moves.append((name, move))
    
    p1, p2 = moves[0], moves[1]
    result = determine_winner(p1[1], p2[1])
    
    if result == 0 or result == 1:
        return f"{p1[0]} {p1[1]}"
    else:
        return f"{p2[0]} {p2[1]}"