import requests

# Count all the values
'''
print("====")
with open('sales_data.txt') as f:
    sales_data = list(f.readlines())
with open('sales_data.txt') as f:
    for line in len(sales_data):
        sales_arr[lines] = f.readlines()
print(sales_arr[1])
'''

with open('sales_data.txt') as f:
    raw_data = f.readlines()


def clean_up(raw_data):
    cleaned_lines = []
    for line in raw_data:
        cleaned_line = line.replace('$', '')
        cleaned_line = cleaned_line.replace('\n', '')
        cleaned_line = cleaned_line.split('\t')
        cleaned_line[3] = float(cleaned_line[3])
        cleaned_lines.append(cleaned_line)
    return cleaned_lines


cleaned_data = clean_up(raw_data)
print(cleaned_data[:4])

all_phillie_sales = [i for i in cleaned_data if i[0] == "Philadelphia"]
print(all_phillie_sales)

total_sales = sum([i[3] for i in cleaned_data])
print(total_sales)

''' Http reques'''

start_date = '2017-10-21'
end_date = '2017-10-22'
nasa_response = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date={}&end_date={}&api_key=DEMO_KEY'.format(start_date, end_date))

print(nasa_response.text)
