from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("check_login", views.check_login, name="check_login"),

    path("service/", views.service, name="service"),
    path("create_service/", views.create_service, name="create_service"),
    path('service-list/', views.service_list, name='service_list'),
    path('edit-service/<int:service_id>/',
         views.edit_service, name='edit_service'),
    path('delete-service/<int:service_id>/',
         views.delete_service, name='delete_service'),
    path('update-service/<int:service_id>/',
         views.update_service, name='update_service'),

    path("item/", views.item, name="item"),
    path("create_item/", views.create_item, name="create_item"),
    path('item-list/', views.item_list, name='item_list'),
    path('edit-item/<int:item_id>/',
         views.edit_item, name='edit_item'),
    path('delete-item/<int:item_id>/',
         views.delete_item, name='delete_item'),
    path('update-item/<int:item_id>/',
         views.update_item, name='update_item'),
    path('get-item-qty/', views.get_item_qty, name='get_item_qty'),
    path('sell-item/', views.sell_item, name='sell_item'),


    path("car/", views.car, name="car"),
    path("create_car/", views.create_car, name="create_car"),
    path('car-list/', views.car_list, name='car_list'),
    path('edit-car/<int:car_id>/',
         views.edit_car, name='edit_car'),
    path('delete-car/<int:car_id>/',
         views.delete_car, name='delete_car'),
    path('update-car/<int:car_id>/',
         views.update_car, name='update_car'),


    path("stuff/", views.stuff, name="stuff"),
    path("create_stuff/", views.create_stuff, name="create_stuff"),
    path('stuff-list/', views.stuff_list, name='stuff_list'),
    path('edit-stuff/<int:stuff_id>/',
         views.edit_stuff, name='edit_stuff'),
    path('delete-stuff/<int:stuff_id>/',
         views.delete_stuff, name='delete_stuff'),
    path('update-stuff/<int:stuff_id>/',
         views.update_stuff, name='update_stuff'),


    path("sale/", views.sale, name="sale"),
    path("create_sale/", views.create_sale, name="create_sale"),
    path('sales-list/', views.sales_list, name='sales_list'),
    path('sales-list-month/', views.sales_list_month, name='sales_list_month'),
    path('sales-list-all/', views.sales_list_all, name='sales_list_all'),
    path('dues-list/', views.dues_list, name='dues_list'),
    path('dues-list-pending/', views.dues_list_pending, name='dues_list_pending'),
    path('edit-sale/<int:sale_id>/',
         views.edit_sale, name='edit_sale'),
    path('delete-sale/<int:sale_id>/',
         views.delete_sale, name='delete_sale'),
#     path('delete-sale-all/<int:sale_id>/',
#          views.delete_sale, name='delete_sale_all'),



    path("update_due/<int:due_id>/", views.update_due, name="update_due"),




    path("cost/", views.cost, name="cost"),
    path("create_cost/", views.create_cost, name="create_cost"),
    path('costs-list/', views.costs_list, name='costs_list'),
    path('costs-list-day/', views.costs_list_day, name='costs_list_day'),
    path('costs-list-month/', views.costs_list_month, name='costs_list_month'),
    path('edit-cost/<int:cost_id>/',
         views.edit_cost, name='edit_cost'),
    path('delete-cost/<int:cost_id>/',
         views.delete_cost, name='delete_cost'),
    path('update-cost/<int:cost_id>/',
         views.update_cost, name='update_cost'),

    path("salary/", views.salary, name="salary"),
    path("salary/view", views.salary_view, name="salary_view"),
    path("salary_report/<int:stuff_id>/",
         views.salary_report, name="salary_report"),
    path("create_salary/", views.create_salary, name="create_salary"),
    path("getSalaryInfo/<int:stuff_id>",
         views.getSalaryInfo, name="salary_info"),
    path('salary-list/', views.salaries_list, name='salary_list'),
    path('edit-salary/<int:salary_id>/',
         views.edit_salary, name='edit_salary'),
    path('delete-salary/<int:salary_id>/',
         views.delete_salary, name='delete_salary'),
    path('update-salary/<int:salary_id>/',
         views.update_salary, name='update_salary'),

    path("stock/", views.stock, name="stock"),
    path("create_stock/", views.create_stock, name="create_stock"),
    path('stock_list/', views.stock_list, name='stock_list'),
    path('edit_stock/<int:stock_id>/',
         views.edit_stock, name='edit_stock'),
    path('delete_stock/<int:stock_id>/',
         views.delete_stock, name='delete_stock'),
    path('update_stock/<int:stock_id>/',
         views.update_stock, name='update_stock'),
    path('search_stock/',
         views.search_stock, name='search_stock'),

    path("bill/", views.bill, name="bill"),

    path("job-card/", views.job_card, name="job_card"),
    path("create_jobcard/", views.create_jobcard, name="create_jobcard"),
    path('jobcard_list/', views.jobcard_list, name='jobcard_list'),
    path('view_jobcard/<int:order_id>', views.view_jobcard, name='view_jobcard'),
    path('search_jobcard/',
         views.search_jobcard, name='search_jobcard'),
    path('delete_jobcard/<int:order_id>',
         views.delete_jobcard, name='delete_jobcard'),

    path('monthly-statement/', views.monthly_statement, name='monthly_statement'),

    path("reports/", views.reports, name="reports"),


]
