import numpy as np
import pandas as pd
import torch  # Ensure torch is imported

# Assuming 'df' is your DataFrame and 'symbol_idx' is defined
# Convert 'df['date']' to datetime if not already
df['date'] = pd.to_datetime(df['date'])

# Extract columns and convert to NumPy arrays
start_positions = df['realtime_start_position'].to_numpy(dtype=np.int64)
end_positions = df['realtime_end_position'].to_numpy(dtype=np.int64)
date_positions = df['date_position'].to_numpy(dtype=np.int64)
values = pd.to_numeric(df['value'], errors='coerce').to_numpy(dtype=np.float32)  # Convert to float, invalid values become NaN
datadates = df['date']

# Convert 'datadates' to numerical format
date_values = (datadates.dt.strftime('%Y%m%d').astype(np.int64) * 0.0001).to_numpy(dtype=np.float32)

# Calculate lengths of positions to fill
lengths = end_positions - start_positions + 1
total_positions = lengths.sum()

# Preallocate arrays for indices and values
positions_list = []  # Use lists to accumulate data
date_positions_list = []
values_list = []
date_values_list = []

# Loop over the DataFrame indices
for i in range(len(df)):
    # Create the range of positions for this row
    positions_range = np.arange(start_positions[i], end_positions[i] + 1, dtype=np.int64)
    length = len(positions_range)

    # Append to the lists
    positions_list.append(positions_range)
    date_positions_list.append(np.full(length, date_positions[i], dtype=np.int64))
    values_list.append(np.full(length, values[i], dtype=np.float32))
    date_values_list.append(np.full(length, date_values[i], dtype=np.float32))

# Concatenate lists into single NumPy arrays
positions_array = np.concatenate(positions_list)
date_positions_array = np.concatenate(date_positions_list)
values_array = np.concatenate(values_list)
date_values_array = np.concatenate(date_values_list)
symbol_idx_array = np.full(total_positions, symbol_idx, dtype=np.int64)

# Convert NumPy arrays to PyTorch tensors
positions_tensor = torch.from_numpy(positions_array)
date_positions_tensor = torch.from_numpy(date_positions_array)
values_tensor = torch.from_numpy(values_array)
date_values_tensor = torch.from_numpy(date_values_array)
symbol_idx_tensor = torch.from_numpy(symbol_idx_array)

# Ensure target tensors are PyTorch tensors (e.g., tensor and date_tensor are PyTorch tensors)
# If not, you need to create or convert them accordingly

# Use advanced indexing to fill the tensors
tensor_test[positions_tensor, symbol_idx_tensor, date_positions_tensor] = values_tensor
date_tensor[positions_tensor, symbol_idx_tensor, date_positions_tensor] = date_values_tensor
fillmethod = 1  # If 'fillmethod' is needed
