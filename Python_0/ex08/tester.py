from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main():
    try:

        for elem in ft_tqdm(range(333)):
            sleep(0.005)
        print()

        for elem in tqdm(range(333)):
            sleep(0.005)
        print()

    except Exception as message:
        print(f"{type(message).__name__}{message}")


if __name__ == "__main__":
    main()
