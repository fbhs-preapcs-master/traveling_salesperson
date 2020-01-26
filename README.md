# Traveling Salesperson Visualization

* To setup, start by creating a virtual environment:

    `python3 -m venv venv`

* Then install the required packages:

    `pip3 install -r requirements.txt`

* Run `traveling_salesperson.py`

    The first time it will only have 3 points (cities)

    Use the + key (or =) to increase the number of cities, one at a time (- will decrease the number).   Pay attention to how long it takes to find the "shortest path".  Do you notice a pattern? (Hint: What is the difference between 3! and 4!; between 4! and 5!; between 5! and 6!; etc.)

    <details><summary>Click AFTER looking for the pattern!</summary>
    

    `traveling_salesperson.py` finds the absolute shortest path between all of the "cities".  It has a run-time of `O(n!)`.  Here is a table summarizing the approximate time it took for each number of cities:

    | NUM_CITIES| Seconds to Complete| Change from Previous |
    |:-: | :-:| :-: |
    | 3  | 0.25 | --- |
    | 4  | 1 | x4 |
    | 5  | 5 | x5 |
    | 6  | 30 | x6 |
    | 7 | 210 (3.5 minutes)| x7 |
    | 8 | 1680 (28 minutes)| x8|
    | 9 | 15120 (4.2 hours) | x9 |
    | 10| 42 hours (1.75 days) | x10 |

    You obviously didn't go past 7 elements, but you can see what would have happened if you did!

    

    </details>

* Run `tsp_heuristic.py`, also changing the number of cities using +/- one value one at a time.  What do you notice?

    <details><summary>Click ONLY AFTER running the program for multiple values of NUM_CITIES</summary>

    This is an example of a **heuristic** solution to this problem.  A heuristic is a technique designed for solving a problem more quickly when classic methods are too slow (from Wikipedia). The downside is that a heuristic may not find the actual **best** solution.  But it will find a pretty good one in MUCH less time than the previous algorithm.

    This particular solution is an example of a **construction heuristic** because it builds the solution from scratch.  Construction heuristics are often referred to as **greedy heuristics**.  Each step checks for the best next step, but does not look any farther ahead.  

    This particular algorithm is usually called the **nearest neighbor heuristic**.  

    Increase the number of cities to around 20 and run the program.  Press the `M` key once, then press `R` to reload.  You can then press `ENTER` to step through the city selection process.  Watch as it selects the *closest* neighbor at each step.  

    This is only one heuristic approach (and definitely not the best).  There are other heuristics called **improvement heuristics** which start with a feasible solution and look for an improved solution that can be found by making a very small number of changes.  These heuristics are a bit more complex, but 
    
    </details>
