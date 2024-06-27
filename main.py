import random
from sales_in_restaurants.generate_csv import generate_csv
from sales_in_restaurants.restaurants_sale_data import generate_restaurants_menu, generate_restaurants_sale_history, \
    generate_menu_add_on

generate_csv("./data/add-on.csv", generate_menu_add_on())
generate_csv("./data/menus.csv", generate_restaurants_menu())
generate_csv("./data/sale.csv", generate_restaurants_sale_history(num=100 * 30, time=12 * 3))