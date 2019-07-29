def draw_one_sample_bootstrap(sample_a, test_mean):
# Make an array of translated impact forces: translated_force_b
    translated_sample_a = sample_a-force_a.mean() + test_mean

# Take bootstrap replicates of Frog B's translated impact forces: bs_replicates
    bs_replicates = draw_bs_reps(translated_sample_a, np.mean, 10000)

# Compute fraction of replicates that are less than the observed Frog B force: p
    p = np.sum(bs_replicates <= np.mean(sample_a)) / 10000

# Print the p-value
    print('p = ', p)
