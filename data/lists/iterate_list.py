def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction: ")
    dis = directions()
    for i in range(len(dis)):
        print(f"{i}: {dis[i]}")


def run():
    menu()

if __name__ == "__main__":
    run()