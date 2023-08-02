import numpy as np

'''
No other imports allowed
All functions must be implemented in one line.

This is a numpy assignment so make sure all of your arrays are numpy arrays!
Arrays look like lists, except all elements in the array share the same data type.
To demonstrate creating and accessing an array:
>>> a = np.array([[1,2,3],
				  [4,5,6]])
>>> print(a[0])
[1 2 3]     # there are no commas because this is an array, not a list
'''

def replenishment(maximum_capacity, curr_inventory, purchase_quantity):
	"""
A grocery store replenishes its stock every weekend. Every time it purchases the
same amount of goods. Given its inventory in the current week(i), maximum store
capacity(c), and the number of goods to replenish(n) per week, return an array
that contains the store's inventory in the upcoming weeks until the store reaches
the maximum capacity.
Note: Every time the store must either replenish the full amount(n) of goods or
replenish 0 goods. For example, if c = 100, n = 15, i = 90, the store should
import 0 goods in the next week.

Args:
  maximum_capacity (int): The maximum amount of goods in the store
  curr_inventory (int): Current amount of goods in the store
  purchase_quantity (int or float): The replenishment every week.
Returns:
  np.array of inventory groups, from inventory of the current week to the week
  before reaching the maximum capacity.
>>> arr = replenishment(100, 40, 15)
array([ 40  55  70  85 100])
	"""
	return np.arange(curr_inventory, maximum_capacity + purchase_quantity, purchase_quantity)

def drop(revenue):
	"""
The manager of the grocery store wants to calculate the profitability for each
product in the past 5 weeks. Given a sorted array of revenues, return an array
of all the revenues EXCEPT the week of minimum and maximum of the revenue,
which will be dropped.
Note: As the example below, each row of the array has been sorted. For example,
for good 1, the lowest revenue in the past 5 weeks was 32 and the highest was 103.
You don't need to sort the array yourself.

Args:
  revenue (array) : array representing all goods' revenues. Each row
  represents a type of good and each column represents a week.

Returns:
  np.array of sliced revenues

>>> revenue = array([[32, 70, 71, 89, 103]
					[70, 87, 93, 94, 99]
					[76, 78, 92, 98, 117]] )
>>> result = drop(revenue)
array ([[70 71 89]
		[87 93 94]
		[78 92 98]])

	"""
	return revenue[0:3,1:-1] 

def final_price(price_matrix, sales_tax):
	"""
You are doing your weekly grocery shopping, and you want to use a numpy array to calculate the final
values of each item you purchase. Given a numpy array containing both origninal sales price and amount that
that item is discounted by, calculate the final price for each grocery item by subtracting the discount amount from
the sales price, and then add the tax on top of that.


Args:
price_matrix (array): array where first row is original sales price of the item and
the second row is the amount taken off of each grocery item. You can assume
there will always only be two rows in price_matrix.

Returns:
np.array of final price: the original price with the discount factored in and the sales tax added

>>>price_matrix = array([[8.00, 5.00, 3.00, 13.00]
						[1.00, 2.00, 0.50, 3.50]])
>>>sales_tax = .06

>>> final_price(price_matrix, sales_tax)
array([ 7.42  3.18  2.65 10.07 ])
	"""
	return (price_matrix[0] - price_matrix[1])*(1+sales_tax)

def broke_student(cart, item_budget):
	"""
Uh-oh! After scoring 17.5% on your 4th exam of the week, you find yourself starving,
and your stock of snacks is running low. Famished, you find yourself crawling to
the local Publix grocery store in Midtown to purchase some food. As you are waiting
in the checkout line, you realized that you are not able to afford all of the food
you picked out due to you being a broke college student. Thus, you must decide which
items you should end up keeping.

Given a 1-D array of floats representing item prices, use array masking to return
a new array that only includes item prices that are less than or equal to your
`item_budget` and is not equal to the score you received on your last exam, which is a 17.5.


Args:
cart (array): array consisting of floats representing item prices
item_budget (float): float that represents your current budget for each item

Returns:
np.array of the updated cart: should include item prices below or equal your
item budget and should not equal your exam grade of an 17.5

>>> cart = array([11.99, 15.5, 7.75, 20.49, 17.5, 27.79, 26.25])
>>> broke_student(cart, 20.5)
array([11.99  15.5  7.75  20.49])
	"""


def bulk_szn(labels):
	"""
You have decided to bulk. Your protein intake is your #1 priority in life,
thus you want to calculate your protein macros for the day. In order to do so,
you must translate the string protein label on the items in your cart to a corresponding number in grams.
You want to convert 'High' to 32.0, 'Mid' will be displayed as a 15.0, 'Low' will be displayed as a 8.0, and
everything below a 'Insufficient' is displayed as a 0.0.

Args:
protein (array): array of all the protein labels for each of the items in your cart

Returns:
np.array of the grams: the protein labels converted to grams from the string label
to the numeric (as a float) grams.

>>> labels = np.array(['High' 'High' 'Low' 'Insufficient' 'Mid' 'High'])
>>> bulk_szn(labels)
array([32. 32.  8.  0. 15. 32.])
	"""
	return np.where(labels=="High",32.0,np.where(labels=="Mid",15.0,np.where(labels=="Low",8.0,0)))


if __name__ == '__main__':
	#### Question 1##################################
	#print(replenishment(100, 40, 15))

	#### Question 2##################################
	revenue = np.array([[32, 70, 71, 89, 103],[70, 87, 93, 94, 99],[76, 78, 92, 98, 117]])
	print(drop(revenue))

	#### Question 3###################################
	price_matrix = np.array([[8.00, 5.00, 3.00, 13.00],[1.00, 2.00, 0.50, 3.50]])
	sales_tax = .06
	#print(final_price(price_matrix, sales_tax))

	#### Question 4##################################
	cart = np.array([11.99, 15.5, 7.75, 20.49, 17.5, 27.79, 26.25])
	#print(broke_student(cart, 20.5))

	#### Question 5#################################
	labels = np.array(['High','High','Low','Insufficient','Mid','High'])
	#print(bulk_szn(labels))
