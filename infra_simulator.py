import json
from pathlib import Path
from pydantic import ValidationError
from src.machine import Computer
import logging
import subprocess

logging.basicConfig(
    filename="logs/provisioning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def user_computer_input() -> list[Computer]:
    computers: list[Computer] = []

    while True:
        print("==========================")
        print("       Choose a computer       ")
        print("__________________________")

        system = input("Enter system (windows/mac/linux) or 'done' to finish: ")

        if system.lower() == "done":
            break

        gpu = input("Enter GPU (nvidia/intel): ")
        ram_str = input("Enter RAM (4, 8, 12, 16, 32, 64): ")
        cpu_str = input("Enter CPU (2, 4, 8, 10, 12): ")

        try:
            ram = int(ram_str)
            cpu = int(cpu_str)

            comp = Computer(
                system=system,
                gpu=gpu,
                ram=ram,
                cpu=cpu
            )

        except ValueError as e:
            print(f"[INPUT ERROR] {e}")
            logging.error(f"Input error: {e}")
            continue

        except ValidationError as e:
            print("[VALIDATION ERROR]")
            print(e)
            logging.error(f"Validation error: {e}")
            continue

        computers.append(comp)
        logging.info(f"New computer added: {comp}")

    return computers


def save_to_json(computers: list[Computer]):
    Path("configs").mkdir(exist_ok=True)

    data = [c.model_dump() for c in computers]

    with open("configs/instances.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    logging.info("Saved computers to configs/instances.json")


if __name__ == "__main__":
    machines = user_computer_input()
    save_to_json(machines)
    print("Done!")

#def run_service_setup():
#    try:
#        subprocess.run(["bash", "scripts/setup_service.sh"], check=True)
#    except subprocess.CalledProcessError as e:
#        print("[ERROR] Service setup failed.")
#        logging.error(f"Service setup failed: {e}")

#if __name__ == "__main__":
#    machines = user_computer_input()
#    save_to_json(machines)
#    run_service_setup()
#    print("Done!")
