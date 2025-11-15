import csv

filename = "bb45d9d1-bd6e-4364-b3d5-95be4c2ff757_Data.csv"  

with open(filename, encoding="utf-8") as file:
    reader = csv.reader(file)
    data = list(reader)





user_input = input("\nВведіть назви країн через кому: ")

search_countries = [c.strip() for c in user_input.split(",")]

found_rows = []

for row in data[1:]:
    country_name = row[2] 
    if country_name in search_countries:
        found_rows.append(row)

if not found_rows:
    print("Країни не знайдені.")
else:
    print("\n=== Знайдені дані ===")
    for row in found_rows:
        print(row)



output_filename = "result.csv"

with open(output_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(data[0])
    writer.writerows(found_rows)

print(f"\nРезультат записано у файл {output_filename}")
