# split_pool_prob
To calculate rate of collision at differnt input numbers of particles
## Background and motivation
Split-pool indexing strategy relies on combination of multiple layers of indexes. It assumes that the probability of the occurrence same combination of indexes are sufficiently low, that it allows unique assignment of index to particles. The collision rate is therefore an important metric in monitoring the performance of the split-pooling process.
This repo aims to provide an easy to use interface to calculate the collision rate, given a user defined number of input particles. 

## Implementation 
To facilitate the understanding of the experiment, I opt to use simulation instead of calculating the probability directly. It offers rooms for trying parameters. 

## Usage
For the __simulation_experiment.ipynb__ ,it is for demo use to test a single setting. Run by adjusting the parameters.

For the __gen_simulate_data.py__, it repeats the run for a range of parameter and store them in a csv file. Set the range manually in the script, then : 
```
### it take a long time to run, be aware.
python ./gen_simulate_data.py
```
The result will be stored in __simulation_result.csv__ . Data can be visulaized in the __plot_heatmap.Rmd__ script. 


## Experiment with non-uniform distributions
(non_uniform_distribution_prob branch)
The original protocol requires sorting of the nuclei into wells. Sorting ensues a uniform distribution of the nuclei into each well. This uniform distribution allows a consistent probability of sampling unique index combination. 

What outcome should we expect if non-uniform distribution occurs when distributing the nuclei to barcodes, in the first or second or first-and-second nuclei distribution steps? 

We can model the distribution as 1. normal distribution or 2. zero-inflated normal distribution, and calculate the overall duplication rates and other metrics. 

The technical reason behind this exploration is to explore the possibility of skipping the sorting step, which 1. may cause changes to chromatin state, 2. leads to degradation to the chromatin, 3. time consuming. So if possible, we should avoid FACS sorting nuclei. Moreover,  faster processing allows higher throughput, which is the goal of single-cell experiment. Winning in numbers. 