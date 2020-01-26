# Traveling Salesperson Visualization

* To setup, start by creating a virtual environment:

    `python3 -m venv venv`

* Then install the required packages:

    `pip3 install -r requirements.txt`

* Finally, run `traveling_salesperson.py`

    The first time it will only have 3 points (cities)

    Change the value of the constant `NUM_CITIES` to 4, then 5, then 6, etc. to see how the time to find the shortest path changes.  Do you notice a pattern? (Hint: What is the difference between 3! and 4!; between 4! and 5!; between 5! and 6!; etc.)