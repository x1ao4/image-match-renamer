import os

folder_path = '/path/to/your/folder'

with open(os.path.join(folder_path, 'data.txt'), 'r') as f:
    lines = f.readlines()

title_to_number = {}
for line in lines:
    data = line.strip().split(';')
    number = data[0]
    title = data[3]
    title_to_number[title] = number

image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

skipped_count = 0
for image_file in image_files:
    title = image_file.split(' ')[-1].split('.')[0]
    if title not in title_to_number:
        skipped_count += 1
print(f'Total skipped: {skipped_count}')
print()

image_files.sort(key=lambda x: int(title_to_number.get(x.split(' ')[-1].split('.')[0], 999999)))

renamed_count = 0
for image_file in image_files:
    title = image_file.split(' ')[-1].split('.')[0]
    if title in title_to_number:
        new_name = title_to_number[title] + '.jpg'
        os.rename(os.path.join(folder_path, image_file), os.path.join(folder_path, new_name))
        print(f'{image_file.split(".")[0]} > {new_name.split(".")[0]}')
        renamed_count += 1

print()
print(f'Total renamed: {renamed_count}')