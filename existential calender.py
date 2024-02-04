# Outputs the number of weeks left Given an optimistic living year as 90

print("------ Life in Weeks------")
age = input("Enter your age")

years_left_to_live = 90 - int(age)

# Print the years in weeks

weeks = years_left_to_live * 52

""" We multiply by 52 since we have 52 weeks ia a year

"""
print(f"You have {weeks} weeks left.")