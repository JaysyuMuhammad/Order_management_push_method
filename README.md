# Order_management_push_method
# Order Management System

Program ini dibuat menggunakan Python dengan konsep Object Oriented Programming (OOP) untuk mensimulasikan pipeline data pemrosesan pesanan pelanggan pada sistem e-commerce.

## OOP Principles Used

### 1. Class

Program menggunakan dua class:

* Order
* OrderProcessor

### 2. Object

Setiap pesanan dibuat sebagai object dari class Order.

### 3. Method

Method digunakan untuk:

* menghitung pajak pesanan
* menampilkan detail pesanan
* menghitung total revenue
* menghitung total tax

### 4. Encapsulation

Setiap data order disimpan dalam atribut object menggunakan self.

## Testing

Saya membuat 3 data pesanan:

* ORD001 total Rp250.000
* ORD002 total Rp500.000
* ORD003 total Rp750.000

Program dijalankan menggunakan tax rate 11%.

Hasil output program:

* Total Revenue = Rp1.500.000
* Total Tax = Rp165.000


## Run Program

python order_system.py
