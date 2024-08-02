import csv

def read_csv_file(file_name):
    """
    Reads a CSV file and displays its contents.

    Args:
        file_name (str): The name of the CSV file to read.

    Returns:
        None
    """
    try:
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


read_csv_file('addy_test.csv')

"""
['1', '2']
['2', '3']
['3', '4']
['4', '32']
['5', '5']
['6', '44']
['8', '3']
['8', '2']
['9', '1']
['10', '6']
"""
