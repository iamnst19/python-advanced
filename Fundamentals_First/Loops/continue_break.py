cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok"]

# Break
for status in cars:
    if status == "faulty":
        print("Stopping the production")
        break
    print(f"This car is {status}.")

# Continue
for status in cars:
    if status == "faulty":
        print("Found Faulty car, skipping")
        continue
    print(f"This car is {status}.")
    print("Shipping new car to customer")

# Sample for loop to use values in a collection 
kid_ages = (3, 7, 12)
for age in kid_ages:
  print(f'I have a {age} year old kid.')