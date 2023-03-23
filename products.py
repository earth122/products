# 建立記帳程式
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = [] # 創作二維清單
	p.append(name)
	p.append(price)
	# p = [name, price] 等於line 8-10
	products.append(p)
	# products.append([name, price]) 等於line 8-10, 12
print(products)

products[0][0] # 存取大清單(index 0)內的二維清單(index 0)