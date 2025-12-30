from app.models import FoodType, Food

# Create food types
breakfast = FoodType.objects.get_or_create(title='صبحانه')[0]
lunch = FoodType.objects.get_or_create(title='ناهار')[0]
drink = FoodType.objects.get_or_create(title='نوشیدنی')[0]

# Create some foods
food1 = Food.objects.get_or_create(
    name='املت',
    description='املت ساده',
    price=50000,
    defaults={'image': None}
)[0]
food1.food_types.add(breakfast)

food2 = Food.objects.get_or_create(
    name='چلو کباب',
    description='چلو کباب مخصوص',
    price=150000,
    defaults={'image': None}
)[0]
food2.food_types.add(lunch)

food3 = Food.objects.get_or_create(
    name='نوشابه',
    description='نوشابه گازدار',
    price=10000,
    defaults={'image': None}
)[0]
food3.food_types.add(drink)

print('Foods created')

