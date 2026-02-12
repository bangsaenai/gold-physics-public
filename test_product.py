import engine_core
import numpy as np

# ลองเช็คดูซิว่าเป็นของจริงไหม
print("--- TESTING BLACKBOX ENGINE ---")
print(f"File Location: {engine_core.__file__}")

# สร้างข้อมูลจำลอง (ราคาทองปลอมๆ)
dummy_prices = [1900.0, 1905.5, 1910.2, 1920.0, 1915.0]

# เรียกใช้ฟังก์ชันลับ!
score = engine_core.get_gold_instability(dummy_prices)

print(f"\nCalculated Instability Score: {score}")

if score > 0:
    print("✅ SUCCESS: Engine is working!")
else:
    print("❌ ERROR: Something is wrong.")