no_of_vehicles = []

no_of_lanes = int(input("Enter number of lanes:"))

for no in range(no_of_lanes):
    x = int(input(f"Enter number of vehicles of lane {no+1}:"))
    no_of_vehicles.append(x)

baseTimer = 120  # baseTimer = int(input("Enter the base timer value"))
timeLimits = [5, 30]  # timeLimits = list(map(int,input("Enter the time limits ").split()))

# print("Input no of vehicles : ", *no_of_vehicles)
t = [(i / sum(no_of_vehicles)) * baseTimer if timeLimits[0] < (i / sum(no_of_vehicles)) * baseTimer < timeLimits[1]
else min(timeLimits, key=lambda x: abs(x - (i / sum(no_of_vehicles)) * baseTimer)) for i in no_of_vehicles]

# print(t, sum(t))

for no in range(no_of_lanes):
    print(f"* lane {no+1} => No of vehicles: {no_of_vehicles[no]} => Time: {t[no]}s")

print(f"* Total of vehicles: {sum(no_of_vehicles)} => Total time: {sum(t)}s")