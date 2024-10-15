class Laptop:
    def __init__(self,id,brand,os,price,rating):
        self.laptopId = id
        self.laptopBrand = brand
        self.os = os
        self.price = price
        self.rating = rating

laptops = []
# for i in range(4):
#     id = int(input())
#     brand = input()
#     os = input()
#     price = int(input())
#     rating = int(input())
#     laptops[i] = Laptop(id,brand,os,price,rating)

searchBrand = input()
searchOs = input()
result = countOfLaptopByBrand(laptops,searchBrand) # type: ignore
print(result)

def countOfLaptopByBrand(laptops,searchBrand):
    return 1