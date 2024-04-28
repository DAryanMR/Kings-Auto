from django.db import models


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    service_charge = models.DecimalField(max_digits=8, decimal_places=2)


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_cost = models.DecimalField(max_digits=8, decimal_places=2)
    item_charge = models.DecimalField(max_digits=8, decimal_places=2)


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    qty = models.IntegerField(default=0)


class Cost(models.Model):
    cost_id = models.AutoField(primary_key=True)
    cost_date = models.DateField()
    cost_name = models.CharField(max_length=100, null=True)
    cost_amount = models.DecimalField(max_digits=8, decimal_places=2)


class Stuff(models.Model):
    stuff_id = models.AutoField(primary_key=True)
    join_date = models.CharField(max_length=100, null=True)
    stuff_name = models.CharField(max_length=100, null=True)
    stuff_father = models.CharField(max_length=100, null=True)
    stuff_nid = models.CharField(max_length=100, null=True)
    stuff_address = models.CharField(max_length=100, null=True)
    stuff_mobile = models.CharField(max_length=100, null=True)
    stuff_salary = models.DecimalField(max_digits=10, decimal_places=2)
    duty_days = models.IntegerField(null=True)


class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    memo_id = models.IntegerField(default=None, null=True)
    sale_date = models.DateField()
    payment_method = models.CharField(max_length=100, null=True)
    customer_name = models.CharField(max_length=100, null=True)
    car_name = models.CharField(max_length=100, null=True)
    car_reg = models.CharField(max_length=20, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    qty = models.IntegerField(default=1)
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE, default=1)
    sale_total = models.DecimalField(max_digits=10, decimal_places=2)


class Dues(models.Model):
    due_id = models.AutoField(primary_key=True)
    due_date = models.DateField(default=None)
    memo_id = models.ForeignKey(Sale, on_delete=models.CASCADE)
    due_total = models.DecimalField(max_digits=10, decimal_places=2)
    due_received = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)


class Salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    salary_date = models.DateField()
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    paid_status = models.BooleanField(default=False)


class Jobcard(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.CharField(max_length=100, default=None, null=True)
    customer_name = models.CharField(max_length=100, default=None, null=True)
    customer_address = models.CharField(
        max_length=100, default=None, null=True)
    customer_phone = models.CharField(max_length=100, default=None, null=True)
    chassis = models.CharField(max_length=100, default=None, null=True)
    vehicle = models.CharField(max_length=100, default=None, null=True)
    model_year = models.CharField(max_length=100, default=None, null=True)
    model = models.CharField(max_length=100, default=None, null=True)
    engine = models.CharField(max_length=100, default=None, null=True)
    reg = models.CharField(max_length=100, default=None, null=True)


class CustomerRequest(models.Model):
    sl_no = models.IntegerField(default=None, null=True)
    order_id = models.ForeignKey(Jobcard, on_delete=models.CASCADE)
    request = models.CharField(max_length=100, default=None, null=True)
    category = models.CharField(max_length=100, default=None, null=True)
    charge = models.CharField(max_length=100, default=None, null=True)


class Diagnosis(models.Model):
    sl_no = models.IntegerField(default=None, null=True)
    order_id = models.ForeignKey(Jobcard, on_delete=models.CASCADE)
    diagnosis_detail = models.CharField(
        max_length=100, default=None, null=True)
    ref_by = models.CharField(max_length=100, default=None, null=True)
    diagnosed_by = models.CharField(max_length=100, default=None, null=True)
    driver_signature = models.CharField(
        max_length=100, default=None, null=True)


class IssueDemand(models.Model):
    sl_no = models.IntegerField(default=None, null=True)
    order_id = models.ForeignKey(Jobcard, on_delete=models.CASCADE)
    material_description = models.CharField(
        max_length=100, default=None, null=True)
    material_qty = models.CharField(max_length=100, default=None, null=True)
    material_price = models.CharField(max_length=100, default=None, null=True)
    req_description = models.CharField(max_length=100, default=None, null=True)
    req_qty = models.CharField(max_length=100, default=None, null=True)
    req_sign = models.CharField(max_length=100, default=None, null=True)


class IssueDemandEngineer(models.Model):
    sl_no = models.IntegerField(default=None, null=True)
    order_id = models.ForeignKey(Jobcard, on_delete=models.CASCADE)
    engineer = models.CharField(
        max_length=100, default=None, null=True)
    technician = models.CharField(max_length=100, default=None, null=True)
