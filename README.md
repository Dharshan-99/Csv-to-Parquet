# Parquet

### What is Parquet?

Parquet is an open source file format available to any project in the Hadoop ecosystem (Hadoop Ecosystem is a platform or a suite which provides various services to solve the big data problems).
Apache Parquet is designed for efficient as well as performant flat columnar storage format of data compared to row based files like CSV or TSV files.


## Advantages of Storing Data in a Parquet (Columnar Format):

* ***Columnar storage*** like Apache Parquet is designed to bring efficiency compared to row-based files like CSV.
When querying, columnar storage you can skip over the non-relevant data very quickly.
As a result, aggregation queries are less time consuming compared to row-oriented(CSV) databases.

* The layout of Parquet data files is optimized for queries that process large volumes of data, in the gigabyte range for each individual file.
* Apache Parquet works best with interactive and serverless technologies like AWS Athena, Amazon Redshift Spectrum, Google BigQuery and Google Dataproc.
* Google and Amazon will charge you according to the amount of data stored on GS/S3. Parquet has helped its users reduce storage requirements by at least one-third on large datasets, in addition, it greatly improved scan and deserialization time

### Columnar Storage Format
In columnar storage format above table will be stored column wise.

Columnar Storage Format :


![image](https://user-images.githubusercontent.com/75352450/130431311-a79f1d52-1463-4556-9415-a76bf9b910a5.png)



As you can see in this format all the IDs are together and  names and salaries. A Query selecting Name column will require less I/O time as all the values are adjacent unlike in row oriented format.

## CSV to Parquet File(Using Python):

### libraries to import:
```
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
```
Giving path to csv file.
```
csv_file = 'sample.csv'
```
Parquet output file name:
```
parquet_file = 'my1.parquet'
```
Using Chunk size for reading csv.
```
chunksize = 100_000
csv_file = pd.read_csv(csv_file, sep='\t', chunksize=chunksize, low_memory=False)
```
_Chunk size is a  parameter essentially means the number of rows to be read into a dataframe at any single time in order to fit into the local memory._

Read columns one by one by using _enumerate_...
```
for i, chunk in enumerate(csv_file):
    print("Chunk", i)
    if i == 0: 
        parquet_schema = pa.Table.from_pandas(df=chunk).schema
        parquet_writer = pq.ParquetWriter(parquet_file, parquet_schema, compression='gzip')
    table = pa.Table.from_pandas(chunk, schema=parquet_schema)
    parquet_writer.write_table(table)
```
Printing the no.of chunk for the sample csv file.

Closing the Parquet Writer
```
parquet_writer.close()
```

After executing the above code...The Parquet file is created named _"sample.parquet"_ in our directory.

### File sizes:-
| Sample.csv  | sampleparquet |
| ------------- | ------------- |
| 109 MB | 15.7 MB  |

_NOTE: Here I taken small size csv file(sample file).We may use any size of file_

The above shows the difference between the cvs and Parquet file.

### Reading Parquet File using Pandas:-
```
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
table=pd.read_parquet('filename.parquet', engine='pyarrow')
table
```


In this Tutorial we learn about Parquet file and how to convert csv to Parquet file.




