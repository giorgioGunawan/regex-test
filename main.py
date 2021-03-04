import re
import json
import raw_string

#2.1
product_count_text = "381 Products Found"
product_count_int = int(re.findall("\d+", product_count_text)[0])

#2.2

generic_urls = ["https://www.genericdomain.com/abc/def/1290aodwb23-ghi.img",
                "https://www.genericdomain.com/abc/31287bdwakj-jkl.img",
                "https://www.genericdomain.com/19unioawd02-jkl.img"]

special_sequence = []
for url in generic_urls:
    special_sequence.append(re.findall(r'/(.*?)-', url)[0].split('/')[-1])

#2.3
product_storage_parsed = re.findall(r'products_storage= (.*?);', raw_string.product_storage_string_raw)[0]
product_storage_json = json.loads(product_storage_parsed)
with open('product_storage_json.json', 'w') as f:
    json.dump(product_storage_json, f)
