class libraryManager:
    def __init__(self):
        self.library_list = {}
        self.borrow_list = {}

    def add_book(self):
        book = input('請輸入書名:')
        author = input('請輸入作者:')
        price = int(input('請輸入價格:'))
        quantity = int(input('請輸入庫存數量:'))
        self.library_list[book] = {'author': author, 'price': price, 'quantity': quantity}

    def remove_book(self):
        book = input('請輸入要刪除的書名:')
        if book in self.library_list.keys():
            del self.library_list[book]
            print(f'已成功移除{book}')
        else:
            print(f'沒有這本書')

    def show_book(self):
        for books, details in self.library_list.items():
            print("書名: {0}, 作者: {1}, 價格: {2}, 庫存: {3}".format(books,details['author'],details['price'],details['quantity']))

    def update_book(self):
        book = input('請輸入要更新的書名:')
        if book in self.library_list.keys():
            price = int(input(f'請輸入{book}的新價格:'))
            quantity = int(input(f'請輸入{book}的新庫存數量:'))
            self.library_list[book]['price'] = price
            self.library_list[book]['quantity'] = quantity
        else:
            print(f'沒有這本書')

    def borrow_book(self):
        borrow_book = input('請輸入要借的書名:')
        if borrow_book in self.library_list.keys():
            borrow_quantity = int(input(f'請輸入{borrow_book}的借書的數量:'))
            if borrow_quantity <= self.library_list[borrow_book]['quantity']:
                if borrow_book in self.borrow_list:
                    self.borrow_list[borrow_book] += borrow_quantity
                else:
                    self.borrow_list[borrow_book] = borrow_quantity
                self.library_list[borrow_book]['quantity'] -= borrow_quantity
            else:
                print(f'超出庫存數量')
        else:
            print(f'沒有這本書')

    def return_book(self):
        return_book = input('請輸入要還的書名:')
        if return_book in self.library_list.keys():
            try:
                return_quantity = int(input(f'請輸入要還{return_book}的數量:'))
                if return_quantity > 0:
                    self.library_list[return_book]['quantity'] += return_quantity
                    print(f"成功還{return_quantity}本{return_book}")
                else:
                    print(f'數量必須為正數')
            except ValueError:
                print(f'請輸入有效數量')
        else:
            return_author = input('請輸入還書作者:')
            try:
                return_price = int(input('請輸入還書價格:'))
                return_quantity = int(input('請輸入還書庫存數量:'))
                if return_price > 0 and return_quantity > 0:
                    self.library_list[return_book] = {'author' : return_author,'price' : return_price, 'quantity':return_quantity}
                else:
                    print(f'數量必須為正數')
            except ValueError:
                print('請輸入有效數量')

    def statistics(self):
        total = 0
        popular = ''
        max_borrowed = 0
        for books,details in self.library_list.items():
            value = details['price'] * details['quantity']
            total += value
        print(f'所有書籍的總價值為{total}')
        for borrow_books,quantity in self.borrow_list.items():
            if quantity > max_borrowed:
                popular = borrow_books
                max_borrowed = quantity
        print(f"最暢銷書籍為{popular}數量為{max_borrowed}")
