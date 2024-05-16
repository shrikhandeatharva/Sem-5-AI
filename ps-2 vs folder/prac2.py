import requests
import pandas as pd

# Function to read data from a URL
def read_data_from_web(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve data from {url}")
        return None

# Function to read data from a file (both .txt and .csv supported)
def read_data_from_file(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r') as txt_file:
            return txt_file.read()
    elif file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    else:
        print(f"Unsupported file format: {file_path}")
        return None

# Function to write data to a file
def write_data_to_file(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        output_file.write(data)


# Example usage
web_url = "https://example-files.online-convert.com/document/txt/example.txt"
local_file_path = "cars1.csv"
output_path = "Note.txt"

# Read data from web
web_data = read_data_from_web(web_url)

# Read data from local file
local_data = read_data_from_file(local_file_path)

# Combine or process the data as needed
combined_data = f"{web_data}\n\n{local_data}"

# Write the combined data to a new file
write_data_to_file(combined_data, output_path)

print(f"Combined data written to: {output_path}")



import pandas
df = pandas.read_excel('D:\\GCOEN SEM 6\\PS-2 LAB\\files\\cars.xlsx', nrows=10)
print("Contents of excel sheet : ")
print(df)
