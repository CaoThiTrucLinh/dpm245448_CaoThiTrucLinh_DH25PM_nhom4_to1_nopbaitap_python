#Cau1
from __future__ import print_function
import numpy as np
from sklearn import datasets, linear_model

# Dữ liệu mẫu (từ bảng trên trang 82/84)
# Chiều cao (cm) - X
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# Cân nặng (kg) - Y
y = np.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

# --- 1. Xây dựng ma trận mở rộng Xbar (Thêm cột 1 cho hệ số chặn w_0) ---
# Thêm cột "1" vào ma trận X để tính hệ số chặn (intercept) w_0.
# Xbar = [1, X]
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate (one, X, axis=1)

# --- 2. Tính toán các hệ số (weights) của mô hình hồi quy tuyến tính (Giải tích) ---
# Công thức giải tích cho hồi quy tuyến tính: w = (X^T * X)^-1 * X^T * y
# w = [w_0, w_1] (w_0 là intercept, w_1 là slope)
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
# np.linalg.pinv(A) là ma trận giả nghịch đảo của A, tương đương với A^-1
w = np.dot(np.linalg.pinv(A), b)

# w[0] là w_0 (hệ số chặn/intercept), w[1] là w_1 (hệ số góc/slope)

# --- 3. Fit mô hình bằng thư viện scikit-learn ---
regr = linear_model.LinearRegression()
# Scikit-learn tự động xử lý việc thêm hệ số chặn
regr.fit(X, y)

# --- 4. So sánh hai kết quả và In ra thông số mô hình ---
print("--- Kết quả so sánh hệ số mô hình ---")
print("scikit-learn's solution: w_1={0}, w_0={1}".format(regr.coef_[0], regr.intercept_))
print("our solution: w_1={0}, w_0={1}".format(w[1], w[0]))
print("------------------------------------------")

# --- 5. Dự đoán cân nặng dựa trên chiều cao người dùng nhập vào ---
try:
    # Lấy đầu vào từ người dùng
    yourHeight = float(input("Input your height (cm): "))
    
    # Sử dụng kết quả của scikit-learn để dự đoán
    # Công thức: weight = w_0 + w_1 * height
    # regr.intercept_ là w_0, regr.coef_[0] là w_1
    yourWeight = regr.intercept_ + regr.coef_[0] * yourHeight
    
    print("Your height is {0:.2f} cm, I predict your weight is {1:.2f} kg".format(yourHeight, yourWeight))
    
    # Ví dụ dự đoán cho chiều cao 170 cm như trong hình ảnh minh họa
    if yourHeight == 170:
        print("*(Lưu ý: Với chiều cao 170 cm, kết quả dự đoán là {0:.10f} kg)*".format(yourWeight))

except ValueError:
    print("Lỗi: Đầu vào không hợp lệ. Vui lòng nhập một số.")