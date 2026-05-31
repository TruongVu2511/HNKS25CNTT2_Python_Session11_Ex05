product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]

while True :
    print("""===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====
1. Hiển thị danh sách sản phẩm
2. Bán sản phẩm cho khách hàng
3. Xử lý đổi trả sản phẩm
4. Áp dụng giảm giá cho sản phẩm
5. Nhập thêm hàng vào kho cửa hàng
6. Thoát chương trình""")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ")
    if not choice.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
            continue
    choose = int(choice)
    match choose:
        case 1: 
            if product_list == [] :
                print("Danh sách sản phẩm hiện đang trống.") 
            else :          
                print("Danh sách sản phẩm hiện tại : ")
                for list_product in product_list :
                    if list_product["quantity"] == 0 :
                        status = "Hết hàng"
                    elif list_product["quantity"] <= 5 :
                        status = "Sắp hết hàng"
                    else :
                        status = "Còn hàng"
                    print(f"Mã sản phẩm : {list_product["product_id"]} | Tên : {list_product["product_name"]} | Giá : {list_product["price"]} | Tồn kho : {list_product["quantity"]} | Đã bán : {list_product["sold"]} |  Đổi trả : {list_product["returned"]} | Giảm giá : {list_product["discount"]} | Trạng thái : {status} ")    
        case 2:
            product_buy = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
            try:
                quantity_buy = int(input("Nhập số lượng khách mua: "))
                if quantity_buy <= 0:
                    print("Số lượng mua phải là số nguyên dương, vui lòng nhập lại")
                    continue
            except ValueError:
                print("Số lượng mua phải là số nguyên dương, vui lòng nhập lại")
                continue
            found = False
            for product in product_list:
                if product["product_id"] == product_buy:
                    found = True
                    if quantity_buy > product["quantity"]:
                        print("Số lượng mua vượt quá số lượng tồn kho, vui lòng nhập lại")
                        break
                    total_money = product["price"] * (1 - product["discount"] / 100) * quantity_buy
                    product["quantity"] -= quantity_buy
                    product["sold"] += quantity_buy

                    print(f"Tổng tiền khách cần thanh toán: {total_money:,.0f}")

                    break

            if found == False:
                print("Mã sản phẩm không tồn tại, vui lòng nhập lại")