#   S H D
def tower_of_hanoi(disk: int, source: str, helper: str, destination: str) -> None:
    if disk == 1:
        print(f"transfer disk {disk} from  {source} to  {destination}")
        return

    tower_of_hanoi(disk - 1, source, destination, helper)
    print(f"transfer disk {disk} from  {source} to  {destination}")
    tower_of_hanoi(disk - 1, helper, source, destination)


tower_of_hanoi(4, "SOURCE", "HELPER", "DESTINATION")
