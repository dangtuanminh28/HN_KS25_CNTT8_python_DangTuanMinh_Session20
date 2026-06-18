'''
Phân tích lỗi
1. Vì khi đến phần tử 'ShowMaker' biến d = 0, khi đến lệnh int(d) = 0 nên khi tính chia 0 báo lỗi dừng lập tức
2. Nếu xóa ShowMaker, đến lượt Chovy sẽ gặp lỗi  ValueError: invalid literal for int() with base 10: 'ba'
 Vì biến d phần tử 'Chovy' đang chuỗi 'ba' nên khi int('ba') sẽ ép sang số nguyên dù 'ba' là chuỗi nên báo lỗi
3. Theo đánh giá tên biến quá ngắn và tối nghĩa. Người khác đọc vào sẽ không biết ds là danh sách gì
 Đổi tên:
 ds -> player_list (danh sách tuyển thủ)
 x -> player (Tuyển thủ)
 n -> name (Tên tuyển thủ)
 k -> kills (Số mạng hạ gục)
 d -> deaths (Số mạng bị hẹo)
 a -> assists (Số mạng hỗ trợ)
4. Lợi ích: Tái sử dụng, dễ sửa chữa, dùng trong bất kỳ hàm nào trong dự án
'''

# Sửa lỗi
player_list = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]

def calculate_kda(kills, deaths, assists):
    num_kills = int(kills)
    num_deaths = int(deaths)
    num_assists = int(assists)
    
    kda_result = (num_kills + num_assists) / num_deaths
    return kda_result

def print_kda_leaderboard(data):
    print("--- BẢNG XẾP HẠNG KDA ---")
    
    for player in data:
        name = player[0]
        kills = player[1]
        deaths = player[2]
        assists = player[3]
        
        try:
            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda}")
            
        except ZeroDivisionError:
            print(f"[{name}]: KDA Hoàn hảo (Perfect Game)!")
            continue            
        except ValueError:
            print(f"[{name}]: Lỗi dữ liệu không hợp lệ!")
            continue

print_kda_leaderboard(player_list)