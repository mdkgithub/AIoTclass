class C_AiStore:

    def __init__(self, store_name, store_id, store_address):
        self.store_name = store_name
        self.store_id = store_id
        self.store_address = store_address
        self.store_count = 0
        self.store_price = 0

    # 상품개수, 상품가격
    def set_product(self, store_count, store_price):
        self.store_count += store_count
        self.store_price += store_price

    # 구매개수, 상품가격
    def buy_item(self, order_unit, input_price):
        self.order_unit += order_unit
        self.input_price += input_price
        self.store_count = 0
        self.store_price = 1


        if self.bank_balance:
            print('잔돈은   입니다')
        elif self.product_unit < order_unit:
            print('재고가   부족합니다')
        elif self.iput_price < store_price:
            print('금액이   부족합니다')
        else:
            print('구매 개수와 상품 가격을 입력하세요')


    def get_name(self):
        return self.store_name

    def get_id(self):
        return self.store_id

    def get_locate(self):
        return self.store_address

    def get_count(self):
        return self.store_count

    def get_price(self):
        return self.store_price


if __name__ == '__main__':

    print('스토어 지점이름 입력:')
    s_name = input()
    print('스토어 지점아이디 입력:')
    s_id = input()
    print('스토어 위치 입력:')
    s_locate = input()

    aistore = C_AiStore(s_name, s_id, s_locate)
    print('스토어 지점이름: ', aistore.store_name, '스토어 지점ID: ', aistore.store_id, '스토어 위치', aistore.store_address, '스토어가 생성되었습니다.')



    for button in range(0, 10):
        print('소트어 조회는 1번, 구매는 2번, 상품 관리는 3번, 종료는 4번을 눌려주세요')
        button = int(input())

        if button == 1:
            info = input('이름:')
            aistore.get_name()

            info = input('아이디: ')
            aistore.get_id()

            info = input('재고개수: ')
            aistore.get_count()

            info = input('상품가격: ')
            aistore.get_price()

        elif button == 2:
            info = int(input('구매할 상품 개수 입력: '))
            print('필요한 금액: ')
            aistore.product_price()
            info = int(input('필요한 금액 출력: '))
            aistore.buy_item(info)
        elif button == 3:
            info = int(input('상품 재고 입력: '))
            aistore.product_unit(info)
            info= int(input('상품 가격 입력: '))
            aistore.product_price(info)
            # aistore.get_rat()
        elif button == 4:
            break
        # customer.get_rat()