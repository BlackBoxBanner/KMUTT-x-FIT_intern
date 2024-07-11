from sales_in_restaurants.generate_csv import generate_csv
from sales_in_restaurants.restaurants_sale_data import generate_restaurants_menu, generate_restaurants_sale_history, \
    generate_menu_add_on

generate_csv(name="data/add-on.csv", data=generate_menu_add_on())
generate_csv(name="data/menus.csv", data=generate_restaurants_menu())
generate_csv(name="data/sale.csv", data=generate_restaurants_sale_history(num=100 * 30, time=12 * 3))