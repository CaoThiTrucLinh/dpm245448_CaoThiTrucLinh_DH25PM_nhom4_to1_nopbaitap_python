#Cau8
import os

# Đường dẫn mẫu: d:\music\muabui.mp3

def get_full_filename(filepath):
    """
    Lấy ra tên file đầy đủ (bao gồm phần mở rộng).
    Sử dụng os.path.basename.
    """
    # os.path.basename() trả về phần cuối cùng của đường dẫn.
    return os.path.basename(filepath)

def get_song_title(filepath):
    """
    Lấy ra tên bài hát (không có phần mở rộng).
    Sử dụng os.path.splitext để tách tên và phần mở rộng.
    """
    full_filename = get_full_filename(filepath)
    # os.path.splitext() tách chuỗi tại dấu chấm cuối cùng (.), trả về (tên, .mở_rộng)
    title, extension = os.path.splitext(full_filename)
    return title

# Thử nghiệm hàm:
test_path_win = r"d:\music\muabui.mp3"
test_path_unix = "/user/songs/yume/baylen.mp4"

print("\n--- Câu 8: Tách lấy tên bài hát ---")

# Kết quả cho test_path_win
print(f"Đường dẫn: {test_path_win}")
filename_win = get_full_filename(test_path_win)
title_win = get_song_title(test_path_win)
print(f"1. Tên file đầy đủ: {filename_win}") # muabui.mp3
print(f"2. Tên bài hát: {title_win}")       # muabui

# Kết quả cho test_path_unix
print(f"\nĐường dẫn: {test_path_unix}")
filename_unix = get_full_filename(test_path_unix)
title_unix = get_song_title(test_path_unix)
print(f"1. Tên file đầy đủ: {filename_unix}") # baylen.mp4
print(f"2. Tên bài hát: {title_unix}")       # baylen