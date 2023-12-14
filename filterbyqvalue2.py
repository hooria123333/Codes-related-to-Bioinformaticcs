import pandas as pd

def filter_tsv_QValue(tsv_file, QValue):
  """Filters a tsv file at a given FDR.

  Args:
    tsv_file: The path to the tsv file to filter.
    fdr: The FDR threshold.

  Returns:
    A pandas DataFrame containing the filtered data.
  """

  # Read the tsv file into a pandas DataFrame.
  df = pd.read_csv(tsv_file, sep='\t')

  # Filter the DataFrame to only include rows with an FDR of fdr or less.
  df_filtered = df[df['QValue'] <= QValue]

  return df_filtered

# Filter the tsv file at 0.01 FDR.
df_filtered = filter_tsv_QValue('outputT3_NaF.tsv', 0.01)

# Save the filtered tsv file.
df_filtered.to_csv('outputT3_NaFfiltered.tsv', sep='\t', index=False)
