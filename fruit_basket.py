basket1 = {"banana", "apple", "mango", "grape", "apple"}
basket2 = {"kiwi", "kiwi", "mango", "banana"}
print("basket 1:", basket1)
print("basket 2:", basket2)

basket1.add("orange")
print("After adding orange to basket 1:", basket1)

common_fruits = basket1.intersection(basket2)
print("fruits in both baskets:", common_fruits)

import array as arr
fruit_counts = arr.array('i', [3, 5, 2, 4,])
print("fruit counts array:", fruit_counts)

fruit_counts.insert(0, 1)
fruit_counts.append(6)
print("After adding items:", fruit_counts)


count_of_4 = fruit_counts.count(4)
print("number of times 4 appears:", count_of_4)

fruit_counts.reverse()
print("reversed fruits counts array:", fruit_counts)

print("")
print("===== FRUIT BASKET SUMMARY =====")
print("Basket 1:", basket1)
print("Basket 2:", basket2)
print("Fruits in both baskets:", common_fruits)
print("Fruit counts:", fruit_counts)
print("==================================================")