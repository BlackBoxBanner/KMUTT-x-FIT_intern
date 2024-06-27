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
menus = [
    {
        "name": "BIG BREAKFAST",
        "category": "All day breakfast",
        "price": 21.00,
        "description": "Cevapi sausage, halloumi, bacon, grilled tomatoes, hash brown, ajvar relish, poached eggs on sourdough",
    },
    {
        "name": "BREAKFAST BURGER",
        "category": "All day breakfast",
        "price": 16.00,
        "description": "Cevapi sausage, swiss cheese, spinach, relish, mayo, fried egg, bacon on brioche bun served w/ hash brown",
    },
    {
        "name": "AVOCADO TOAST",
        "category": "All day breakfast",
        "price": 16.00,
        "description": "Seeded toast w/ mixed seeds, marinated feta, dukkah, saffron infused hummus & crispy kale (V.VeO, GFO)",
    },
    {
        "name": "COCONUT & CHIA PUDDING",
        "category": "All day breakfast",
        "price": 17.50,
        "description": "House made almond granola, berry compote served w/ seasonal fruit (V, Ve)",
    },
    {
        "name": "CHILLI SCRAMBLE",
        "category": "All day breakfast",
        "price": 18.00,
        "description": "Asparagus, crispy shallots, fresh chilli, parsley, feta & sambol oelek w/toast w/ toast (V, GFO)",
    },
    {
        "name": "EGG, BACON & CHEESE TOASTIE",
        "category": "All day breakfast",
        "price": 10.5,
        "description": "Sourdough, fried egg, house made relish, cheese & bacon (GFO)",
    },
    {
        "name": "HUEVOS (SPANISH BAKED EGGS)",
        "category": "All day breakfast",
        "price": 16.5,
        "description": "Bell pepper, tomato, onion, spices & pecorino cheese w/ seeded toast (V, GFO)",
    },
    {
        "name": "EGGS ON TOAST",
        "category": "All day breakfast",
        "price": 9.5,
        "description": "Free range - poached, scrambled or fried (V. GFO)",
    },
    {
        "name": "TOAST",
        "category": "All day breakfast",
        "price": 7.00,
        "description": "Sourdough or seeded toast w/ choice of butter/jam/peanut butter/Vegemite\n(V. Ve, GFO)",
    },
    {
        "name": "FRUIT TOAST",
        "category": "All day breakfast",
        "price": 7.50,
        "description": "Raisins, apricots, prunes w/ citrus curd (V)",
    },
    {
        "name": "NEW YORK BAGEL BENEDICT",
        "category": "All day breakfast",
        "price": 13.00,
        "description": "Toasted bagel topped w/ wilted spinach. poached eggs & house made hollandaise sauce (V. GFO)",
    },
    {
        "name": "BURRITO BOWL",
        "category": "All day lunch",
        "price": 18.5,
        "description": "Lime brown rice, avocado, purple cabbage. chargrilled corn, spiced black beans, pickled capsicum, spinach, tortilla chips (V, Ve, GFO)"
    },
    {
        "name": "SOFT SHELL TORTILLAS",
        "category": "All day lunch",
        "price": 18.5,
        "description": "Spicy crispy chicken, avocado, chilli & corn salsa, chipotle aioli, slaw in soft shell tortillas\n(V, VeO)",
    },
    {
        "name": "OPEN LAMB SOUVLAKI",
        "category": "All day lunch",
        "price": 18.5,
        "description": "8 hour slow cooked lamb. pita bread, Greek salad, tzatziki w/ fries",
    },
    {
        "name": "WINIFRED WAGYU BURGER",
        "category": "All day lunch",
        "price": 18.5,
        "description": "House made 130g grilled wagyu beef patty, cheddar, lettuce, tomato, pickle, Winifred special sauce on brioche bun w/ side of fries (GFO)",
    },
    {
        "name": "TEXAN COUSIN BURGER",
        "category": "All day lunch",
        "price": 18.5,
        "description": "Southern style spiced chicken, lettuce, apple slaw, tomato, swiss cheese, pickled mayo on brioche bun w/ side of fries (GFO)",
    },
    {
        "name": "VEGAN SWISS BROWN MUSHROOM BURGER",
        "category": "All day lunch",
        "price": 18.0,
        "description": "Crispy porcini mushroom patty, pickled red capsicum, lettuce, tomato, onion relish on sourdough bun w/ side of fries (V. Ve. (GFO)",
    },
    {
        "name": "Cheese & tomato",
        "category": "Toasties On Sourdough",
        "price": 7,
        "description": "Toasties on sourdough",
    },
    {
        "name": "Chicken, avocado, lettuce & aioli",
        "category": "Toasties On Sourdough",
        "price": 11.5,
        "description": "Toasties on sourdough",
    },
    {
        "name": "Ham & cheese",
        "category": "Toasties On Sourdough",
        "price": 7,
        "description": "Toasties on sourdough",
    },
    {
        "name": "Ham, cheese & tomato",
        "category": "Toasties On Sourdough",
        "price": 7.5,
        "description": "Toasties on sourdough",
    },
    {
        "name": "Mushroom & cheese",
        "category": "Toasties On Sourdough",
        "price": 8.5,
        "description": "Toasties on sourdough",
    },
    {
        "name": "Avocado & cheese",
        "category": "Toasties On Sourdough",
        "price": 9,
        "description": "Toasties on sourdough",
    },
    {
        "name": "Bacon & tomato",
        "category": "Toasties On Sourdough",
        "price": 8.5,
        "description": "Toasties on sourdough",
    },
    {
        "name": "Bacon & egg",
        "category": "Toasties On Sourdough",
        "price": 8.5,
        "description": "Toasties on sourdough",
    },
    {
        "name": "BLT (bacon, lettuce & tomato)",
        "category": "Toasties On Sourdough",
        "price": 11,
        "description": "Toasties on sourdough",
    },
    {
        "name": "FRIES",
        "category": "Fries",
        "price": 7.5,
        "description": "Served w/ aioli",
    },
    {
        "name": "Quiche w/ relish",
        "category": "House Made Pastries",
        "price": 7.0,
        "description": "Served w/ aioli",
    },
    {
        "name": "Savoury muffin",
        "category": "House Made Pastries",
        "price": 6.0,
        "description": "Served w/ aioli",
    },
    {
        "name": "Chicken, beef & pork or vegan sausage roll",
        "category": "House Made Pastries",
        "price": 7,
        "description": "Served w/ aioli",
    },
    {
        "name": "Lamington",
        "category": "CAKES, SLICES & SWEETS",
        "price": custom_round_price(random.randint(4, 14)),
        "description": "House made assortment available from display - Aussie classic sponge cake dipped in chocolate and rolled in coconut",
    },
    {
        "name": "Pavlova",
        "category": "CAKES, SLICES & SWEETS",
        "price": custom_round_price(random.randint(4, 14)),
        "description": "House made assortment available from display - Crisp meringue base topped with fresh fruit and whipped cream",
    },
    {
        "name": "Anzac Biscuit",
        "category": "CAKES, SLICES & SWEETS",
        "price": custom_round_price(random.randint(4, 14)),
        "description": "House made assortment available from display - Crunchy, chewy oat cookies with a rich history",
    },
    {
        "name": "Vanilla Slice",
        "category": "CAKES, SLICES & SWEETS",
        "price": custom_round_price(random.randint(4, 14)),
        "description": "House made assortment available from display - Creamy vanilla custard between layers of flaky pastry, topped with icing",
    },
    {
        "name": "Tim Tam Cheesecake",
        "category": "CAKES, SLICES & SWEETS",
        "price": custom_round_price(random.randint(4, 14)),
        "description": "House made assortment available from display - Cheesecake with a Tim Tam biscuit base and chocolate topping",
    },
    {
        "name": "Fairy Bread",
        "category": "CAKES, SLICES & SWEETS",
        "price": custom_round_price(random.randint(4, 14)),
        "description": "House made assortment available from display - Simple yet delightful bread with butter and colorful sprinkles",
    },
    {
        "name": "Flat White",
        "category": "Beverage",
        "price": 4.0,
        "description": "A smooth, velvety milk coffee",
    },
    {
        "name": "Latte",
        "category": "Beverage",
        "price": 4.5,
        "description": "Creamy coffee with steamed milk",
    },
    {
        "name": "Cappuccino",
        "category": "Beverage",
        "price": 4.5,
        "description": "Rich coffee with a frothy top, sprinkled with cocoa",
    },
    {
        "name": "Long Black",
        "category": "Beverage",
        "price": 3.5,
        "description": "Double shot of espresso with hot water",
    },
    {
        "name": "Espresso",
        "category": "Beverage",
        "price": 3.0,
        "description": "Strong and black shot of coffee",
    },
    {
        "name": "Mocha",
        "category": "Beverage",
        "price": 5.0,
        "description": "Coffee with chocolate, topped with steamed milk and cocoa",
    },
    {
        "name": "Hot Chocolate",
        "category": "Beverage",
        "price": 4.0,
        "description": "Rich and creamy hot chocolate",
    },
    {
        "name": "Orange Juice",
        "category": "Beverage",
        "price": 5.0,
        "description": "Freshly squeezed orange juice",
    },
    {
        "name": "Apple Juice",
        "category": "Beverage",
        "price": 5.0,
        "description": "Freshly pressed apple juice",
    },
    {
        "name": "Lemonade",
        "category": "Beverage",
        "price": 3.0,
        "description": "Classic refreshing lemonade",
    },
    {
        "name": "Cola",
        "category": "Beverage",
        "price": 3.0,
        "description": "Popular carbonated cola Beverage",
    },
    {
        "name": "Sparkling Water",
        "category": "Beverage",
        "price": 3.0,
        "description": "Refreshing carbonated water",
    }
]

# Define add_on menu items with categories
add_on = [
    {"menu": "Sparkling Water", "name": "Ice", "price": 0.0},
    {"menu": "Sparkling Water", "name": "Lemon Slice", "price": 0.5},
    {"menu": "Sparkling Water", "name": "Lime Slice", "price": 0.5},
    {"menu": "Cola", "name": "Ice", "price": 0.0},
    {"menu": "Cola", "name": "Lemon Slice", "price": 0.5},
    {"menu": "Lemonade", "name": "Ice", "price": 0.0},
    {"menu": "Lemonade", "name": "Lemon Slice", "price": 0.5},
    {"menu": "Apple Juice", "name": "Ice", "price": 0.0},
    {"menu": "Orange Juice", "name": "Ice", "price": 0.0},
    {"menu": "Hot Chocolate", "name": "Whipped Cream", "price": 0.5},
    {"menu": "Hot Chocolate", "name": "Marshmallows", "price": 0.5},
    {"menu": "Mocha", "name": "Extra Shot", "price": 0.5},
    {"menu": "Mocha", "name": "Almond Milk", "price": 0.5},
    {"menu": "Mocha", "name": "Soy Milk", "price": 0.5},
    {"menu": "Mocha", "name": "Whipped Cream", "price": 0.5},
    {"menu": "Espresso", "name": "Extra Shot", "price": 0.5},
    {"menu": "Long Black", "name": "Extra Shot", "price": 0.5},
    {"menu": "Cappuccino", "name": "Extra Shot", "price": 0.5},
    {"menu": "Cappuccino", "name": "Almond Milk", "price": 0.5},
    {"menu": "Cappuccino", "name": "Soy Milk", "price": 0.5},
    {"menu": "Cappuccino", "name": "Hazelnut Syrup", "price": 0.5},
    {"menu": "Latte", "name": "Extra Shot", "price": 0.5},
    {"menu": "Latte", "name": "Almond Milk", "price": 0.5},
    {"menu": "Latte", "name": "Soy Milk", "price": 0.5},
    {"menu": "Latte", "name": "Caramel Syrup", "price": 0.5},
    {"menu": "Flat White", "name": "Extra Shot", "price": 0.5},
    {"menu": "Flat White", "name": "Almond Milk", "price": 0.5},
    {"menu": "Flat White", "name": "Soy Milk", "price": 0.5},
    {"menu": "Flat White", "name": "Vanilla Syrup", "price": 0.5},
    {"menu": "BURRITO BOWL", "name": "Chicken", "price": 4.5},
    {"menu": "AVOCADO TOAST", "name": "Free range eggs", "price": 2.5},
    {"menu": "AVOCADO TOAST", "name": "Smoked salmon", "price": 4.5},
    {"menu": "AVOCADO TOAST", "name": "Grilled halloumi", "price": 3.0},
    {"menu": "AVOCADO TOAST", "name": "Bacon", "price": 4.5},
    {"menu": "NEW YORK BAGEL BENEDICT", "name": "Bacon", "price": 3.5},
    {"menu": "NEW YORK BAGEL BENEDICT", "name": "BBQ pulled pork", "price": 3.5},
    {"menu": "NEW YORK BAGEL BENEDICT", "name": "Smoked salmon", "price": 3.5},
    {"menu": "EGGS ON TOAST", "name": "Salmon, bacon, cevapi, Chorizo", "price": 4.5},
    {"menu": "EGGS ON TOAST", "name": "Smashed avocado, hash brown, mushroom, Grilled halloumi, baked beans",
     "price": 4.0},
    {"menu": "EGGS ON TOAST", "name": "Grilled tomatoes, spinach, Feta", "price": 3.0},
    {"menu": "EGGS ON TOAST", "name": "Free range egg, ajvar. hollandaise", "price": 2.5},
    {"menu": "EGGS ON TOAST", "name": "Gluten free bread", "price": 1.5},
    {"menu": "EGGS ON TOAST", "name": "Toast, curd", "price": 1},
    {"menu": "HUEVOS (SPANISH BAKED EGGS)", "name": "Traditional spanish chorizo", "price": 4.5},
    {"menu": "Hot Chocolate", "name": "Whipped Cream", "price": 0.5},
    {"menu": "Hot Chocolate", "name": "Marshmallows", "price": 0.5}
]

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


# Define a function to generate a sales history with UUIDs
def generate_restaurants_sale_history(num=3000, month=1, time=1):
    num = num * time
    month = month * time

    sales_history = []
    start_date = datetime.now() - timedelta(days=30 * month)

    beverage_items = [item for item in menus if item["category"] == "Beverage"]
    other_items = [item for item in menus if item["category"] != "Beverage"]

    for _ in tqdm(range(num), desc="Generating sales history"):
        while True:
            sale_time = start_date + timedelta(minutes=random.randint(0, 30 * 24 * 60 * month))
            if is_open(sale_time):
                break

        if random.random() < 0.4:  # 40% chance to select a beverage
            menu_item = random.choice(beverage_items)
        else:
            menu_item = random.choice(other_items)

        add_ons = [ao for ao in add_on if ao["menu"] == menu_item["name"]]
        selected_add_ons = []
        if add_ons and random.random() < 0.2:  # 20% chance to select add-ons
            selected_add_ons = random.sample(add_ons, k=random.randint(1, len(add_ons)))

        sales_history.append({
            "uuid": str(uuid.uuid4()),
            "date_time": sale_time,
            "menu_item": menu_item["name"],
            "add_ons": [ao["name"] for ao in selected_add_ons],
        })

    return sales_history
