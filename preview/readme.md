# Preview

A catalog with various tests and algorithm results. The tests were selected to show the differences between the algorithms. Below is a description of the file structure and their content:


## Directory  [`input`](input)
- [`memory_tests`](input/memory_tests): Contains text files with tests for memory page replacement algorithms.

    - `basicTest.txt` i `basicTest2.txt`: Basic tests.
    - `interleaved.txt`: Test with interleaving pages.
    - `interleavedPlus.txt`: Test with interleaving pages and additional details.
    - `interleavedMoreOften.txt`: Test with more frequent pages interleaving.
    - `game.txt`: Game-style test.
    - `random.txt`: Random pages test.
    - `interleavedRatio11.txt` i `interleavedRatio12.txt`: Tests with different ratio of page interleaving.

- [`processor_tests`](input/processor_tests): Contains text files with tests for CPU scheduling algorithms.

    - `basicTest.txt` i `basicTest2.txt`: Basic tests.
    - `longShort.txt` i `shortLong.txt`: Tests with long and short tasks.
    - `fiftyFifty.txt`: A test with equal time division between processes.
    - `divergentAe.txt` i `accumulateAe.txt`: Tests with different ranges of max execution time.

## Directory  [`output`](output)
The output directory contains both text files with reports and images showing visual results for better analysis.

- [`memory_tests`](output/memory_tests): Contains results for tests related to memory page replacement.

_Click [here](output/memory_tests/readme.md) for a list of readme files with comparisons of memory page replacement algorithm performance for each test_

Example: `FIFO_basicTest.png`, `LFU_interleavedMoreOften.txt`.

- [`processor_tests`](output/processor_tests): Contains results for tests related to CPU time scheduling.

_Click [here](output/processor_tests/readme.md) for a list of readme files with comparisons of CPU scheduling algorithm performance for each test_

Example: `FCFS_basicTest.png`, `SJF_longShort.txt`.