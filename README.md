# Cloud_Computing

WordCount on Hadoop VM:

1. Install Hadoop in a virtual machine using the Hadoop VM installation instructions handout, and verify the WordCount program is working fine. 
Look at the source code and description of the WordCount program to understand how it works:
https://www.cloudera.com/documentation/other/tutorial/CDH5/topics/ht_wordcount1_source.html

You may also look at how to build and run the WordCount program:
https://www.cloudera.com/documentation/other/tutorial/CDH5/topics/ht_usage.html
Note: If you get an error when compiling the WordCount class, you may need to execute the command without the “-Xlint” option.  
For example, when compiling in a parcel installation of CDH, use:javac -cp /opt/cloudera/parcels/CDH/lib/hadoop/*:/opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/* WordCount.java -d build 

2. Download  the  Canterbury  Corpus  (http://corpus.canterbury.ac.nz/descriptions/) from http://corpus.canterbury.ac.nz/resources/cantrbry.zip . 

3. Run  WordCount  on  the  alice29.txt  input  file  and  then  on  the  asyoulik.txt  input  file.

4. Save  the  last  20  lines  of  output  from  WordCount  for  each  of  the  two  input  files.  The  output  files  (each  consisting  of  the  last  20  lines  of  output)  corresponding  to  the input files alice29.txt and asyoulik.txt should be named alice20-hadoop.txt and asyoulik20-hadoop.txt respectively.

It  is  recommended  that  you  use  the  UNIX  “tail”  command  and  redirect  the  resulting output to a file to do this. 
For example, $ hadoop fs -cat wordcount/output/* | tail –n 20  > output20.txt

Additional information on shell commands for the filesystem is at: 
http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html

For example, if you want to save the output file in HDFS to the local filesystem, you can use the command:
hadoop fs –get /user/cloudera/wordcount/output/part-00000 MY_LOCAL_DIRHere MY_LOCAL_DIR is the path to the directory where you want to save the file.

5.If  you  are  unfamiliar  with  UNIX,  it  is  strongly recommended  that  you  work  through the UNIX tutorial at http://www.ee.surrey.ac.uk/Teaching/Unix/

------------------------------------------------------------------------------------------------------------------------

Now, try on AWS EMR instance:

1. Once you are able to log in, please modify the WordCount program so it is not case sensitive, that is, it treats all words as being lowercase. 
Call this new program WordCountCaseInsensitive.java. You can refer to the link:https://www.cloudera.com/documentation/other/tutorial/CDH5/topics/ht_wordcount2.html

2. Next  modify  WordCountCaseInsensitive.java  to  incorporate  a  combiner  function  that runs on the map output. 

3. Run  WordCountCaseInsensitive  on  the  alice29.txt  input  file  and  then  on  the  asyoulik.txt input file.

4. Save  the  last  20  lines  of  output  from  WordCount  for  each  of  the  two  input  files.  The  output  files  (each  consisting  of  the  last  20  lines  of  output)  corresponding  to  the  input  files  alice29.txt  and  asyoulik.txt  should  be  named  alice20-hadoop-ci.txt and asyoulik20-hadoop-ci.txt respectively.
