import os # operating system

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續，跳到下一次迴圈
			name, price = line.strip().split(',') # 字串以「,」做切割，分別存成 name price
			products.append([name, price])
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		# p = [] # 創作二維清單
		# p.append(name)
		# p.append(price)
		# p = [name, price] # 等於line 8-10
		# products.append(p)
		products.append([name, price]) # 等於line 8-11, 12
	print(products)
	# products[0][0] # 存取大清單(index 0)內的二維清單(index 0)
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		# print(p) # 列印出大清單裡的東西，即二維清單
		# print(p[0]) # 列印出每一個二維清單的index 0
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:
	# 寫入和讀取檔案的時候，都會涉及編碼，所以建議在'w'之後設定編碼 'w', encoding = 'utf-8'
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')
			# line 8 將 price 存成整數，所以p[1]要轉換成str，才能做字串相加

# 主程式
def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案是否存在
		print('yeah! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()