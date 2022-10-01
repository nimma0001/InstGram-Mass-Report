import json
from pathlib import Path


def main():
    config_path = Path("config.json") 

    n = int(input("How many Account you want to Add: "))

    if config_path.exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as file:
                config = json.load(file)
        except BaseException:
            config = {
            "accounts": []
            }
    else:
        config = {
            "accounts": []
        }

    for _ in range(n):
        new_account = {
            "ac": input("enter ur username: "),
            "ps": input("enter ur password: ")
        }
        config["accounts"].append(new_account)

    with open(config_path, 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=4)


if __name__ == '__main__':
    main()