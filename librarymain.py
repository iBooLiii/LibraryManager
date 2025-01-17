# 題目：圖書管理系統
# 設計一個簡單的圖書管理系統，具備以下功能：
#
# 1.顯示目前的圖書清單
# 每本書包括「書名」、「作者」、「價格」和「庫存數量」。
#
# 2.新增或刪除書籍項目（需驗證）
# 使用者可以輸入書名、作者、價格和庫存數量，將書籍新增到清單中。
# 刪除書籍時，需檢查該書是否存在。
#
# 3.更新書籍資訊
# 修改書籍的價格或庫存數量。
#
# 4.借書/還書功能
# 借書時，從庫存數量中扣減並記錄借書人名稱。
# 還書時，更新庫存並移除借書紀錄。
#
# 5.統計資訊
# 計算目前總庫存的價值（所有書籍的總價值 = 價格 × 庫存數量）。
# 找出最暢銷的書籍（可模擬借書次數）。

import librarymanager as l
lib_manager = l.libraryManager()

while True:
    print(f'歡迎來到圖書館:')
    print(f'1.顯示目前的圖書清單')
    print(f'2.新增或刪除書籍項目')
    print(f'3.更新書籍資訊')
    print(f'4.借書/還書功能')
    print(f'5.統計資訊')

    sec = int(input(f'請選擇服務項目(1-5):'))
    if sec == 1:
        lib_manager.show_book()
    elif sec ==2:
        while True:
            add_remove = input(f'請選擇新增/刪除/退出:')
            if add_remove == '新增':
                lib_manager.add_book()
            elif add_remove == '刪除':
                lib_manager.remove_book()
            elif add_remove == '退出':
                break
            else:
                print('請重新輸入')
                continue
    elif sec == 3:
        lib_manager.update_book()
    elif sec == 4:
        while True:
            borrow_return = input(f'請選擇借書/還書/退出:')
            if borrow_return =='借書':
                lib_manager.borrow_book()
            elif borrow_return =='還書':
                lib_manager.return_book()
            elif borrow_return =='退出':
                break
            else:
                print('請重新輸入')
                continue
    elif sec == 5:
        lib_manager.statistics()
    else:
        break