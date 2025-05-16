class Item:
    def __init__(self, weight: int, value: int):
        self.weight = weight
        self.value = value


class BackpackProblem:
    def __init__(self, k: int, n: int, items: list[Item]):
        self.k = k
        self.n = n
        self.items = items

    def generate_backpack(self) -> int:
        best_selection = (0, 0)
        for current in range(1, 2 ** self.n):
            processed_items = self.process_items(current)
            if processed_items is None:
                continue

            if best_selection[1] < processed_items.value:
                best_selection = (current, processed_items.value)
                binary_items = bin(best_selection[0]).removeprefix("0b").zfill(self.n)
                print(f"Iteration {current}, best = {binary_items}, val = {best_selection[1]}")
        return best_selection[0]

    def process_items(self, selected_items: int) -> Item | None:
        items_sum = Item(0, 0)

        for item_iter in range(self.n - 1, -1, -1):
            if selected_items == 0:
                break

            if selected_items % 2 == 1:
                items_sum.value += self.items[item_iter].value
                items_sum.weight += self.items[item_iter].weight
            selected_items >>= 1

            if items_sum.weight > self.k:
                return None
        return items_sum
