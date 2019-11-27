#####  Page Rank Algorithm
This contains the code for parallelized multiple linear regression and NaiveBayes developed from scratch using PySpark. 
The instructions are fairly straightforward

```
CODE - pagerank.py
OUTPUT - PageRanks.txt
```

##### To Run:
```
/usr/bin/spark-submit <PYTHON_CODE_FILE> <INPUT_PATH>
For example,   
/usr/bin/spark-submit pagerank.py /user/darora2/pagerank/simplewiki-20150901-pages-articles-processed.xml
```

##### Get the output part files from HDFS into one local file by following command.
```
hadoop fs -getmerge <output_path_in_HDFS> <file_path_where_merged_output_is_required>
For instance,  
hadoop fs -getmerge /user/darora2/OrderedPageRank/part* /users/darora2/Cloud/Assignment3/PageRanks.txt
```
##### Environment: AWS EMR or Cloudera Hadoop


##### REFERENCES
1. https://github.com/apache/spark
2. https://spark.apache.org/docs/latest/
