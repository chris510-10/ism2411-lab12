import csv
from datetime import datetime

# --- EXERCISE 2 ---
print("\n--- EXERCISE 2: Raw Rows ---")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# --- EXERCISE 3 ---
print("\n--- EXERCISE 3: Skip Header ---")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# --- EXERCISE 4 ---
print("\n--- EXERCISE 4: Compute Totals ---")

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")


# --- EXERCISE 5 ---
print("\n--- EXERCISE 5: Filter and Write ---")

original_count = 0
written_count = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    with open("data/cleaned.csv", "w", newline="") as output:
        writer = csv.writer(output)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                written_count += 1

print(f"Rows written: {written_count}")
print(f"Original rows: {original_count}")


# --- EXERCISE 6 ---
print("\n--- EXERCISE 6: DictReader ---")

dict_total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"DictReader total revenue: ${dict_total_revenue:.2f}")


# --- EXERCISE 7 ---
print("\n--- EXERCISE 7: Sales Summary ---")

sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")


# --- EXERCISE 8 ---
print("\n--- EXERCISE 8: Run Log ---")

timestamp = datetime.now()

with open("data/run_log.txt", "a") as file:
    file.write(f"{timestamp}: Total Revenue = ${total_revenue:.2f}\n")

print("Run log updated successfully!")
