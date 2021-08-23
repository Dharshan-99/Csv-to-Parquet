# Parquet

### What is Parquet?

Parquet is an open source file format available to any project in the Hadoop ecosystem (Hadoop Ecosystem is a platform or a suite which provides various services to solve the big data problems).
Apache Parquet is designed for efficient as well as performant flat columnar storage format of data compared to row based files like CSV or TSV files.


## Advantages of Storing Data in a Parquet (Columnar Format):

* Columnar storage like Apache Parquet is designed to bring efficiency compared to row-based files like CSV.
When querying, columnar storage you can skip over the non-relevant data very quickly.
As a result, aggregation queries are less time consuming compared to row-oriented(CSV) databases.

* The layout of Parquet data files is optimized for queries that process large volumes of data, in the gigabyte range for each individual file.
* Apache Parquet works best with interactive and serverless technologies like AWS Athena, Amazon Redshift Spectrum, Google BigQuery and Google Dataproc.
* Google and Amazon will charge you according to the amount of data stored on GS/S3. Parquet has helped its users reduce storage requirements by at least one-third on large datasets, in addition, it greatly improved scan and deserialization time

## CSV to Parquet

