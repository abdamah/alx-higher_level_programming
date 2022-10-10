#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists."""
    new_list = []
    for index in range(list_length):
        try:
            div = my_list_1[index] / my_list_2[index]
        except (ValueError, TypeError):
            print("wrong type")
            div = 0
        except (ZeroDivisionError):
            print("division by 0")
            div = 0
        except (IndexError):
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
