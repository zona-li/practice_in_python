from collections import defaultdict


class TicTacToe:

    def __init__(self, n: int):
        self.mem1h = defaultdict(list)
        self.mem1v = defaultdict(list)
        self.mem2h = defaultdict(list)
        self.mem2v = defaultdict(list)
        self.diagnal = {
            'a+b': [],
            'a=b': []
        }
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        maxCount = 0
        if player == 1:
            self.mem1h[row].append(col)
            self.mem1v[col].append(row)
            maxCount = max(maxCount, len(
                self.mem1h[row]), len(self.mem1v[col]))
        else:
            self.mem2h[row].append(col)
            self.mem2v[col].append(row)
            maxCount = max(maxCount, len(
                self.mem2h[row]), len(self.mem2v[col]))
        isDiagnal = []
        if row == col:
            isDiagnal.append('a=b')
        if row + col == self.size - 1:
            isDiagnal.append('a+b')
        for type in isDiagnal:
            if type in self.diagnal:
                if len(self.diagnal[type]) == 0:
                    self.diagnal[type].append(player)
                elif self.diagnal[type][-1] == player:
                    self.diagnal[type].append(player)
                    maxCount = max(maxCount, len(self.diagnal[type]))
                else:
                    del self.diagnal[type]
        if maxCount == self.size:
            return player
        else:
            return 0


class TicTacToe2(object):

    def __init__(self, n):
        self.row, self.col, self.diag, self.anti_diag, self.n = [
            0] * n, [0] * n, 0, 0, n

    def move(self, row, col, player):
        offset = player * 2 - 3
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.anti_diag += offset
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1
        return 0
