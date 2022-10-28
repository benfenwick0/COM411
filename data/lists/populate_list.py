def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction: ")
    dis = directions()
    for i in range(len(dis)):
        print(f"{i}: {dis[i]}")
    i = int(input())
    return dis[i]


def run():
    route = []
    print("Working out escape route...")
    for count in range(5):
        route.append(menu())
    print(f"escape route: {route}")

if __name__ == "__main__":
    run()
