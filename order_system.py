class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount

    def calculate_tax(self, tax_rate):
        return self.total_amount * tax_rate

    def display_order(self):
        print(f"Order ID      : {self.order_id}")
        print(f"Customer Name : {self.customer_name}")
        print(f"Order Date    : {self.order_date}")
        print(f"Total Amount  : Rp{self.total_amount:,.2f}")
        print("-" * 30)


class OrderProcessor:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def calculate_total_revenue(self):
        total_revenue = sum(order.total_amount for order in self.orders)
        return total_revenue

    def calculate_total_tax(self, tax_rate):
        total_tax = sum(order.calculate_tax(tax_rate) for order in self.orders)
        return total_tax

    def display_orders(self):
        print("\n=== ORDER LIST ===")
        for order in self.orders:
            order.display_order()


# Main Program
# Membuat objek order
order1 = Order("ORD001", "Andi", "2025-03-15", 250000)
order2 = Order("ORD002", "Budi", "2025-03-16", 500000)
order3 = Order("ORD003", "Citra", "2025-03-17", 750000)

# Membuat processor
processor = OrderProcessor()

# Menambahkan order ke list
processor.add_order(order1)
processor.add_order(order2)
processor.add_order(order3)

# Menampilkan semua order
processor.display_orders()

# Hitung total revenue
total_revenue = processor.calculate_total_revenue()
print(f"Total Revenue : Rp{total_revenue:,.2f}")

# Hitung total pajak
tax_rate = 0.11
total_tax = processor.calculate_total_tax(tax_rate)
print(f"Total Tax (11%): Rp{total_tax:,.2f}") 