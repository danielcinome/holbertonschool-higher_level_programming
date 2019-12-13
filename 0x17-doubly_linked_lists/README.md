# C - Doubly linked lists

```
/**
 * struct dlistint_s - doubly linked list
 * @n: integer
 * @prev: points to the previous node
 * @next: points to the next node
 *
 * Description: doubly linked list node structure
 * for Holberton project
 */
typedef struct dlistint_s
{
    int n;
    struct dlistint_s *prev;
    struct dlistint_s *next;
} dlistint_t;
```

# Files

### 0. Print list
	function that prints all the elements of a `dlistint_t` list.
### 1. List length
	function that returns the number of elements in a linked `dlistint_t` list.
#### 2. Add node
	function that adds a new node at the beginning of a `dlistint_t` list.
#### 3. Add node at the end
	function that adds a new node at the end of a `dlistint_t` list.
#### 4. Free list
	function that free a `dlistint_t` list.
#### 5. Get node at index
	function that returns the nth node of a `dlistint_t` linked list.
