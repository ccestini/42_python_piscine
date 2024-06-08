from load_image import ft_load


def main():
    try:
        print(ft_load("landscape.jpg"))
    except Exception as message:
        print(f"{type(message).__name__}: {message}")


if __name__ == "__main__":
    main()
