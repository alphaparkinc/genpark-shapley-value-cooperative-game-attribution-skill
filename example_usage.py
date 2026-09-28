"""Example demonstrating Shapley value fair profit allocation."""
from client import ShapleyAttribution

def main():
    players = ["A", "B", "C"]
    val_map = {
        "A": 10.0, "B": 20.0, "C": 30.0,
        "A,B": 40.0, "A,C": 50.0, "B,C": 60.0,
        "A,B,C": 90.0
    }
    def v(c):
        return val_map.get(",".join(sorted(c)), 0.0)
    res = ShapleyAttribution.compute_shapley_values(players, v)
    print("Shapley Fair Value Allocation:", res)

if __name__ == "__main__":
    main()
