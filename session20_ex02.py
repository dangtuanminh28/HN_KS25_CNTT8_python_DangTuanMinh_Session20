'''
Phân tích lỗi
1. Vì IndexError là lỗi phần tử không tồn tại trong danh sách
 Vì Levi có dữ liệu ("Levi", 120, 2500) gồm 3 phần tử (0,1,2) nên r = p[2] = 2500 (hợp lệ) 
 Nên đến SofM chỉ có ("SofM", 150) gồm 2 phần tử  nên  r = p[2] = IndexError (ko tồn tại)
2. Dòng bị sập: b = (m * 10) + (int(r) * 0.5)
    Lỗi: ValueError: invalid literal for int() with base 10: 'N/A'
    Vì điểm MMR của Optimus đang "N/A" nên khi ép int("N/A") sẽ đọc là số dù biến là chuỗi nên báo lỗi
3. Lệnh print("Đang xử lý:", p) giúp khi chương trình bị sập, dòng cuối cùng sẽ in ra tuyển thủ nào gây lỗi
4. Theo đánh giá tên biến quá ngắn và tối nghĩa. Người khác đọc vào sẽ không biết ds là danh sách gì
 Đổi tên:
 ds -> player_list (danh sách tuyển thủ)
 p -> record (Hồ sơ của một tuyển thủ)
 n -> name (Tên tuyển thủ)
 m -> matches (Số trận đấu)
 r -> mmr (Điểm MMR)
 b -> bonus (Tiền thưởng RP)
'''

# Sửa lỗi
player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]

def calculate_bonus(matches, mmr):
    num_mmr = int(mmr)
    bonus_rp = (matches * 10) + (num_mmr * 0.5)
    return bonus_rp

def process_player_bonuses(records_list):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    
    for record in records_list:
        try:
            name = record[0]
            matches = record[1]
            mmr = record[2]  
            
            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus} RP")
            
        except IndexError:
            print(f"Tuyển thủ {record[0]} Lỗi - Hồ sơ bị thiếu thông tin!")
            continue
            
        except ValueError:
            print(f"Tuyển thủ {name} Lỗi - Dữ liệu MMR không hợp lệ!")
            continue

process_player_bonuses(player_records)