import sys
import os

from BackpackProblem import Item, BackpackProblem

path = sys.argv[1]
if not os.path.isfile(path):
    raise FileNotFoundError(f"File {path} not found")

with open(file=path, mode="r") as file:
    n, k = map(int, file.readline().split(" "))
    items = [Item(int(item[0]), int(item[1])) for item in zip(file.readline().split(","), file.readline().split(","))]
print(BackpackProblem(k, n, items).generate_backpack())
