import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple CLI app")
    parser.add_argument("name", type=str, help="Your name")
    parser.add_argument("--greet", action="store_true", help="Greet the user")

    args = parser.parse_args()

    if args.greet:
        print(f"Hello, {args.name}!")
    else:
        print(f"Welcome, {args.name}")

if __name__ == "__main__":
    main()
