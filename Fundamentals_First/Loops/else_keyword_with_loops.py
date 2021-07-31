cars = ["ok", "ok", "ok", "ok", "ok", "ok"]
#all_successful = True

for status in cars:
    if status == "faulty":
        print("Stopping the production line")
#       all_successful = False
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")

else:
    print("All cars built successfully. No faulty cars!")

#if all_successful:
#    print("All cars built successfully. No fault cars!") 




