class ChessModule:
    def is_attacking(self, q1, q2):
        if q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
            return True
        else:
            return False

    def check_queens(self, queens):
        for i in range(len(queens)):
            for j in range(i+1, len(queens)):
                if self.is_attacking(queens[i], queens[j]):
                    return False
        return True
