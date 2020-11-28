#!/usr/bin/python3

'''
special_order_reader.py - Takes a .CSV file from lightspeed retail and breaks
down total number of preorders by item and then by store
'''

import csv, os

# csv - used for reading the special orders from lightspeed retail
# os - used for finding the csv file to be read

#TO DO
# export findings to CSV

# Let the user choose a store from where the preorders are from OR
# choose if it's all stores instead

# print out can show counts by store

def start_read():

    found_names = find_csv_names()
    orders = retrieve_orders(found_names)
    show_order_totals(orders)

def find_csv_names():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    # finds the directory that this script is in

    return [file for file in os.listdir(dir_path) if file.endswith('.csv')]


def retrieve_orders(csv_name):

    counts = {}

    print('\nFile Status\n')

    special_order_header = ['Started', 'Description', 'Qty',
                            'Cost', 'Retail', 'Subtotal',
                            'Tax', 'Total Tax', 'Total',
                            'Margin', 'Customer', 'Employee']

    for file in csv_name:

        with open(file, newline='') as csvfile:

            reader = csv.reader(csvfile)
            
            # Relevant Special Order CSV Headers
            # 'Description' [1] - Product Name
            # 'Qty' [2] - amount of product on order

            current_header = next(reader)

            if current_header != special_order_header:

                print(f'X --> {file} is not a Lightspeed Retail Special Order CSV File\n')

            else:

                for row in reader:

                    prod_name = row[1]
                    qty_ordered = int(row[2])

                    if prod_name in counts:

                        counts[prod_name] += qty_ordered

                    else:

                        counts[prod_name] = qty_ordered

                print(f'O --> {file} successfully read.\n')

    return counts

def show_order_totals(orders):

    for product in orders.keys():

        qty = orders[product]

        print(f'{product}: {qty}')

if __name__ == '__main__':
    
    start_read()
