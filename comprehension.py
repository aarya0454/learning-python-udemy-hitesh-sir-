tea_ingredients = {
    "Masala Chai": ["black tea", "milk", "sugar", "cardamom", "cinnamon", "ginger", "cloves"],
    "Green Tea": ["green tea leaves", "water"],
    "Earl Grey": ["black tea", "bergamot oil"],
    "Chamomile Tea": ["chamomile flowers", "water"],
    "Lemon Tea": ["black tea", "lemon juice", "honey"],
    "Peppermint Tea": ["peppermint leaves", "water"],
    "Jasmine Tea": ["green tea", "jasmine flowers"],
    "Matcha": ["matcha powder", "water"],
    "Oolong Tea": ["oolong tea leaves", "water"],
    "Herbal Tea": ["herbs", "spices", "flowers", "water"]
}
unique_tea = {spice for ingredients in tea_ingredients.values() for spice in ingredients}
print(unique_tea)