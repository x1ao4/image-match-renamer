import os
import re

folder_path = '/path/to/your/folder'

with open(os.path.join(folder_path, 'data.txt'), 'r') as f:
    lines = f.readlines()

title_to_number = {}
for line in lines:
    data = line.strip().split(';')
    number = data[0]
    title = re.sub(r'[^a-zA-Z0-9]', '', data[3].lower())
    title_to_number[title] = number

image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

title_count = {}
for image_file in image_files:
    title = re.sub(r'[^a-zA-Z0-9]', '', ' '.join(image_file.split(' ')[1:]).split('.')[0].lower())
    if title in title_to_number:
        title_count[title] = title_count.get(title, 0) + 1

skipped_count = 0
for image_file in image_files:
    title = re.sub(r'[^a-zA-Z0-9]', '', ' '.join(image_file.split(' ')[1:]).split('.')[0].lower())
    if title not in title_to_number or title_count[title] > 1:
        skipped_count += 1
print(f'Total skipped: {skipped_count}')
print()

image_files.sort(key=lambda x: int(title_to_number.get(re.sub(r'[^a-zA-Z0-9]', '', ' '.join(x.split(' ')[1:]).split('.')[0].lower()), 999999)))

renamed_count = 0
for image_file in image_files:
    title = re.sub(r'[^a-zA-Z0-9]', '', ' '.join(image_file.split(' ')[1:]).split('.')[0].lower())
    if title in title_to_number and title_count[title] == 1:
        new_name = title_to_number[title] + '.jpg'
        os.rename(os.path.join(folder_path, image_file), os.path.join(folder_path, new_name))
        print(f'{image_file.split(".")[0]} > {new_name.split(".")[0]}')
        renamed_count += 1
        lines = [line for line in lines if re.sub(r'[^a-zA-Z0-9]', '', line.strip().split(';')[3].lower()) != title]

print()
print(f'Total renamed: {renamed_count}')

with open(os.path.join(folder_path, 'data.txt'), 'w') as f:
    f.writelines(lines)
