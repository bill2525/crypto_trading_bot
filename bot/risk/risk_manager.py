class RiskManager:
    def __init__(self, max_position: float, max_daily_loss: float):
        self.max_position = max_position
        self.max_daily_loss = max_daily_loss
        self.daily_loss = 0.0

    def check(self, balance: float, unrealized_pnl: float) -> bool:
        if balance > self.max_position:
            return False
        if self.daily_loss + unrealized_pnl < -self.max_daily_loss:
            return False
        return True
