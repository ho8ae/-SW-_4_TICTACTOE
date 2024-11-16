def validate_position(position, board):
    """Validate if the chosen position is valid and not already taken."""
    if not (0 <= position < len(board)):
        raise ValueError("Position out of range. Choose a valid position.")
    if board[position] != " ":
        raise ValueError("Position already taken. Choose another.")
    return True
