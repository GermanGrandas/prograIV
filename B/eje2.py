
from products import *
from ShopingList import *


if __name__=='__main__':
    values = [100,"001","5V"]
    p1 = Micro(values)
    p2 = Resistencia([50,"009","54ohm"])
    total = ShopList()

    total.add(p1)
    total.add(p2)
    t = total.total()
    print t




