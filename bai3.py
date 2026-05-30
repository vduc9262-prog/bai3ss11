
product_list = [
        {
            "product_id": "SP001",
            "product_name": "Áo polo nam",
            "price": 299000,
            "quantity": 20
        },
        {
            "product_id": "SP002",
            "product_name": "Quần kaki nam",
            "price": 399000,
            "quantity": 15
        },
        {
            "product_id": "SP003",
            "product_name": "Váy công sở nữ",
            "price": 459000,
            "quantity": 10
        }
    ]

while True:

    choice = input("""
===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình
                       
Nhập vào đây: """)


    if choice == "1": 
        for i,p in enumerate(product_list,1):
            print(f"{i}.Mã SP: {p["product_id"]} | Tên: {p["product_name"]} | Giá: {p["price"]} | Số lượng: {p["quantity"]}")
        if product_list == []:
            print("Danh sách sản phẩm hiện đang trống !")
    
    elif choice == "2":
        new_id = input("Mời bạn nhập mã sản phẩm: ").strip().upper()

        is_duplicate = False

        for p in product_list:
            if p["product_id"] == new_id:
                is_duplicate = True
                break

        if is_duplicate:
            print("Mã sản phẩm bị trùng")
            continue

        new_name = input("Mời bạn nhập tên sản phẩm: ").strip()

        while True:
            try:
                new_price = int(input("Mời bạn nhập giá sản phẩm: "))

                if new_price <= 0:
                    print("Giá/Số lượng không hợp lệ")
                else:
                    break

            except ValueError:
                print("Giá/Số lượng không hợp lệ")

        while True:
            try:
                new_quantity = int(input("Mời bạn nhập số lượng sản phẩm: "))

                if new_quantity <= 0:
                    print("Giá/Số lượng không hợp lệ")
                else:
                    break

            except ValueError:
                print("Giá/Số lượng không hợp lệ")

        product_list.append({
            "product_id": new_id,
            "product_name": new_name,
            "price": new_price,
            "quantity": new_quantity
        })

        print("Thêm sản phẩm thành công")
    elif choice == "3":
        update_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()

    
        for p in product_list:
            if p["product_id"] == update_id:
                print(f"Đang cập nhật sản phẩm: {p['product_name']}")

                new_name = input("Nhập tên sản phẩm mới : ").strip()
                if new_name != "":
                    p["product_name"] = new_name

                while True:
                    new_price = input("Nhập giá sản phẩm mới : ").strip()
                    if new_price == "":
                        break
 
                    new_price = int(new_price)
                    if new_price < 0:
                        print("Giá không được nhỏ hơn 0, vui lòng nhập lại!")
                    else:
                        p["price"] = new_price
                        break

                while True:
                    new_quantity = input("Nhập số lượng sản phẩm mới : ").strip()
                    if new_quantity == "":
                        break
                    new_quantity = int(new_quantity)
                    if new_quantity < 0:
                        print("Số lượng không được nhỏ hơn 0, vui lòng nhập lại!")
                    else:
                        p["quantity"] = new_quantity
                        break


                print("Cập nhật sản phẩm thành công!")
                break
        else:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")


    elif choice == "4":
            print("\n--- XÓA SẢN PHẨM ---")
            delete_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()

            found = False
            for i, prod in enumerate(product_list):
                if prod["product_id"] == delete_id:
                    product_list.pop(i)
                    print(f"Đã xóa sản phẩm: {delete_id}")
                    found = True
                    break

            if not found:
                print("Không tìm thấy mã sản phẩm cần xoá!")

    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

# Phân tích Input/Output
# Input
# Tên biến	Ý nghĩa	Kiểu dữ liệu
# full_name	Họ tên người dùng	str
# age	Tuổi	int
# Output
# Nội dung
# Thông tin đã nhập
# Kết quả xử lý theo yêu cầu
# Đề xuất giải pháp
# Hàm/phương thức sử dụng
# input() để nhận dữ liệu từ người dùng.
# int() để chuyển đổi dữ liệu sang số nguyên.
# if-elif-else để xử lý điều kiện.
# print() để hiển thị kết quả.
# Kiểm tra dữ liệu hợp lệ
# Tuổi phải là số nguyên dương.
# Họ tên không được để trống.
# Các bước thực hiện
# Nhập dữ liệu.
# Kiểm tra tính hợp lệ.
# Xử lý nghiệp vụ.
# Hiển thị kết quả.
# 3. Thiết kế thuật toán (Pseudocode)
# Bắt đầu

# Nhập full_name
# Nhập age

# Nếu age <= 0
#     Thông báo dữ liệu không hợp lệ
# Ngược lại
#     Xử lý theo yêu cầu

# Hiển thị kết quả

# Kết thúc
