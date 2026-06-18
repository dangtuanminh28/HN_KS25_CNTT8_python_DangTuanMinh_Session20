import logging

logging.basicConfig(
    filename="tournament_app.log",
    filemode="a",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)


matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    },
    {
        "match_id": "M03",
        "team_a": "G2",
        "team_b": "FNC",
        "score_a": 0,
        "score_b": 1,
        "status": "Completed"
    }
]

def determine_winner(match):
    if match.get("status") != "Completed":
        return "Pending"
    if match["score_a"] > match["score_b"]:
        return match["team_a"]
    elif match["score_a"] < match["score_b"]:
        return match["team_b"]
    else:
        return "Hòa"

def display_matches(match_list) :
    if not match_list :
        print("Hiện chưa có trận đấu nào trong hệ thống")
        return
    else :
        print("--- LỊCH THI ĐẤU & KẾT QUẢ ---")
        print("Mã trận   | Đội A           | Đội B           | Tỷ số   | Trạng thái")
        print("----------------------------------------------------------------------")
        for count in match_list :
            print(f"{count['match_id']:<9} | {count['team_a']:<15} | {count['team_b']:<15} | {count['score_a']}-{count['score_b']:<5} | {count['status']}")
        logging.info("User viewed the match list.")

def add_matches(match_list) :
    print("--- THÊM TRẬN ĐẤU MỚI ---")
    add_matches_id = input("Nhập mã trận đấu: ").strip().upper()
    if add_matches_id == '' :
        print("Mã trận đấu không được để trống.")
        logging.warning(" User tried to add a match with empty match ID.")
        return
    
    for count in match_list :
        if add_matches_id == count['match_id'] :
            print(f"Lỗi: Mã trận đấu {add_matches_id} đã tồn tại.")
            logging.warning(f"Match ID {add_matches_id} already exists.")
            return
        
    add_teams_A = input("Nhập tên đội A: ").strip()
    add_teams_B = input("Nhập tên đội B: ").strip()
    if add_teams_A == '' or add_teams_B == '' :
        print("Tên đội không được để trống.")
        logging.warning(" User tried to add a match with empty team name.")
        return
    else :
        new_matches = {
            "match_id": add_matches_id,
            "team_a": add_teams_A,
            "team_b": add_teams_B,
            "score_a": 0,
            "score_b": 0,
            "status": "Pending"
        }
        match_list.append(new_matches)
        print(f"Thành công: Đã thêm trận đấu {add_matches_id}")
        logging.info(f"Match {add_matches_id} added successfully")
            
def update_score(match_list) :
    print("--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")
    update_matches_id = input("Nhập mã trận đấu cần cập nhật: ").strip().upper()
    if update_matches_id == '' :
        print("Mã trận đấu không được để trống.")
        logging.warning(" User tried to add a match with empty match ID.")
        return
    for count in match_list :
        if update_matches_id == count['match_id'] :
            print(f"Trận đấu {count['team_a']} vs {count['team_b']} ({count['status']})")
            try :
                update_teams_A = int(input("Nhập điểm Đội A: "))
                update_teams_B = int(input("Nhập điểm Đội B: "))
                if update_teams_A < 0:
                    print("Điểm số đội A phải lớn hơn hoặc bằng 0.")
                    logging.error(f"Negative score input detected: {update_teams_A}")
                    return
                if update_teams_B < 0:
                    print("Điểm số đội B phải lớn hơn hoặc bằng 0.")
                    logging.error(f"Negative score input detected: {update_teams_B}")
                    return
                if update_teams_A == 0 and update_teams_B == 0 :
                    while True :
                        update_confirm = input("Tỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n): ").strip().lower()
                        if update_confirm == 'y' :
                            count['status'] = 'Completed'
                            break
                        elif update_confirm == 'n':
                            count['status'] = 'Pending'
                            break
                        else :
                            print("Vui lòng nhập(y/n)")

            except ValueError as alert :
                print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
                logging.error(f"Invalid score input. Error: {alert}")
                return
            
            count['score_a'] = update_teams_A
            count['score_b'] = update_teams_B
            print(f"Thành công: Đã cập nhật tỷ số trận đấu {update_matches_id}")
            logging.info(f"Match {update_matches_id} score updated successfully")
            return
    else :
        print(f"Không tìm thấy trận đấu mang mã {update_matches_id}")
        logging.warning(f"User tried to update non-existing match {update_matches_id}")
        return
        
def generate_report(match_list) :
    if not match_list :
        print("Chưa có trận đấu nào hoàn thành.")
        print("Tổng số trận đã hoàn thành: 0")
        return
    else :
        total_done = 0
        print("--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")
        for count in match_list :
            if count['status'] == "Completed" :
                total_done += 1
                winner = determine_winner(count)

                print(f"{count['match_id']:<2}: "
                    f"{count['team_a']:<3} {count['score_a']}-{count['score_b']:<3} {count['team_b']:<5} | "
                    f"Kết quả: {winner}")
           
        print(f"Tổng số trận đã hoàn thành: {total_done}")
        logging.info(" User generated tournament report.")

while True: 
    print("""
===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====
1. Hiển thị lịch thi đấu & Kết quả
2. Thêm trận đấu mới
3. Cập nhật tỷ số trận đấu
4. Báo cáo thống kê
5. Thoát chương trình
================================================== 
""")
    choice = input("Chọn chức năng (1-5): ")
    if choice == '1':
        display_matches(matches)
    elif choice == '2':
        add_matches(matches)
    elif choice == '3':
        update_score(matches)
    elif choice == '4':
        generate_report(matches)
    elif choice == '5':
        print("Thoát chương trình")
        break
    else :
        print("Vui lòng nhập lại(1-5)!")
        