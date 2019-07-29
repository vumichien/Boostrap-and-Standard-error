"""A two-sample bootstrap hypothesis test for difference of means"""
import numpy as np

def two_samples_bootstrap(sample_a, sample_b):
# Compute mean of all sample: mean_sample, empirical_diff_means
    sample_concat = np.concatenate(sample_a,sample_b, axis = 0)
    mean_sample = sample_concat.mean()

    empirical_diff_means = np.mean(sample_a) - np.mean(sample_b)
# Generate shifted arrays
    sample_a_shifted = sample_a - np.mean(sample_a) + mean_force
    sample_b_shifted = sample_b - np.mean(sample_b) + mean_force

# Compute 10,000 bootstrap replicates from shifted arrays
    bs_replicates_a = draw_bs_reps(sample_a_shifted, np.mean, 10000)
    bs_replicates_b = draw_bs_reps(sample_b_shifted, np.mean, 10000)

# Get replicates of difference of means: bs_replicates
    bs_replicates = bs_replicates_a -bs_replicates_b

# Compute and print p-value: p
    p = np.sum(bs_replicates >= empirical_diff_means) / 10000
    print('p-value =', p)
