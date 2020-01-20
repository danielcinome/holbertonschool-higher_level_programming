# Python - Inheritance


# Files

#### 0-lookup.py
	unction that returns the list of available attributes and methods of an object:

-   Prototype:  `def lookup(obj):`
-   Returns a  `list`  object
#### 1-my_list.py, tests/1-my_list.txt
	lass  `MyList`  that inherits from  `list`:

-   Public instance method:  `def print_sorted(self):`  that prints the list, but sorted (ascending sort)
#### 2-is_same_class.py
	function that returns `True` if the object is _exactly_ an instance of the specified class ; otherwise `False`.
#### 3-is_kind_of_class.py
	function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.
###  4-inherits_from.py
	function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.
#### 5-base_geometry.py
	an empty class `BaseGeometry`.
#### 6-base_geometry.py
	class  `BaseGeometry`  (based on  `5-base_geometry.py`).

-   Public instance method:  `def area(self):`  that raises an  `Exception`  with the message  `area() is not implemented`
#### 7-base_geometry.py, tests/7-base_geometry.txt
	class  `BaseGeometry`  (based on  `6-base_geometry.py`).
#### 8-rectangle.py
	class  `Rectangle`  that inherits from  `BaseGeometry`  (`7-base_geometry.py`).
	-   `width`  and  `height`  must be private. No getter or setter
-   `width`  and  `height`  must be positive integers, validated by  `integer_validator`
#### 9-rectangle.py
	class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)
#### 10-square.py
	class  `Square`  that inherits from  `Rectangle`  (`9-rectangle.py`):

-   Instantiation with  `size`:  `def __init__(self, size):`:
    -   `size`  must be private. No getter or setter
    -   `size`  must be a positive integer, validated by  `integer_validator`
-   the  `area()`  method must be implemented
#### 11-square.py
	class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).
	-   Instantiation with  `size`:  `def __init__(self, size):`:
    -   `size`  must be private. No getter or setter
    -   `size`  must be a positive integer, validated by  `integer_validator`
-   the  `area()`  method must be implemented
