import csv

input_file = "bb45d9d1-bd6e-4364-b3d5-95be4c2ff757_Data.csv"
output_file = "result.csv"


try:
    with open(input_file, encoding="utf-8") as file:
        reader = csv.reader(file)
        data = list(reader)

except FileNotFoundError:
    print(f"Помилка: файл '{input_file}' не знайдено.")
    exit()

except PermissionError:
    print(f"Помилка: немає дозволу на читання файлу '{input_file}'.")
    exit()

except Exception as e:
    print("Невідома помилка при відкритті файлу:", e)
    exit()

print("=== Вміст CSV файлу ===")
for row in data:
    print(row)



user_input = input("\nВведіть назви країн через кому: ")
search_countries = [c.strip() for c in user_input.split(",")]

found_rows = []

for row in data[1:]:  
    country_name = row[2]
    if country_name in search_countries:
        found_rows.append(row)


try:
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(data[0])
        writer.writerows(found_rows)

    print(f"\nРезультат успішно записано у '{output_file}'.")

except Exception as e:
    print("Помилка при записі у файл:", e)
