from faker import Faker
from faker.providers import DynamicProvider
import random
from datetime import datetime, timedelta
import uuid
from tqdm import tqdm

# Initialize Faker with Australian locale https://franciswinifred.com.au/
fake = Faker(["en_AU"])


# Helper function to round prices to nearest .0, .25, .50, or .75
def custom_round_price(price):
    return round(price * 4) / 2


# Define menu items with categories
menus = [{'name': 'BIG BREAKFAST', 'category': 'All day breakfast', 'price': 21.0,
          'description': 'Cevapi sausage, halloumi, bacon, grilled tomatoes, hash brown, ajvar relish, poached eggs on sourdough',
          'cost': 19.99}, {'name': 'BREAKFAST BURGER', 'category': 'All day breakfast', 'price': 16.0,
                           'description': 'Cevapi sausage, swiss cheese, spinach, relish, mayo, fried egg, bacon on brioche bun served w/ hash brown',
                           'cost': 15.1}, {'name': 'AVOCADO TOAST', 'category': 'All day breakfast', 'price': 16.0,
                                           'description': 'Seeded toast w/ mixed seeds, marinated feta, dukkah, saffron infused hummus & crispy kale (V.VeO, GFO)',
                                           'cost': 15.71},
         {'name': 'COCONUT & CHIA PUDDING', 'category': 'All day breakfast', 'price': 17.5,
          'description': 'House made almond granola, berry compote served w/ seasonal fruit (V, Ve)', 'cost': 16.2},
         {'name': 'CHILLI SCRAMBLE', 'category': 'All day breakfast', 'price': 18.0,
          'description': 'Asparagus, crispy shallots, fresh chilli, parsley, feta & sambol oelek w/toast w/ toast (V, GFO)',
          'cost': 16.66}, {'name': 'EGG, BACON & CHEESE TOASTIE', 'category': 'All day breakfast', 'price': 10.5,
                           'description': 'Sourdough, fried egg, house made relish, cheese & bacon (GFO)',
                           'cost': 9.05},
         {'name': 'HUEVOS (SPANISH BAKED EGGS)', 'category': 'All day breakfast', 'price': 16.5,
          'description': 'Bell pepper, tomato, onion, spices & pecorino cheese w/ seeded toast (V, GFO)',
          'cost': 16.15}, {'name': 'EGGS ON TOAST', 'category': 'All day breakfast', 'price': 9.5,
                           'description': 'Free range - poached, scrambled or fried (V. GFO)', 'cost': 8.82},
         {'name': 'TOAST', 'category': 'All day breakfast', 'price': 7.0,
          'description': 'Sourdough or seeded toast w/ choice of butter/jam/peanut butter/Vegemite\n(V. Ve, GFO)',
          'cost': 5.35}, {'name': 'FRUIT TOAST', 'category': 'All day breakfast', 'price': 7.5,
                          'description': 'Raisins, apricots, prunes w/ citrus curd (V)', 'cost': 5.51},
         {'name': 'NEW YORK BAGEL BENEDICT', 'category': 'All day breakfast', 'price': 13.0,
          'description': 'Toasted bagel topped w/ wilted spinach. poached eggs & house made hollandaise sauce (V. GFO)',
          'cost': 12.89}, {'name': 'BURRITO BOWL', 'category': 'All day lunch', 'price': 18.5,
                           'description': 'Lime brown rice, avocado, purple cabbage. chargrilled corn, spiced black beans, pickled capsicum, spinach, tortilla chips (V, Ve, GFO)',
                           'cost': 18.19}, {'name': 'SOFT SHELL TORTILLAS', 'category': 'All day lunch', 'price': 18.5,
                                            'description': 'Spicy crispy chicken, avocado, chilli & corn salsa, chipotle aioli, slaw in soft shell tortillas\n(V, VeO)',
                                            'cost': 17.7},
         {'name': 'OPEN LAMB SOUVLAKI', 'category': 'All day lunch', 'price': 18.5,
          'description': '8 hour slow cooked lamb. pita bread, Greek salad, tzatziki w/ fries', 'cost': 18.04},
         {'name': 'WINIFRED WAGYU BURGER', 'category': 'All day lunch', 'price': 18.5,
          'description': 'House made 130g grilled wagyu beef patty, cheddar, lettuce, tomato, pickle, Winifred special sauce on brioche bun w/ side of fries (GFO)',
          'cost': 17.16}, {'name': 'TEXAN COUSIN BURGER', 'category': 'All day lunch', 'price': 18.5,
                           'description': 'Southern style spiced chicken, lettuce, apple slaw, tomato, swiss cheese, pickled mayo on brioche bun w/ side of fries (GFO)',
                           'cost': 17.86},
         {'name': 'VEGAN SWISS BROWN MUSHROOM BURGER', 'category': 'All day lunch', 'price': 18.0,
          'description': 'Crispy porcini mushroom patty, pickled red capsicum, lettuce, tomato, onion relish on sourdough bun w/ side of fries (V. Ve. (GFO)',
          'cost': 16.45}, {'name': 'Cheese & tomato', 'category': 'Toasties On Sourdough', 'price': 7,
                           'description': 'Toasties on sourdough', 'cost': 6.33},
         {'name': 'Chicken, avocado, lettuce & aioli', 'category': 'Toasties On Sourdough', 'price': 11.5,
          'description': 'Toasties on sourdough', 'cost': 11.29},
         {'name': 'Ham & cheese', 'category': 'Toasties On Sourdough', 'price': 7,
          'description': 'Toasties on sourdough', 'cost': 5.57},
         {'name': 'Ham, cheese & tomato', 'category': 'Toasties On Sourdough', 'price': 7.5,
          'description': 'Toasties on sourdough', 'cost': 7.36},
         {'name': 'Mushroom & cheese', 'category': 'Toasties On Sourdough', 'price': 8.5,
          'description': 'Toasties on sourdough', 'cost': 6.56},
         {'name': 'Avocado & cheese', 'category': 'Toasties On Sourdough', 'price': 9,
          'description': 'Toasties on sourdough', 'cost': 8.3},
         {'name': 'Bacon & tomato', 'category': 'Toasties On Sourdough', 'price': 8.5,
          'description': 'Toasties on sourdough', 'cost': 6.83},
         {'name': 'Bacon & egg', 'category': 'Toasties On Sourdough', 'price': 8.5,
          'description': 'Toasties on sourdough', 'cost': 7.16},
         {'name': 'BLT (bacon, lettuce & tomato)', 'category': 'Toasties On Sourdough', 'price': 11,
          'description': 'Toasties on sourdough', 'cost': 9.6},
         {'name': 'FRIES', 'category': 'Fries', 'price': 7.5, 'description': 'Served w/ aioli', 'cost': 7.29},
         {'name': 'Quiche w/ relish', 'category': 'House Made Pastries', 'price': 7.0, 'description': 'Served w/ aioli',
          'cost': 5.14},
         {'name': 'Savoury muffin', 'category': 'House Made Pastries', 'price': 6.0, 'description': 'Served w/ aioli',
          'cost': 5.31},
         {'name': 'Chicken, beef & pork or vegan sausage roll', 'category': 'House Made Pastries', 'price': 7,
          'description': 'Served w/ aioli', 'cost': 6.47},
         {'name': 'Lamington', 'category': 'CAKES, SLICES & SWEETS', 'price': 18.0,
          'description': 'House made assortment available from display - Aussie classic sponge cake dipped in chocolate and rolled in coconut',
          'cost': 16.64}, {'name': 'Pavlova', 'category': 'CAKES, SLICES & SWEETS', 'price': 20.0,
                           'description': 'House made assortment available from display - Crisp meringue base topped with fresh fruit and whipped cream',
                           'cost': 18.9}, {'name': 'Anzac Biscuit', 'category': 'CAKES, SLICES & SWEETS', 'price': 22.0,
                                           'description': 'House made assortment available from display - Crunchy, chewy oat cookies with a rich history',
                                           'cost': 20.87},
         {'name': 'Vanilla Slice', 'category': 'CAKES, SLICES & SWEETS', 'price': 20.0,
          'description': 'House made assortment available from display - Creamy vanilla custard between layers of flaky pastry, topped with icing',
          'cost': 19.68}, {'name': 'Tim Tam Cheesecake', 'category': 'CAKES, SLICES & SWEETS', 'price': 12.0,
                           'description': 'House made assortment available from display - Cheesecake with a Tim Tam biscuit base and chocolate topping',
                           'cost': 10.62}, {'name': 'Fairy Bread', 'category': 'CAKES, SLICES & SWEETS', 'price': 26.0,
                                            'description': 'House made assortment available from display - Simple yet delightful bread with butter and colorful sprinkles',
                                            'cost': 25.79},
         {'name': 'Flat White', 'category': 'Beverage', 'price': 4.0, 'description': 'A smooth, velvety milk coffee',
          'cost': 2.69},
         {'name': 'Latte', 'category': 'Beverage', 'price': 4.5, 'description': 'Creamy coffee with steamed milk',
          'cost': 3.96}, {'name': 'Cappuccino', 'category': 'Beverage', 'price': 4.5,
                          'description': 'Rich coffee with a frothy top, sprinkled with cocoa', 'cost': 2.63},
         {'name': 'Long Black', 'category': 'Beverage', 'price': 3.5,
          'description': 'Double shot of espresso with hot water', 'cost': 3.06},
         {'name': 'Espresso', 'category': 'Beverage', 'price': 3.0, 'description': 'Strong and black shot of coffee',
          'cost': 1.6}, {'name': 'Mocha', 'category': 'Beverage', 'price': 5.0,
                         'description': 'Coffee with chocolate, topped with steamed milk and cocoa', 'cost': 3.76},
         {'name': 'Hot Chocolate', 'category': 'Beverage', 'price': 4.0, 'description': 'Rich and creamy hot chocolate',
          'cost': 3.6},
         {'name': 'Orange Juice', 'category': 'Beverage', 'price': 5.0, 'description': 'Freshly squeezed orange juice',
          'cost': 4.32},
         {'name': 'Apple Juice', 'category': 'Beverage', 'price': 5.0, 'description': 'Freshly pressed apple juice',
          'cost': 4.12},
         {'name': 'Lemonade', 'category': 'Beverage', 'price': 3.0, 'description': 'Classic refreshing lemonade',
          'cost': 2.69},
         {'name': 'Cola', 'category': 'Beverage', 'price': 3.0, 'description': 'Popular carbonated cola Beverage',
          'cost': 1.45},
         {'name': 'Sparkling Water', 'category': 'Beverage', 'price': 3.0, 'description': 'Refreshing carbonated water',
          'cost': 2.12}]

# Define add_on menu items with categories
add_on = [{'menu': 'Sparkling Water', 'name': 'Ice', 'price': 0.0, 'cost': 1.24},
          {'menu': 'Sparkling Water', 'name': 'Lemon Slice', 'price': 0.5, 'cost': 0.58},
          {'menu': 'Sparkling Water', 'name': 'Lime Slice', 'price': 0.5, 'cost': 0.65},
          {'menu': 'Cola', 'name': 'Ice', 'price': 0.0, 'cost': 0.48},
          {'menu': 'Cola', 'name': 'Lemon Slice', 'price': 0.5, 'cost': 0.32},
          {'menu': 'Lemonade', 'name': 'Ice', 'price': 0.0, 'cost': 0.87},
          {'menu': 'Lemonade', 'name': 'Lemon Slice', 'price': 0.5, 'cost': 0.98},
          {'menu': 'Apple Juice', 'name': 'Ice', 'price': 0.0, 'cost': 1.28},
          {'menu': 'Orange Juice', 'name': 'Ice', 'price': 0.0, 'cost': 0.22},
          {'menu': 'Hot Chocolate', 'name': 'Whipped Cream', 'price': 0.5, 'cost': 1.36},
          {'menu': 'Hot Chocolate', 'name': 'Marshmallows', 'price': 0.5, 'cost': 1.28},
          {'menu': 'Mocha', 'name': 'Extra Shot', 'price': 0.5, 'cost': 0.75},
          {'menu': 'Mocha', 'name': 'Almond Milk', 'price': 0.5, 'cost': 1.42},
          {'menu': 'Mocha', 'name': 'Soy Milk', 'price': 0.5, 'cost': 1.07},
          {'menu': 'Mocha', 'name': 'Whipped Cream', 'price': 0.5, 'cost': 0.03},
          {'menu': 'Espresso', 'name': 'Extra Shot', 'price': 0.5, 'cost': 0.24},
          {'menu': 'Long Black', 'name': 'Extra Shot', 'price': 0.5, 'cost': 0.01},
          {'menu': 'Cappuccino', 'name': 'Extra Shot', 'price': 0.5, 'cost': 0.12},
          {'menu': 'Cappuccino', 'name': 'Almond Milk', 'price': 0.5, 'cost': 0.07},
          {'menu': 'Cappuccino', 'name': 'Soy Milk', 'price': 0.5, 'cost': 0.84},
          {'menu': 'Cappuccino', 'name': 'Hazelnut Syrup', 'price': 0.5, 'cost': 0.36},
          {'menu': 'Latte', 'name': 'Extra Shot', 'price': 0.5, 'cost': 0.61},
          {'menu': 'Latte', 'name': 'Almond Milk', 'price': 0.5, 'cost': 0.95},
          {'menu': 'Latte', 'name': 'Soy Milk', 'price': 0.5, 'cost': 0.32},
          {'menu': 'Latte', 'name': 'Caramel Syrup', 'price': 0.5, 'cost': 0.16},
          {'menu': 'Flat White', 'name': 'Extra Shot', 'price': 0.5, 'cost': 0.05},
          {'menu': 'Flat White', 'name': 'Almond Milk', 'price': 0.5, 'cost': 0.05},
          {'menu': 'Flat White', 'name': 'Soy Milk', 'price': 0.5, 'cost': 1.31},
          {'menu': 'Flat White', 'name': 'Vanilla Syrup', 'price': 0.5, 'cost': 0.74},
          {'menu': 'BURRITO BOWL', 'name': 'Chicken', 'price': 4.5, 'cost': 3.33},
          {'menu': 'AVOCADO TOAST', 'name': 'Free range eggs', 'price': 2.5, 'cost': 2.17},
          {'menu': 'AVOCADO TOAST', 'name': 'Smoked salmon', 'price': 4.5, 'cost': 3.47},
          {'menu': 'AVOCADO TOAST', 'name': 'Grilled halloumi', 'price': 3.0, 'cost': 1.44},
          {'menu': 'AVOCADO TOAST', 'name': 'Bacon', 'price': 4.5, 'cost': 3.77},
          {'menu': 'NEW YORK BAGEL BENEDICT', 'name': 'Bacon', 'price': 3.5, 'cost': 3.0},
          {'menu': 'NEW YORK BAGEL BENEDICT', 'name': 'BBQ pulled pork', 'price': 3.5, 'cost': 3.14},
          {'menu': 'NEW YORK BAGEL BENEDICT', 'name': 'Smoked salmon', 'price': 3.5, 'cost': 3.11},
          {'menu': 'EGGS ON TOAST', 'name': 'Salmon, bacon, cevapi, Chorizo', 'price': 4.5, 'cost': 3.02},
          {'menu': 'EGGS ON TOAST', 'name': 'Smashed avocado, hash brown, mushroom, Grilled halloumi, baked beans',
           'price': 4.0, 'cost': 3.09},
          {'menu': 'EGGS ON TOAST', 'name': 'Grilled tomatoes, spinach, Feta', 'price': 3.0, 'cost': 2.8},
          {'menu': 'EGGS ON TOAST', 'name': 'Free range egg, ajvar. hollandaise', 'price': 2.5, 'cost': 0.77},
          {'menu': 'EGGS ON TOAST', 'name': 'Gluten free bread', 'price': 1.5, 'cost': 0.58},
          {'menu': 'EGGS ON TOAST', 'name': 'Toast, curd', 'price': 1, 'cost': 0.22},
          {'menu': 'HUEVOS (SPANISH BAKED EGGS)', 'name': 'Traditional spanish chorizo', 'price': 4.5, 'cost': 4.05},
          {'menu': 'Hot Chocolate', 'name': 'Whipped Cream', 'price': 0.5, 'cost': 0.2},
          {'menu': 'Hot Chocolate', 'name': 'Marshmallows', 'price': 0.5, 'cost': 0.37}]

# Define a DynamicProvider for menus
menus_provider = DynamicProvider(
    provider_name="menus",
    elements=menus
)

# Add the custom provider to Faker
fake.add_provider(menus_provider)


# Define a function to generate add_on menu with UUIDs
def generate_menu_add_on():
    menu_add_on = []

    for data in tqdm(add_on, desc="Generating Menu Add On"):
        menu_add_on.append({
            "uuid": str(uuid.uuid4()),
            **data
        })

    return menu_add_on


# Define a function to generate a menu with UUIDs
def generate_restaurants_menu():
    menu_items = []

    for data in tqdm(menus, desc="Generating menu items"):
        menu_items.append({
            "uuid": str(uuid.uuid4()),
            **data
        })

    return menu_items


# Helper function to check if a given datetime is within opening hours
def is_open(date_time):
    opening_hours = {
        0: (None, None),  # Monday: Closed
        1: ("07:00", "15:00"),  # Tuesday
        2: ("07:00", "15:00"),  # Wednesday
        3: ("07:00", "15:00"),  # Thursday
        4: ("07:00", "15:00"),  # Friday
        5: ("08:00", "15:00"),  # Saturday
        6: ("08:00", "15:00"),  # Sunday
    }

    day = date_time.weekday()
    opening_time, closing_time = opening_hours[day]

    if opening_time is None or closing_time is None:
        return False

    opening_time = datetime.strptime(opening_time, "%H:%M").time()
    closing_time = datetime.strptime(closing_time, "%H:%M").time()
    current_time = date_time.time()

    return opening_time <= current_time <= closing_time


# Function to generate a dynamic sales history
def generate_restaurants_sale_history(num=3000, month=1, time=1):
    num = num * time
    month = month * time

    sales_history = []
    start_date = datetime.now() - timedelta(days=30 * month)

    beverage_items = [item for item in menus if item["category"] == "Beverage"]
    other_items = [item for item in menus if item["category"] != "Beverage"]

    # Factors affecting sales
    day_factors = {0: 0.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.2, 5: 1.5, 6: 1.3}  # Monday to Sunday
    time_factors = {"morning": 1.0, "afternoon": 1.5, "evening": 1.2}

    for _ in tqdm(range(num), desc="Generating sales history"):
        while True:
            sale_time = start_date + timedelta(minutes=random.randint(0, 30 * 24 * 60 * month))
            if is_open(sale_time):
                break

        day_factor = day_factors[sale_time.weekday()]
        hour = sale_time.hour
        if 7 <= hour < 12:
            time_factor = time_factors["morning"]
        elif 12 <= hour < 17:
            time_factor = time_factors["afternoon"]
        else:
            time_factor = time_factors["evening"]

        # Adjust probability of selecting a beverage
        beverage_prob = 0.4 * day_factor * time_factor
        if random.random() < beverage_prob:
            menu_item = random.choice(beverage_items)
        else:
            menu_item = random.choice(other_items)

        # Adjust probability of selecting add-ons
        add_ons = [ao for ao in add_on if ao["menu"] == menu_item["name"]]
        selected_add_ons = []
        add_ons_prob = 0.2 * day_factor * time_factor
        if add_ons and random.random() < add_ons_prob:
            selected_add_ons = random.sample(add_ons, k=random.randint(1, len(add_ons)))

        sales_history.append({
            "uuid": str(uuid.uuid4()),
            "date_time": sale_time,
            "menu_item": menu_item["name"],
            "add_ons": [ao["name"] for ao in selected_add_ons],
        })

    return sales_history
