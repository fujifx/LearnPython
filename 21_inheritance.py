from Chef import Chef
from ChineseChef import ChineseChef

# Inheritance is basically where we can dfine a buunch of attributes
# and functions inside a class. Then we can create another class
# and we can inherit all of those attributes. You can have one class that has
# all the functionality of another class without having to physically
# write out any of the same methods or attributes.

myChef = Chef()
myChineseChef = ChineseChef()

myChef.make_special_dish()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()