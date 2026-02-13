# engine_core.py
# นี่คือ "สูตรลับ" ที่เราต้องการซ่อน
def calculate_secret_score(price):
    if price < 0:
        return 0
    # สมมติสูตรคำนวณซับซ้อน
    magic_number = 0.85
    volatility = price * 0.05
    return (price * magic_number) + volatility

def get_version():
    return "v1.0 (Blackbox Edition)"
