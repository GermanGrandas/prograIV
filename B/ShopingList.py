
class ShopList(object):
    def __init__(self):
        self.__list = []
    
    def add(self,product):
        self.__list.append(product)
    
    def total(self):
        total=0
        for elemento in self.__list:
            total+=elemento.getPrice()
        return total


