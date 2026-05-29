
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
            new_id = input("moi ban nhập mã sản phẩm: ").strip().upper()
            new_name = input("moi ban nhập tên sản phẩm: ").strip()
            while True:
                new_price  = int(input("moi ban nhập giá sản phẩm: "))

                if new_price < 0:
                    print('ko dc nhỏ hơn 0 yeu cau nhap lại !')
                else:
                    break
            while True:
                new_quantity = int(input("moi ban nhập số lượng sản phẩm: "))

                if new_quantity < 0:
                    print('ko dc nhỏ hơn 0 yeu cau nhap lại !')
                else: 
                    break
            

            product_list.append({"product_id": new_id, "product_name": new_name, "price": new_price, "quantity": new_quantity})
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
        id_new = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
        
        for i, p in enumerate(product_list):
            if p['product_id'] == id_new:
                del product_list[i]
                print("Xóa sản phẩm thành công!")
                break
            else:
                print("Không tìm thấy mã sản phẩm cần xoá!")

    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

