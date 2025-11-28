#Cau15
def explain_range_commands():
    ranges = {
        "(a)": range(5),
        "(b)": range(5, 10),
        "(c)": range(5, 20, 3),
        "(d)": range(20, 5, -1),
        "(e)": range(20, 5, -3),
        "(f)": range(10, 5),
        "(g)": range(0),
        "(h)": range(10, 101, 10),
        "(i)": range(10, -1, -1),
        "(j)": range(-3, 4),
        "(k)": range(0, 10, 1)
    }

    print("\n--- Câu 15: Giải thích cách chạy các dòng lệnh range ---")
    
    # Định dạng header cho kết quả
    print(f"{'Câu':<5} | {'Lệnh':<20} | Dãy số sinh ra")
    print("-" * 50)
    
    for key, r_obj in ranges.items():
        # Lấy thông tin về start, stop, step (range_obj.start, range_obj.stop, range_obj.step)
        info = f"range({r_obj.start}, {r_obj.stop}, {r_obj.step})"
        
        # Chuyển đổi range object thành list để hiển thị
        sequence = list(r_obj)
        
        print(f"{key:<5} | {info:<20} | {sequence}")

explain_range_commands()