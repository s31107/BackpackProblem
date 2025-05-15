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
            if not self._acceptability_test(current):
                continue
            val = self.compute_value(current)
            if best_selection[1] < val:
                best_selection = (current, val)
                print(f"Iteration {current}, best = {best_selection}, val = {val}")
        return best_selection[0]

    def compute_value(self, selected_items: int) -> int:
        value_sum = 0
        while selected_items != 0:
            if selected_items % 2 == 1:
                value_sum += self.items[selected_items.bit_length() - 1].value
            selected_items >>= 1
        return value_sum

    def _acceptability_test(self, selected_items: int) -> bool:
        selected_items_size = 0
        while selected_items != 0:
            if selected_items_size > self.k:
                return False
            if selected_items % 2 == 1:
                selected_items_size += self.items[selected_items.bit_length() - 1].weight
            selected_items >>= 1
        return True