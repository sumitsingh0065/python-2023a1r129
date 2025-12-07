#Custom exception
class LowBalanceError(Exception):
    pass

class DigitalWallet:
    def __init__(self, credits):
        self.credits = credits
    
    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.credits:
            raise LowBalanceError("Payment exceeds available credits")
        self.credits -= amount
        return self.credits

# Example usage
wallet = DigitalWallet(3000)

try:
    wallet.pay(5000)
except Exception as e:
    print(e)  # Output: Payment exceeds available credits

try:
    wallet.pay(-20)
except Exception as e:
    print(e)  # Output: Amount must be positive
 
