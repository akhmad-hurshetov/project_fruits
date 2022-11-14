def get_cheapest_fruit(data):
    """
    This function returns the name of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    f=open('fruits.csv')
    s=f.read()
    sum=0
    for i in s:
        if i==i.isdigit():
            sum+=int(i)
    pass sum