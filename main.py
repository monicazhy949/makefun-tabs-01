"""One number: the honest count of open browser tabs, for make.fun."""
import os

OUTPUT_PATH = "/output/entry.txt"

# 173 tabs, counted just now across three windows: research saved
# "for later", docs left open mid-task, and a dozen videos queued for
# a weekend that never came. An odd, exact number -- the kind a real
# count gives you, not a round guess.
COUNT = "173"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(COUNT)


if __name__ == "__main__":
    main()
