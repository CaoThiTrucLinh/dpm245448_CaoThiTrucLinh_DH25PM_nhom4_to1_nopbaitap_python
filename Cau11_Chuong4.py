#Cau11
# Khai báo các hàm theo đề bài
val = 0 # Biến toàn cục (global)

def sum1(x):
    global val
    n = x
    while n > 0:
        val -= 1
        n -= 1

def sum2():
    global val
    val_temp = val
    i = 0
    while val > 0:
        val -= 1
        i += 1
    
def sum3(x):
    global val
    for n in range(x, 0, -1):
        val += 1

# --- TRƯỜNG HỢP 1 ---
print("\n--- Câu 11: Trường hợp 1 ---")
val = 10
print(val) # 10
print(sum1(1)) # None
print(val) # 9
print(sum3(2)) # None
print(val) # 11
sum2()
print(val) # 0
sum3(10)
print(val) # 10

# --- TRƯỜNG HỢP 2 ---
print("\n--- Câu 11: Trường hợp 2 ---")
val = 5
print(val) # 5
print(sum1(1)) # None
print(val) # 4
print(sum3(2)) # None
print(val) # 6
sum2()
print(val) # 0
sum3(5)
print(val) # 5

# --- TRƯỜNG HỢP 3 ---
print("\n--- Câu 11: Trường hợp 3 ---")
val = 20
print(val) # 20
sum2()
print(val) # 0
print(sum3(1)) # None
print(val) # 1
print(sum1(1)) # None
print(val) # 0
sum3(3)
print(val) # 3