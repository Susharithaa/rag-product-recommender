# import json
# import random

# # Categories to make dataset more realistic
# categories = [
#     "Laptop",
#     "Smartphone",
#     "Headphones",
#     "Shoes",
#     "Backpack",
#     "Watch",
#     "Keyboard",
#     "Mouse",
#     "Camera",
#     "Speaker"
# ]

# brands = [
#     "TechPro",
#     "UltraGear",
#     "NextGen",
#     "SmartWave",
#     "PrimeTech",
#     "Nova",
#     "EliteGear",
#     "PowerX",
#     "VisionTech",
#     "SpeedPro"
# ]

# descriptions = [
#     "High quality product for everyday use",
#     "Designed for performance and durability",
#     "Lightweight and comfortable",
#     "Best choice for professionals",
#     "Affordable and reliable",
#     "Premium design with modern features",
#     "Perfect for travel and daily work",
#     "High performance and stylish design",
#     "Engineered for maximum productivity",
#     "Built with advanced technology"
# ]


# products = []

# for i in range(1, 101):

#     category = random.choice(categories)
#     brand = random.choice(brands)
#     description = random.choice(descriptions)

#     product = {
#         "id": i,
#         "name": f"{brand} {category} {i}",
#         "category": category,
#         "brand": brand,
#         "price": random.randint(20, 2000),
#         "description": description
#     }

#     products.append(product)


# # Save dataset
# with open("products.json", "w") as f:
#     json.dump(products, f, indent=4)

# print("Dataset created successfully: products.json")