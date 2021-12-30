class Leaderboard:

    def __init__(self):
        self.lb = {}
        self.score = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.lb:
            old_player_score = self.lb[playerId]
            self.lb[playerId] = old_player_score + score
            self.score.remove(old_player_score)
            bisect.insort(self.score, old_player_score+score)
        else:
            self.lb[playerId] = score
            bisect.insort(self.score, score)
            

    def top(self, K: int) -> int:
        if K > len(self.score):
            K = len(self.score)
        sum = 0
        for n in self.score[len(self.score)-K:]:
            sum += n
        return sum
        

    def reset(self, playerId: int) -> None:
        if playerId in self.lb:
            player_score = self.lb[playerId]
            del self.lb[playerId]
            self.score.remove(player_score)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)