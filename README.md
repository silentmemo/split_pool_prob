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
The result will be stored in __simulation_result.csv__ . Data can be visulaized in the __plot_heatmap.R__ script. 
