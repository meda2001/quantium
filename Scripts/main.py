import csv
import re

# List of input CSV filenames
input_files = ['C:/Users/medam/Desktop/quantium/quantium/data/daily_sales_data_0.csv', 'C:/Users/medam/Desktop/quantium/quantium/data/daily_sales_data_1.csv', 'C:/Users/medam/Desktop/quantium/quantium/data/daily_sales_data_2.csv']





# Output CSV filename
output_file = 'formatted_merged_output.csv'

# Open the output CSV file in write mode
with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Write the header row to the output file
    writer.writerow(["Sales", "Date", "Region"])

    # Loop through input files and copy data to the output file, calculating "Sales"
    for input_file in input_files:
        with open(input_file, 'r') as infile:
            reader = csv.reader(infile)
            next(reader)  # Skip the header row in input files
            for row in reader:
                product = row[0]

                # Check if the "product" column is not "pink morsel"
                if product != "pink morsel":
                    continue

                quantity = int(row[2])

                # Remove non-numeric characters and convert "price" to a float
                price_str = re.sub(r'[^\d.]', '', row[1])
                price = float(price_str)

                date = row[3]
                region = row[4]

                # Calculate "Sales" by multiplying "quantity" and "price"
                sales = quantity * price

                # Write "Sales," "Date," and "Region" to the output file
                writer.writerow([sales, date, region])

print(f'Formatted and merged CSV file saved as {output_file}')








# # Output CSV filename
# output_file = 'formatted_merged_output.csv'

# # Open the output CSV file in write mode
# with open(output_file, 'w', newline='') as outfile:
#     writer = csv.writer(outfile)

#     # Write the header row to the output file
#     writer.writerow(["Sales", "Date", "Region"])

#     # Loop through input files and copy data to the output file, calculating "Sales"
#     for input_file in input_files:
#         with open(input_file, 'r') as infile:
#             reader = csv.reader(infile)
#             next(reader)  # Skip the header row in input files
#             for row in reader:
#                 product = row[0]
#                 quantity = int(row[2])

#                 # Remove non-numeric characters and convert "price" to a float
#                 price_str = re.sub(r'[^\d.]', '', row[1])
#                 price = float(price_str)

#                 date = row[3]
#                 region = row[4]

#                 # Calculate "Sales" by multiplying "quantity" and "price"
#                 sales = quantity * price

#                 # Write "Sales," "Date," and "Region" to the output file
#                 writer.writerow([sales, date, region])

# print(f'Formatted and merged CSV file saved as {output_file}')






# # Output CSV filename
# output_file = 'merged.csv'

# # Open the output CSV file in write mode
# with open(output_file, 'w', newline='') as outfile:
#     writer = csv.writer(outfile)

#     # Write headers to the output file
#     with open(input_files[0], 'r') as infile:
#         reader = csv.reader(infile)
#         headers = next(reader)
#         writer.writerow(headers)

#     # Loop through input files and copy data (excluding headers) to the output file
#     for input_file in input_files:
#         with open(input_file, 'r') as infile:
#             reader = csv.reader(infile)
#             next(reader)  # Skip the header row in input files
#             for row in reader:
#                 writer.writerow(row)

# print(f'Merged CSV file saved as {output_file}')


# # Input CSV filename
# input_file = 'merged.csv'

# # Output CSV filename
# output_file = 'filtered_merged.csv'

# # Open the input and output CSV files
# with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)

#     # Write the header row to the output file
#     headers = next(reader)
#     writer.writerow(headers)

#     # Loop through the rows in the input file and copy to the output file
#     for row in reader:
#         if row[0] != "pink morsel":  # Check if the "product" column is not "pink morsel"
#             writer.writerow(row)

# print(f'Filtered CSV file saved as {output_file}')



# # Input CSV filename
# input_file = 'filtered_merged.csv'

# # Output CSV filename
# output_file = 'filtered_merged_with_sales.csv'

# # Open the input and output CSV files
# with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)

#     # Write the header row to the output file with the "sales" column
#     headers = next(reader)
#     headers.append("sales")
#     writer.writerow(headers)

#     # Loop through the rows in the input file, calculate "sales," and copy to the output file
#     for row in reader:
#         product = row[0]
#         quantity = int(row[2])
#         price = float(row[1])
#         date = row[3]
#         region = row[4]

#         # Calculate the "sales" column by multiplying "quantity" and "price"
#         sales = quantity * price

#         # Append the "sales" value to the row and write it to the output file
#         row.append(sales)
#         writer.writerow(row)

# print(f'Filtered CSV file with "sales" column saved as {output_file}')


# # Output CSV filename
# output_file = 'formatted_merged_output.csv'

# # Open the output CSV file in write mode
# with open(output_file, 'w', newline='') as outfile:
#     writer = csv.writer(outfile)

#     # Write the header row to the output file
#     writer.writerow(["Sales", "Date", "Region"])

#     # Loop through input files and copy data to the output file, calculating "Sales"
#     for input_file in input_files:
#         with open(input_file, 'r') as infile:
#             reader = csv.reader(infile)
#             next(reader)  # Skip the header row in input files
#             for row in reader:
#                 product = row[0]
#                 quantity = int(row[2])
#                 price = float(row[1])
#                 date = row[3]
#                 region = row[4]

#                 # Calculate "Sales" by multiplying "quantity" and "price"
#                 sales = quantity * price

#                 # Write "Sales," "Date," and "Region" to the output file
#                 writer.writerow([sales, date, region])

# print(f'Formatted and merged CSV file saved as {output_file}')