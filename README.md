# My Advent of Code 2024

I've never done Advent of Code before so I'm giving it a shot! I'll have a different subdirectory for each day. I don't have a wild hook for how I'm solving, just using Python and trying to challenge myself a bit. 

For as long as I can I'll try to do a "no external dependencies" run, but no promises!

## Running my solutions

I'm using uv, so you can clone this repo
```git clone https://github.com/mcmullarkey/advent-of-code-2024.git```

Install uv if you haven't already
```
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```
```
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
And then from the root directory run, for example
```uv run 01/solution.py```

Replace the `01` with whatever day's solution you'd like to run.