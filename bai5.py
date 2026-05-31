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
    
    choice = input("Nhập lựa chọn của bạn (1-6): ")
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
                        print("Số lượng trong kho không đủ để bán")
                        break
                    price_after_discount = product["price"] * (100 - product["discount"]) / 100
                    total_money = price_after_discount * quantity_buy                    
                    product["quantity"] -= quantity_buy
                    product["sold"] += quantity_buy
                    print(f"Tổng tiền khách cần thanh toán: {total_money}")
                    break
            if found == False:
                print("Không tìm thấy sản phẩm cần bán")
        case 3:
            product_return = input("Nhập mã sản phẩm khách muốn đổi/trả: ").strip().upper()
            try:
                quantity_return = int(input("Nhập số lượng đổi/trả: "))
                if quantity_return <= 0:
                    print("Số lượng đổi/trả phải là số nguyên dương, vui lòng nhập lại")
                    continue
            except ValueError:
                print("Số lượng đổi/trả phải là số nguyên dương, vui lòng nhập lại")
                continue
            found = False
            for product in product_list:
                if product["product_id"] == product_return:
                    found = True
                    if quantity_return > product["sold"]:
                        print("Số lượng đổi/trả không được vượt quá số lượng đã bán")
                        break
                    refund_money = product["price"] * quantity_return
                    product["sold"] -= quantity_return
                    product["quantity"] += quantity_return
                    product["returned"] += quantity_return
                    print(f"Số tiền hoàn lại cho khách hàng: {refund_money}")
                    break
            if found == False:
                print("Không tìm thấy sản phẩm cần đổi trả")
        case 4:
            product_discount = input("Nhập mã sản phẩm cần áp dụng giảm giá: ").strip().upper()
            try:
                discount = int(input("Nhập phần trăm giảm giá: "))
                if discount < 0 or discount > 70:
                    print("Phần trăm giảm giá không hợp lệ")
                    continue
            except ValueError:
                print("Phần trăm giảm giá không hợp lệ")
                continue
            found = False
            for product in product_list:
                if product["product_id"] == product_discount:
                    found = True
                    product["discount"] = discount
                    break
            if found == False:
                print("Mã sản phẩm không tồn tại, vui lòng nhập lại")
        case 5:
            product_import = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()
            try:
                quantity_import = int(input("Nhập số lượng nhập thêm: "))
                if quantity_import <= 0:
                    print("Số lượng nhập thêm phải là số nguyên dương")
                    continue
            except ValueError:
                print("Số lượng nhập thêm phải là số nguyên dương")
                continue
            found = False
            for product in product_list:
                if product["product_id"] == product_import:
                    found = True
                    product["quantity"] += quantity_import
                    break
            if found == False:
                print("Mã sản phẩm không tồn tại, vui lòng nhập lại")
        case 6:
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
            
            
            
            
#1. Phân tích Input/Output
# Input:
# Lựa chọn chức năng từ menu (int).
# Mã sản phẩm (string).
# Số lượng mua, đổi trả, nhập thêm (int).
# Phần trăm giảm giá (int).

# Output:
# Danh sách sản phẩm và trạng thái tồn kho.
# Tổng tiền khách cần thanh toán khi mua hàng.
# Số tiền hoàn lại khi đổi/trả sản phẩm.
# Thông báo cập nhật giảm giá, nhập hàng thành công.
# Thông báo lỗi khi dữ liệu không hợp lệ.
# 2. Đề xuất giải pháp
# Sử dụng danh sách (list) chứa các từ điển (dictionary) để lưu thông tin sản phẩm.
# Sử dụng vòng lặp while True để hiển thị menu liên tục.
# Sử dụng match-case để xử lý từng chức năng.
# Dùng .strip().upper() để chuẩn hóa mã sản phẩm.
# Dùng try-except để kiểm tra dữ liệu số nguyên.
# Kiểm tra các điều kiện hợp lệ trước khi cập nhật dữ liệu:
# Mã sản phẩm phải tồn tại.
# Số lượng phải là số nguyên dương.
# Không bán vượt tồn kho.
# Không đổi trả vượt số lượng đã bán.
# Phần trăm giảm giá từ 0 đến 70.
# 3. Thiết kế thuật toán (Pseudocode)
# Bắt đầu chương trình

# Khởi tạo danh sách sản phẩm

# Lặp vô hạn:
#     Hiển thị menu
#     Nhập lựa chọn

#     Nếu lựa chọn không hợp lệ:
#         Thông báo lỗi
#         Tiếp tục

#     Nếu chọn 1:
#         Hiển thị danh sách sản phẩm
#         Xác định trạng thái tồn kho

#     Nếu chọn 2:
#         Nhập mã sản phẩm và số lượng mua
#         Kiểm tra dữ liệu hợp lệ
#         Tìm sản phẩm
#         Kiểm tra tồn kho
#         Tính tổng tiền
#         Cập nhật tồn kho và số lượng đã bán

#     Nếu chọn 3:
#         Nhập mã sản phẩm và số lượng đổi/trả
#         Kiểm tra dữ liệu hợp lệ
#         Tìm sản phẩm
#         Kiểm tra số lượng đã bán
#         Cập nhật tồn kho, số lượng đã bán và đổi trả
#         Tính tiền hoàn lại

#     Nếu chọn 4:
#         Nhập mã sản phẩm và phần trăm giảm giá
#         Kiểm tra dữ liệu hợp lệ
#         Cập nhật giảm giá

#     Nếu chọn 5:
#         Nhập mã sản phẩm và số lượng nhập thêm
#         Kiểm tra dữ liệu hợp lệ
#         Cập nhật tồn kho

#     Nếu chọn 6:
#         Thoát chương trình

# Kết thúc chương trình