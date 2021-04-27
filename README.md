# split_pool_prob
To calculate rate of collision at differnt input numbers of particles
## Background and motivation
Split-pool indexing strategy relies on combination of multiple layers of indexes. It assumes that the probability of the occurrence same combination of indexes are sufficiently low, that it allows unique assignment of index to particles. The collision rate is therefore an important metric in monitoring the performance of the split-pooling process.
This repo aims to provide an easy to use interface to calculate the collision rate, given a user defined number of input particles. 

## implementation 
To facilitate the understanding of the experiment, I opt to use simulation instead of calculating the probability directly. It offers rooms for trying parameters. 