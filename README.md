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

Program diuji dengan membuat 3 data order:

* ORD001
* ORD002
* ORD003

Kemudian seluruh order dimasukkan ke OrderProcessor untuk menghitung:

* total revenue
* total tax

## Run Program

python order_system.py
