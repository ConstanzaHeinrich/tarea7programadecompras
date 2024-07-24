from customer import Customer
from item import Item
from seller import Seller

seller = Seller("DICストア")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memoria", 13880, seller)
    Item("Placa base", 28980, seller)
    Item("Fuente de alimentación", 8980, seller)
    Item("Caja PC", 8727, seller)
    Item("Disco duro de 3,5 pulgadas", 10980, seller)
    Item("SSD de 2,5 pulgadas", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("Refrigerador CPU", 13400, seller)
    Item("Tarjeta gráfica", 23800, seller)

print("🤖 Por favor, dime tu nombre")
customer = Customer(input())

print("🏧 Por favor, introduzca la cantidad que se cargará en la billetera")
customer.wallet.deposit(int(input()))

print("🛍️ Empieza a comprar")
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos")
    seller.show_items()

    print("️️⛏ Por favor, introduzca el número de archivos")
    number = int(input())

    print("⛏ Por favor, introduzca la cantidad del producto")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 合計金額: {customer.cart.total_amount()}")

    print("😭 Te gustaría terminar tus compras？(yes/no)")
    end_shopping = input() == "yes"

print("💸 Quieres confirmar la compra？(yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈El resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{customer.name}Propiedad de")
customer.show_items()
print(f"😱👛 {customer.name}Saldo de la billetera: {customer.wallet.balance}")

print(f"📦 {seller.name}Estado de las reservas")
seller.show_items()
print(f"😻👛 {seller.name}Saldo de la billetera: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 Importe total: {customer.cart.total_amount()}")

print("🎉 Final")
