
units = int(input("Enter electricity units: "))
ration = input("Ration card (yes/no): ").lower()
senior = input("Member above 80 (yes/no): ").lower()

print("\nUsing separate if statements:")

if units <= 100:
    print("Full subsidy")
if 101 <= units <= 200 and ration == "yes":
    print("Partial subsidy")
if 101 <= units <= 200 and ration != "yes":
    print("No subsidy")
if units > 200 and senior == "yes":
    print("Special subsidy")
if units > 200 and senior != "yes":
    print("No subsidy")

print("\nUsing if-elif-else:")

if units <= 100:
    print("Full subsidy")
elif 101 <= units <= 200 and ration == "yes":
    print("Partial subsidy")
elif units > 200 and senior == "yes":
    print("Special subsidy")
else:
    print("No subsidy")
