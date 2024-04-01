# Operating Systems Project - Algorithm simulations

The project was created as a final project for the course 'Operating Systems'
The project includes implementations of [`CPU time scheduling algorithms`](https://en.wikipedia.org/wiki/Scheduling_(computing)) and [`page replacement algorithms`](https://en.wikipedia.org/wiki/Page_replacement_algorithm).

## Running

1. Clone the repository: `git clone https://github.com/USER/REPO.git`
2. Navigate into the cloned repository: `cd REPO`
3. Install the required dependencies:`pip install -r requirements.txt`
4. Run the main script with the appropriate arguments
```python main.py [options]```

Options:

- `-A`: Run all simulations, generate all graphs, and generate all summaries.
- `-P`: Run processor simulations, generate processor graphs, and generate processor summaries.
- `-M`: Run memory simulations, generate memory graphs, and generate memory summaries.

You can also specify one of the following optional arguments to limit the actions performed:

- `-S`: Only run simulations.
- `-g`: Only generate graphs.
- `-s`: Only generate summaries.
- `-r`: Only generate readme files.

If no optional argument is provided, all actions (simulations, graphs, summaries) will be performed.

For example, to run all simulations, you would use:
```python main.py -A -S```

## Project structure

### Directory: [`input`](input)
- [`memory_tests`](input/memory_tests): Contains text files with tests for page replacement algorithms 

_Test case file description for page replacement algorithms is available: [Here](preview/input/memory_tests/inputStructure.md)_

- [`processor_tests`](input/processor_tests): Contains text files with tests for CPU time scheduling

_Test case file description for CPU time scheduling algorithms is available: [Here](preview/input/processor_tests/inputStructure.md)_

### Directory: [`output`](output)

Subfolders contains both - text files with raw results and images showing visual results for better analysis

- [`memory_tests`](output/memory_tests): Contains simulation results of page replacement algorithms
    - text files with raw data - `[Algorithm_Shortcut]_[Test_case_name].txt`
    - visual results - `[Algorithm_Shortcut]_[Test_case_name].png`
    

_Output file structure for specific test and used (memory) algorithm is described: [Here](preview/output/memory_tests/outputStructure.md)_


- [`processor_tests`](output/processor_tests): Contains simulation results of CPU time scheduling
    - text files with raw data - `[Algorithm_Shortcut]_[Test_case_name].txt`
    - visual results - `[Algorithm_Shortcut]_[Test_case_name].png`

_Output file structure for specific test and used (processor) algorithm is described: [Here](preview/output/processor_tests/outputStructure.md)_

### Directory: [`preview`](preview)

This folder contains the results of my tests for a report summarizing and comparing the performance of the algorithms
Report is available as a `README.md` files in dedicated folders

_Click [here](preview/readme.md) to go to the algorithm results for my test cases._

### Directory: [`src`](src)

Most of objects/class/method/fields, even obevious, are described in detail due to college course requirements

```
📦src
 ┣ 📂generators
 ┃ ┣ 📜ProcessGenerator.py
 ┃ ┣ 📜QueueGenerator.py
 ┃ ┗ 📜ReadmeGenerator.py
 ┣ 📂managers
 ┃ ┣ 📜FileManager.py
 ┃ ┣ 📜TestsManager.py
 ┃ ┗ 📜PlotManager.py
 ┣ 📂objects
 ┃ ┣ 📜ATestCase.py
 ┃ ┣ 📜ATestResult.py
 ┃ ┗ 📜SummaryTable.py
 ┣ 📂processor
 ┃ ┣ 📂objects
 ┃ ┃ ┗ (...)
 ┃ ┣ 📜BaseProcessor.py
 ┃ ┣ 📜[Algo_Shortcut]Processor.py
 ┣ 📂ram
 ┃ ┣ 📂objects
 ┃ ┃ ┗ (...)
 ┃ ┣ 📜BaseMemory.py
 ┃ ┣ 📜[Algo_Shortcut]Memory.py
 ┗ 📜Main.py
 ```
 - `./generators`: Generator classes (e.g. generating readme files, tests to run, etc.)
 - `./managers`: File, Plot and Tests management classes
 - `./objects`: Objects for general usage, abstract classes
 - `./processor` or `./memory`:
    - `./objects`: Sub-objects used exclusively for one of algorightms
    - `BaseMemory.py` or `BaseProcessor.py`: An abstract class implements general functions of algorithm
    - `[Algo_shortcut]Memory.py` or `[Algo_Shortcut]Processor.py`: Child class inheriting from suitable abstract class. Implements only method that decides which one of _Processes_ or _Memory pages_ goes first
 - `Main.py` - Main class of program
