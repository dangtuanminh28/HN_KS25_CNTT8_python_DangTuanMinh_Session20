import logging

logging.basicConfig(
    filename="roster_app.log",
    filemode="a",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)

roster = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active"
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active"
    },
    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched"
    }
]

def display_roster(roster_list):
    if not roster_list :
        print("Đội hình hiện đang trống.")
        return
    else :
        print("--- ĐỘI HÌNH RIKKEI ESPORTS ---")
        print("ID       | Tên tuyển thủ        | Vị trí          | Lương        | Trạng thái")
        print("--------------------------------------------------------------------------------")
        for roster in roster_list :
            if roster['status'] == 'Benched' :
                full_name = f"{roster['name']} [DỰ BỊ]"
            else :
                full_name = roster["name"]
            print(
                f"{roster['player_id']:<8} | "
                f"{full_name:<20} | "
                f"{roster['role']:<15} | "
                f"{roster['salary']:<12} | "
                f"{roster['status']}"
            )
        logging.info("Coach viewed the team roster.")

def sign_player(roster_list):
    print("--- CHIÊU MỘ TUYỂN THỦ MỚI ---")

    while True:
        add_id = input("Nhập mã tuyển thủ: ").strip().upper()
        if add_id == "":
            print("Lỗi: Mã tuyển thủ không được để trống!")
            continue
        for ros in roster_list:
            if ros["player_id"] == add_id:
                print(f"Lỗi: Mã tuyển thủ {add_id} đã tồn tại.")
                logging.warning(f"Failed to sign player - Duplicate player ID {add_id}")
                break
        else:
            break

    while True:
        add_name = input("Nhập tên tuyển thủ: ").strip().title()
        if add_name == "":
            print("Lỗi: Tên không được để trống!")
            continue
        break

    while True:
        add_placed = input("Nhập vị trí thi đấu: ").strip()
        if add_placed == "":
            print("Lỗi: Vị trí không được để trống!")
            continue
        break

    while True:
        try:
            add_price = int(input("Nhập mức lương hàng tháng: ").strip())
            if add_price <= 0:
                print("Lương phải là số. Vui lòng nhập lại.")
                logging.warning("Failed to sign player - Invalid salary input")
                continue
            break
        except ValueError:
            print("Lương phải là số. Vui lòng nhập lại.")
            logging.warning("Failed to sign player - Invalid salary input")

    new_ros = {
        "player_id": add_id,
        "name": add_name,
        "role": add_placed,
        "salary": add_price,
        "status": "Active",
    }
    roster_list.append(new_ros)

    print(f"Thành công: Đã chiêu mộ tuyển thủ {add_name}")
    logging.info(f"Signed new player {add_name} with salary {add_price}")

def update_player_status(roster_list):
    print("--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---")
    update_id = input("Nhập mã tuyển thủ cần cập nhật: ").strip().upper()
    for roster in roster_list:
        if roster["player_id"] == update_id:
            print(f"Tuyển thủ: {roster['name']}\n"
                  f"Vị trí: {roster['role']}\n"
                  f"Lương hiện tại: {roster['salary']:,}\n"
                  f"Trạng thái hiện tại: {roster['status']}\n")
            print("Bạn muốn cập nhật:")
            print("1. Cập nhật lương")
            print("2. Cập nhật trạng thái thi đấu")

            while True:
                choice = input("Chọn chức năng cập nhật (1-2): ").strip()
                if choice == "1":
                    while True:
                        try:
                            new_salary = int(input("Nhập mức lương mới: ").strip())
                            if new_salary <= 0:
                                print("Lỗi: Lương phải là số lớn hơn 0. Vui lòng nhập lại!")
                                continue

                            old_salary = roster["salary"]
                            roster["salary"] = new_salary

                            print(f"Thành công: Đã cập nhật lương cho tuyển thủ {update_id}.")
                            logging.info(f"Updated player {update_id} salary from {old_salary} to {new_salary}")
                            return

                        except ValueError:
                            print("Lỗi: Mức lương phải là số nguyên hợp lệ. Vui lòng nhập lại!")

                elif choice == "2":
                    print("Chọn trạng thái mới:")
                    print("1. Active")
                    print("2. Benched")

                    while True:
                        status_choice = input("Nhập lựa chọn trạng thái (1-2): ").strip()

                        if status_choice == "1":
                            new_status = "Active"
                        elif status_choice == "2":
                            new_status = "Benched"
                        else:
                            print("Lựa chọn không hợp lệ. Vui lòng chỉ chọn 1 hoặc 2!")
                            continue

                        old_status = roster["status"]
                        roster["status"] = new_status

                        print(f"\nThành công: Đã cập nhật trạng thái cho tuyển thủ {update_id}.")
                        logging.info(f"Updated player {update_id} status from {old_status} to {new_status}")
                        return
                else:
                    print("Vui lòng chọn (1-2)")

    else:
        print(f"Không tìm thấy tuyển thủ mang mã {update_id}.")
        logging.warning(f"Failed to update player - Player ID {update_id} not found")

def generate_payroll_report(roster_list):
    print("--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---")
    if not roster_list:
        print("Đội hình hiện đang trống. Tổng quỹ lương: 0.0")
        logging.info("Generated monthly payroll report. Total: 0.0")
        return
    print(f"{'ID':<8} | {'Tên tuyển thủ':<15} | {'Trạng thái':<10} | {'Lương gốc':<12} | {'Lương thực nhận'}")
    print("--------------------------------------------------------------------------------")
    total_payroll = 0.0

    try:
        for roster in roster_list:
            player_id = roster["player_id"]
            name = roster["name"]
            status = roster["status"]
            base_salary = float(roster["salary"])

            if status == "Active":
                actual_salary = base_salary
            elif status == "Benched":
                actual_salary = base_salary * 0.5
            else:
                actual_salary = 0.0

            total_payroll += actual_salary

            print(f"{player_id:<8} | {name:<15} | {status:<10} | {base_salary:,}       | {actual_salary:,}")

    except KeyError as alert:
        print("Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")
        print("--------------------------------------------------------------------------------")
        print("Tổng quỹ lương hàng tháng: 0.0")
        logging.error(f"Missing key while generating payroll report: {alert}")
        return

    print("--------------------------------------------------------------------------------")
    print(f"Tổng quỹ lương hàng tháng: {total_payroll:,}")
    logging.info(f"Generated monthly payroll report. Total: {total_payroll}")

while True :
    print("""
===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS ===== 
1.Xem đội hình thi đấu hiện tại
2.Chiêu mộ tuyển thủ mới
3.Cập nhật lương & Trạng thái thi đấu
4.Báo cáo quỹ lương hàng tháng
5.Thoát hệ thống
================================================== 
""")
    choice = input("Chọn chức năng (1-5): ")
    if choice == '1':
        display_roster(roster)
    elif choice == '2':
        sign_player(roster)
    elif choice == '3':
        update_player_status(roster)
    elif choice == '4':
        generate_payroll_report(roster)
    elif choice == '5':
        print("Thoát chương trình")
        break
    else :
        print("Vui lòng nhập lại(1-5)!")