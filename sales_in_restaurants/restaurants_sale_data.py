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
        "add-on": []
    },
    {
        "name": "BREAKFAST BURGER",
        "category": "All day breakfast",
        "price": 16.00,
        "description": "Cevapi sausage, swiss cheese, spinach, relish, mayo, fried egg, bacon on brioche bun served w/ hash brown",
        "add-on": []
    },
    {
        "name": "AVOCADO TOAST",
        "category": "All day breakfast",
        "price": 16.00,
        "description": "Seeded toast w/ mixed seeds, marinated feta, dukkah, saffron infused hummus & crispy kale (V.VeO, GFO)",
        "add-on": [
            {
                "name": "Free range eggs",
                "price": 2.5
            },
            {
                "name": "Smoked salmon",
                "price": 4.5
            },
            {
                "name": "Grilled halloumi",
                "price": 3.0
            },
            {
                "name": "Bacon",
                "price": 4.5
            }
        ]
    },
    {
        "name": "COCONUT & CHIA PUDDING",
        "category": "All day breakfast",
        "price": 17.50,
        "description": "House made almond granola, berry compote served w/ seasonal fruit (V, Ve)",
        "add-on": []
    },
    {
        "name": "CHILLI SCRAMBLE",
        "category": "All day breakfast",
        "price": 18.00,
        "description": "Asparagus, crispy shallots, fresh chilli, parsley, feta & sambol oelek w/toast w/ toast (V, GFO)",
        "add-on": []
    },
    {
        "name": "EGG, BACON & CHEESE TOASTIE",
        "category": "All day breakfast",
        "price": 10.5,
        "description": "Sourdough, fried egg, house made relish, cheese & bacon (GFO)",
        "add-on": []
    },
    {
        "name": "HUEVOS (SPANISH BAKED EGGS)",
        "category": "All day breakfast",
        "price": 16.5,
        "description": "Bell pepper, tomato, onion, spices & pecorino cheese w/ seeded toast (V, GFO)",
        "add-on": [
            {
                "name": "Traditional spanish chorizo",
                "price": 4.5
            }
        ]
    },
    {
        "name": "EGGS ON TOAST",
        "category": "All day breakfast",
        "price": 9.5,
        "description": "Free range - poached, scrambled or fried (V. GFO)",
        "add-on": [
            {
                "name": "Salmon, bacon, cevapi, Chorizo",
                "price": 4.5
            },
            {
                "name": "Smashed avocado, hash brown, mushroom, Grilled halloumi, baked beans",
                "p,rice": 4.0
            },
            {
                "name": "Grilled tomatoes, spinach, Feta",
                "price": 3.0
            },
            {
                "name": "Free range egg, ajvar. hollandaise",
                "price": 2.5
            },
            {
                "name": "Gluten free bread",
                "price": 1.5
            },
            {
                "name": "Toast, curd",
                "price": 1
            }
        ]
    },
    {
        "name": "TOAST",
        "category": "All day breakfast",
        "price": 7.00,
        "description": "Sourdough or seeded toast w/ choice of butter/jam/peanut butter/Vegemite\n(V. Ve, GFO)",
        "add-on": []
    },
    {
        "name": "FRUIT TOAST",
        "category": "All day breakfast",
        "price": 7.50,
        "description": "Raisins, apricots, prunes w/ citrus curd (V)",
        "add-on": []
    },
    {
        "name": "NEW YORK BAGEL BENEDICT",
        "category": "All day breakfast",
        "price": 13.00,
        "description": "Toasted bagel topped w/ wilted spinach. poached eggs & house made hollandaise sauce (V. GFO)",
        "add-on": [
            {
                "name": "Bacon",
                "price": 3.5
            },
            {
                "name": "BBQ pulled pork",
                "price": 3.5
            },
            {
                "name": "Smoked salmon",
                "price": 3.5
            }
        ]
    },
    {
        "name": "BURRITO BOWL",
        "category": "All day lunch",
        "price": 18.5,
        "description": "Lime brown rice, avocado, purple cabbage. chargrilled corn, spiced black beans, pickled capsicum, spinach, tortilla chips (V, Ve, GFO)",
        "add-on": [
            {
                "name": "Chicken",
                "price": 4.5
            }
        ]
    },
    {
        "name": "SOFT SHELL TORTILLAS",
        "category": "All day lunch",
        "price": 18.5,
        "description": "Spicy crispy chicken, avocado, chilli & corn salsa, chipotle aioli, slaw in soft shell tortillas\n(V, VeO)",
        "add-on": []
    },
    {
        "name": "OPEN LAMB SOUVLAKI",
        "category": "All day lunch",
        "price": 18.5,
        "description": "8 hour slow cooked lamb. pita bread, Greek salad, tzatziki w/ fries",
        "add-on": []
    },
    {
        "name": "WINIFRED WAGYU BURGER",
        "category": "All day lunch",
        "price": 18.5,
        "description": "House made 130g grilled wagyu beef patty, cheddar, lettuce, tomato, pickle, Winifred special sauce on brioche bun w/ side of fries (GFO)",
        "add-on": []
    },
    {
        "name": "TEXAN COUSIN BURGER",
        "category": "All day lunch",
        "price": 18.5,
        "description": "Southern style spiced chicken, lettuce, apple slaw, tomato, swiss cheese, pickled mayo on brioche bun w/ side of fries (GFO)",
        "add-on": []
    },
    {
        "name": "VEGAN SWISS BROWN MUSHROOM BURGER",
        "category": "All day lunch",
        "price": 18.0,
        "description": "Crispy porcini mushroom patty, pickled red capsicum, lettuce, tomato, onion relish on sourdough bun w/ side of fries (V. Ve. (GFO)",
        "add-on": []
    },
    {
        "name": "Cheese & tomato",
        "category": "Toasties On Sourdough",
        "price": 7,
        "description": "Toasties on sourdough",
        "add-on": []
    },
    {
        "name": "Chicken, avocado, lettuce & aioli",
        "category": "Toasties On Sourdough",
        "price": 11.5,
        "description": "Toasties on sourdough",
        "add-on": []
    },
    {
        "name": "Ham & cheese",
        "category": "Toasties On Sourdough",
        "price": 7,
        "description": "Toasties on sourdough",
        "add-on": []
    },
    {
        "name": "Ham, cheese & tomato",
        "category": "Toasties On Sourdough",
        "price": 7.5,
        "description": "Toasties on sourdough",
        "add-on": []
    },
    {
        "name": "Mushroom & cheese",
        "category": "Toasties On Sourdough",
        "price": 8.5,
        "description": "Toasties on sourdough",
        "add-on": []
    },
    {
        "name": "Avocado & cheese",
        "category": "Toasties On Sourdough",
        "price": 9,
        "description": "Toasties on sourdough",
        "add-on": []
    },
    {
        "name": "Bacon & tomato",
        "category": "Toasties On Sourdough",
        "price": 8.5,
        "description": "Toasties on sourdough",
        "add-on": []
    },
    {
        "name": "Bacon & egg",
        "category": "Toasties On Sourdough",
        "price": 8.5,
        "description": "Toasties on sourdough",
        "add-on": []
    },
    {
        "name": "BLT (bacon, lettuce & tomato)",
        "category": "Toasties On Sourdough",
        "price": 11,
        "description": "Toasties on sourdough",
        "add-on": []
    },
    {
        "name": "FRIES",
        "category": "Fries",
        "price": 7.5,
        "description": "Served w/ aioli",
        "add-on": []
    },
    {
        "name": "Quiche w/ relish",
        "category": "House Made Pastries",
        "price": 7.0,
        "description": "Served w/ aioli",
        "add-on": []
    },
    {
        "name": "Savoury muffin",
        "category": "House Made Pastries",
        "price": 6.0,
        "description": "Served w/ aioli",
        "add-on": []
    },
    {
        "name": "Chicken, beef & pork or vegan sausage roll",
        "category": "House Made Pastries",
        "price": 7,
        "description": "Served w/ aioli",
        "add-on": []
    },
    {
        "name": "Lamington",
        "category": "CAKES, SLICES & SWEETS",
        "price": custom_round_price(random.randint(4, 14)),
        "description": "House made assortment available from display - Aussie classic sponge cake dipped in chocolate and rolled in coconut",
        "add-on": []
    },
    {
        "name": "Pavlova",
        "category": "CAKES, SLICES & SWEETS",
        "price": custom_round_price(random.randint(4, 14)),
        "description": "House made assortment available from display - Crisp meringue base topped with fresh fruit and whipped cream",
        "add-on": []
    },
    {
        "name": "Anzac Biscuit",
        "category": "CAKES, SLICES & SWEETS",
        "price": custom_round_price(random.randint(4, 14)),
        "description": "House made assortment available from display - Crunchy, chewy oat cookies with a rich history",
        "add-on": []
    },
    {
        "name": "Vanilla Slice",
        "category": "CAKES, SLICES & SWEETS",
        "price": custom_round_price(random.randint(4, 14)),
        "description": "House made assortment available from display - Creamy vanilla custard between layers of flaky pastry, topped with icing",
        "add-on": []
    },
    {
        "name": "Tim Tam Cheesecake",
        "category": "CAKES, SLICES & SWEETS",
        "price": custom_round_price(random.randint(4, 14)),
        "description": "House made assortment available from display - Cheesecake with a Tim Tam biscuit base and chocolate topping",
        "add-on": []
    },
    {
        "name": "Fairy Bread",
        "category": "CAKES, SLICES & SWEETS",
        "price": custom_round_price(random.randint(4, 14)),
        "description": "House made assortment available from display - Simple yet delightful bread with butter and colorful sprinkles",
        "add-on": []
    },
    {
        "name": "Flat White",
        "category": "Beverage",
        "price": 4.0,
        "description": "A smooth, velvety milk coffee",
        "add-on": [
            {"name": "Extra Shot", "price": 0.5},
            {"name": "Almond Milk", "price": 0.5},
            {"name": "Soy Milk", "price": 0.5},
            {"name": "Vanilla Syrup", "price": 0.5}
        ]
    },
    {
        "name": "Latte",
        "category": "Beverage",
        "price": 4.5,
        "description": "Creamy coffee with steamed milk",
        "add-on": [
            {"name": "Extra Shot", "price": 0.5},
            {"name": "Almond Milk", "price": 0.5},
            {"name": "Soy Milk", "price": 0.5},
            {"name": "Caramel Syrup", "price": 0.5}
        ]
    },
    {
        "name": "Cappuccino",
        "category": "Beverage",
        "price": 4.5,
        "description": "Rich coffee with a frothy top, sprinkled with cocoa",
        "add-on": [
            {"name": "Extra Shot", "price": 0.5},
            {"name": "Almond Milk", "price": 0.5},
            {"name": "Soy Milk", "price": 0.5},
            {"name": "Hazelnut Syrup", "price": 0.5}
        ]
    },
    {
        "name": "Long Black",
        "category": "Beverage",
        "price": 3.5,
        "description": "Double shot of espresso with hot water",
        "add-on": [
            {"name": "Extra Shot", "price": 0.5}
        ]
    },
    {
        "name": "Espresso",
        "category": "Beverage",
        "price": 3.0,
        "description": "Strong and black shot of coffee",
        "add-on": [
            {"name": "Extra Shot", "price": 0.5}
        ]
    },
    {
        "name": "Mocha",
        "category": "Beverage",
        "price": 5.0,
        "description": "Coffee with chocolate, topped with steamed milk and cocoa",
        "add-on": [
            {"name": "Extra Shot", "price": 0.5},
            {"name": "Almond Milk", "price": 0.5},
            {"name": "Soy Milk", "price": 0.5},
            {"name": "Whipped Cream", "price": 0.5}
        ]
    },
    {
        "name": "Hot Chocolate",
        "category": "Beverage",
        "price": 4.0,
        "description": "Rich and creamy hot chocolate",
        "add-on": [
            {"name": "Whipped Cream", "price": 0.5},
            {"name": "Marshmallows", "price": 0.5}
        ]
    },
    {
        "name": "Orange Juice",
        "category": "Beverage",
        "price": 5.0,
        "description": "Freshly squeezed orange juice",
        "add-on": [
            {"name": "Ice", "price": 0.0}
        ]
    },
    {
        "name": "Apple Juice",
        "category": "Beverage",
        "price": 5.0,
        "description": "Freshly pressed apple juice",
        "add-on": [
            {"name": "Ice", "price": 0.0}
        ]
    },
    {
        "name": "Lemonade",
        "category": "Beverage",
        "price": 3.0,
        "description": "Classic refreshing lemonade",
        "add-on": [
            {"name": "Ice", "price": 0.0},
            {"name": "Lemon Slice", "price": 0.5}
        ]
    },
    {
        "name": "Cola",
        "category": "Beverage",
        "price": 3.0,
        "description": "Popular carbonated cola Beverage",
        "add-on": [
            {"name": "Ice", "price": 0.0},
            {"name": "Lemon Slice", "price": 0.5}
        ]
    },
    {
        "name": "Sparkling Water",
        "category": "Beverage",
        "price": 3.0,
        "description": "Refreshing carbonated water",
        "add-on": [
            {"name": "Ice", "price": 0.0},
            {"name": "Lemon Slice", "price": 0.5},
            {"name": "Lime Slice", "price": 0.5}
        ]
    }
]

# Define a DynamicProvider for menus
menus_provider = DynamicProvider(
    provider_name="menus",
    elements=menus
)

# Add the custom provider to Faker
fake.add_provider(menus_provider)


# Define a function to generate a random menu with UUIDs
def generate_restaurants_menu(num_items=10):
    """
    Generate a list of menu items with UUIDs.
    Args:
    num_items: Number of menu items to generate.
    """
    menu_items = []
    for _ in tqdm(range(num_items), desc="Generating menu items"):
        fake_menu = fake.menus()
        # item_name = fake.word().capitalize()
        # base_price = round(random.uniform(5.0, 20.0), 2)
        # add_ons = [
        #     {"name": fake.word().capitalize(), "price": round(random.uniform(0.5, 5.0), 2)}
        #     for _ in range(random.randint(0, 3))
        # ]
        menu_items.append({
            "uuid": str(uuid.uuid4()),
            "name": fake_menu["name"],
            "category": fake_menu["category"],
            "description": fake_menu["description"],
            "price": fake_menu["price"],
            "add-on": fake_menu["add-on"]
        })
    return menu_items


def generate_restaurants_menu_add_on(menu_item):
    """
    Generate add-ons for a given menu item.
    80% chance of no add-ons, 20% chance of having add-ons.
    """
    add_ons = menu_item.get("add-on", [])
    if add_ons and random.random() <= 0.2:  # 20% chance to add add-ons
        num_add_ons = random.randint(1, len(add_ons))
        return random.sample(add_ons, num_add_ons)  # Ensure unique add-ons
    return []


def generate_restaurants_sale_history(num=3000, month=1, time=1):
    """
    Generate restaurant sales history.
    Args:
    num: Number of data points to generate.
    month: Number of months for which to generate data.
    time: Multiplier for both num and month.
    """
    num = num * time
    month = month * time

    sales_history = []

    current_time = datetime.now()
    start_time = current_time - timedelta(days=30 * month)

    open_hours_weekday = [(7, 14, 30), (12, 13)]
    open_hours_weekend = [(8, 14, 30), (12, 13)]

    for _ in tqdm(range(num), desc="Generating restaurant sales history"):
        # Generate a random datetime within the specified range
        sale_time = fake.date_time_between(start_date=start_time, end_date=current_time)

        # Ensure the sale is within operating hours
        if sale_time.weekday() in [1, 2, 3, 4]:  # Tuesday to Friday
            while not (7 <= sale_time.hour < 14 or (sale_time.hour == 14 and sale_time.minute <= 30)):
                sale_time = fake.date_time_between(start_date=start_time, end_date=current_time)
        else:  # Saturday to Sunday
            while not (8 <= sale_time.hour < 14 or (sale_time.hour == 14 and sale_time.minute <= 30)):
                sale_time = fake.date_time_between(start_date=start_time, end_date=current_time)

        # Select a random menu item and its price
        menu_item = fake.menus()

        # Generate add-ons
        add_ons = generate_restaurants_menu_add_on(menu_item)
        total_add_ons_price = sum(add_on.get("price", 0) for add_on in add_ons)

        # Append sale record
        sales_history.append({
            "uuid": str(uuid.uuid4()),
            "date_time": sale_time,
            "menu_item": menu_item["name"],
            "add_ons": [add_on["name"] for add_on in add_ons],
            "add_ons_price": total_add_ons_price,
        })

    return sales_history
