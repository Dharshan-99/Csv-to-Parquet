import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

csv_file = 'sample.csv'
parquet_file = 'sample.parquet'
chunksize = 100_000

csv_file = pd.read_csv(csv_file, sep='\t', chunksize=chunksize, low_memory=False)

for i, chunk in enumerate(csv_file):
    print("Chunk", i)
    if i == 0: 
        parquet_schema = pa.Table.from_pandas(df=chunk).schema
        parquet_writer = pq.ParquetWriter(parquet_file, parquet_schema, compression='gzip')
    table = pa.Table.from_pandas(chunk, schema=parquet_schema)
    parquet_writer.write_table(table)

parquet_writer.close()
