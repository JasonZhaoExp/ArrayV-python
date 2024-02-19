# Adding algorithms

## Writing sorting algorithms
- Algorithms are stored in "%PATH_TO_PARENT_FOLDER%\sorts\ 
>
- Variable names are not taken into account, you can use any.
- You can include external functions.
- The program will only accept algorithms with the following two functions in them:

```py
def name():
    return FUNCTION_NAME
```
Replace FUNCTION_NAME with a string containing the name of the sorting algorithm. This will be used in the results file.
>
```py
def sort(LIST):
    # Insert code here
    return SORTED_LIST
```
The variables "LIST" and "SORTED_LIST" can have any name.

## Writing search algorithms
- Algorithms are stored in "%PATH_TO_PARENT_FOLDER%\searches\"
>
- Variable names are not taken into account, you can use any.
- You can include external functions.
- The program will only accept algorithms with the following two functions in them:

```py
def name():
    return FUNCTION_NAME
```
Replace FUNCTION_NAME with a string containing the name of the sorting algorithm. This will be used in the results file.
>
```py
def search(LIST, SEARCHING_FOR):
    # Insert code here
    
    # If SEARCHING_FOR is found:
        return INDEX_OF_SEARCHING_FOR
    # If SEARCHING_FOR is not found:
        return False
```
The variables "LIST", "SEARCHING_FOR" and "INDEX_OF_SEARCHING_FOR" can have any name.