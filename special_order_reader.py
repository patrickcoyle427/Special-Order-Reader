#!/usr/bin/python3

'''
special_order_reader.py - Takes a .CSV file from lightspeed retail and breaks
down total number of preorders by item and then by store
'''

import csv, os

# csv - used for reading the special orders from lightspeed retail
# os - used for finding the csv file to be read

#TO DO
# Let you choose a file if multiple CSV files are found
# Let the user only choose between lightspeed special order CSV files somehow
# export findings to CSV

def start_read():

    found_names = find_csv_names()
    choice = choose_csv(found_names)
    orders = retrieve_orders(choice)
    show_order_totals(orders)

def find_csv_names():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    # finds the directory that this script is in

    return [file for file in os.listdir(dir_path) if file.endswith('.csv')]

def choose_csv(found_names):

    if len(found_names) > 1:

        print('Make sure there is only one .csv. Will make this work better later.')

        print(found_names)
        
        exit()

    else:

        return found_names[0]

def retrieve_orders(csv_name):

    counts = {}

    with open(csv_name, newline='') as csvfile:

        reader = csv.reader(csvfile)

        # Relevant CSV Headers
        # 'Description' [1] - Product Name
        # 'Qty' [2] - amount of product on order

        next(reader)

        #data = list(reader)

        for row in reader:

            prod_name = row[1]
            qty_ordered = int(row[2])

            if prod_name in counts:

                counts[prod_name] += qty_ordered

            else:

                counts[prod_name] = qty_ordered

    return counts

def show_order_totals(orders):

    for product in orders.keys():

        qty = orders[product]

        print(f'{product}: {qty}')

if __name__ == '__main__':
    
    start_read()
