# Stirling Numbers Plotter

A program to calculate and visualize the Stirling numbers of the second kind for sets of size 1 to `n`.

## Overview

The **Stirling Numbers Plotter** calculates the Stirling numbers of the second kind for sets of sizes ranging from 1 to `n` and generates plots to visualize the distribution of the number of subsets for each set size. The resulting plots can be saved to a specified folder.

## Prerequisites

- Python 3.6 or higher
- `matplotlib` library for plotting
- Any additional required libraries (e.g., `numpy`, `os`)

## Installation

1. **Clone the repository**:

    1. `git clone git@github.com:ubk8751/SterlingNumbersPlotter.git` (SSH)
    2. `git clone https://github.com/ubk8751/ SterlingNumbersPlotter.git` (HTTPS)
    3. `cd stirling-numbers-plotter`

2. **Install the required libraries:**
   
    `pip install -r requirements.txt`

## Usage

`python stirling_number_of_second_kind_plotter.py -n [int] [--image-folder [str]]`

### Command-Line Flags

- `-n [int]`: (Required) Specifies the size of the largest set to calculate the Stirling number for. Default value is 1.
- `--image-folder [str]`: (Optional) The folder to save the generated plots. If not specified, the default folder `./img/` will be used.

### Examples

1. **Calculate and plot Stirling numbers for sets up to size 5:**

    `python stirling_number_of_second_kind_plotter.py -n 5`

2. **Save plots to a custom folder:**
   
   `python stirling_number_of_second_kind_plotter.py -n 10 --image-folder ./my_plots/`

### Output

The program will generate bar plots for each set size from 1 to `n`, showing the distribution of the number of subsets. These plots will be saved as image files in the specified folder.

## Description of the Stirling Numbers of the Second Kind


The Stirling number of the second kind, denoted as `S(n, k)`, represents the number of ways to partition a set of `n` elements into `k` non-empty subsets. It is defined recursively as:

$$ S(n, k) = k \times S(n-1, k) + S(n-1, k-1) $$

with the base cases:

- $S(0, 0) = 1$
- $S(n, 0) = 0$ for $n > 0$
- $S(0, k) = 0$ for $k > 0$
- $S(n, k) = 0$ if $k > n$