# question 1 task 1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# destinations both fly to:
overlap = our_routes.intersection(competitor_routes)

print(f"Both airlines fly to: {overlap}")

# destinations unique to our airline:
unique_destinations = our_routes.difference(competitor_routes)

print(f"Our airline flys to unique destinations through: {unique_destinations}")

# destinations not shared by airlines:
all_destinations = our_routes.union(competitor_routes)
not_shared = all_destinations.difference(overlap)

print(f"These destinations are not shared by the airlines: {not_shared}")