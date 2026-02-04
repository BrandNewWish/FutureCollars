import csv
import sys
import os



def main():
    if len(sys.argv) < 3:
        print("Usage: python reader.py <src> <dst> <change1> <change2> ...")
        sys.exit(1)


    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]



    if not os.path.isfile(src):
        print(f"Error: '{src}' is not a valid file.")
        directory = os.path.dirname(src) or "."
        print("File in the same directory:")
        for name in os.listdir(directory):
            print(name)
        sys.exit(1)

    with open(src, newline="") as f:
        reader = csv.reader(f)
        data = list(reader)

    for change in changes:
        try:
            x, y, value = change.split(",", 2)
            x = int(x)
            y = int(y)
            data[y][x] = value
        except (ValueError, IndexError):
            print(f"Skipping invalid change: {change}")


    for row in data:
        print(",".join(row))



    with open(dst, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)



if __name__ == "__main__":
    main()