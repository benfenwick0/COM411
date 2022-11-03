def observed():
    observations = []

    for i in range(7):
        observations.append(input("Enter an observation"))

    return observations

def run():
    print("Counting observations...")
    observations = observed()

    observations_set = set()
    for i in observations:
        data = (i, observations.count(i))
        observations_set.add(data)

    for data in observations_set:
        print(f"{data[0]} observed {data[1]} times.")

run()