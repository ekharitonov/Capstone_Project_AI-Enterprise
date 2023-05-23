import numpy as np
from scipy.stats import entropy, wasserstein_distance

def get_wasserstain_distance(data, batch_size=1000, confidence=0.05):
    wasserstein_data = np.zeros(batch_size)
    for batch in range(batch_size):
        samples = int(np.round(0.8 * data.shape[0]))
        subset_indices = np.random.choice(np.arange(data.shape[0]), samples, replace=True).astype(int)
        data_batch = data[subset_indices, :]
        wasserstein_data[batch] = wasserstein_distance(data.flatten(), data_batch.flatten())
    wasserstein_data.sort()
    return wasserstein_data[int((1-confidence) * batch_size)] + wasserstein_data[int(confidence * batch_size)]
