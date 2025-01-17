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
