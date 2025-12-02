from prettytable import PrettyTable
import matplotlib.pyplot as diagram

receipt = PrettyTable()
receipt.field_names = ['№','Продукт','Цена','Количество','Стоимость']

# списки для данных диаграммы
products = []
pay = []

for i in range(3):
  product = input('Укажите название продукта: ')
  price = int(input('Введите цену продукта: '))
  quantity = int(input('Укажите количество продукта: '))
  receipt.add_row([i+1, product, price, quantity, price*quantity])
  products.append(product)
  pay.append(price*quantity)

  print(receipt)
# построение и вывод диаграммы
  diagram.bar(product, pay, color = 'purple')
  diagram.show()
