# Author: Dhananjay Arora
# Usage: spark-submit pagerank.py <inputdatafile>
# Example usage: spark-submit pagerank.py wiki.txt

from operator import add
import sys
import re
from pyspark import SparkContext
from pyspark import SparkConf, SparkContext

"""Parses an entry in a line into title and outlinks."""
def parsePages(page):
	title = re.findall(r'<title>(.*?)</title>', page)
	outlinks = re.findall(r'\[\[([^]]*)\]\]', page)
	return title[0],outlinks

"Computes contributions of pages pointing to the current page"
def computeContributions(pages, pageRank):
	count = len(pages)
	for page in pages:
		yield(page, pageRank / count)

#initialize Spark Context
sc = SparkContext(appName = "WikiPageRank")

#build RDD from the input file (input as an argument)
#lines = sc.textFile(sys.argv[1])
import os
data_path = os.getcwd()
lines = sc.textFile('file:///'+os.path.join(data_path,'graph2.txt'))
#lines = sc.textFile("graph2.txt").
#lines = sc.textFile("simplewiki-20150901-pages-articles-processed.xml")

#count nr of documents in a corpus
count = lines.count()

#lines.collect()

#parse file
#apply map transformation and lambda function on each line to parse a page
#links = list(K,V), where K=title, V = outgoing links
links = lines.map(lambda e: parsePages(e))
print(links.collect())
print('####################')
#initialize rank for each page with 1/N, where N- total nr of pages in corpus
pageRanks = links.map(lambda link: (link[0], 1/float(count)))

#checkresults
print(pageRanks.collect())
print('####################')

#iteratively calculate page rank
for iteration in range(1):
	#combine links and page ranks
	#links.join(pageRanks).collect()
	#calculate contributions, x[1][0] is a list of outlinks, x[1][1] is pageRank
	joined = links.join(pageRanks)
	print(joined.collect())
	print('####################')
	contributions = links.join(pageRanks).flatMap(lambda x: computeContributions(x[1][0], x[1][1]))
	print(contributions.collect())
	print('####################')
	#sum all the scores for a page with a forumla with dumping factor
	pageRanks = contributions.reduceByKey(add).mapValues(lambda rank: 0.15 + 0.85 * rank)
	
#check results
print(pageRanks.collect())
print('####################')
#save results
#pageRanks.saveAsTextFile("results.txt")

#do the sorting
pageRanksOrdered = pageRanks.takeOrdered(100, key = lambda x: -x[1])

count =1
for link,rank  in pageRanksOrdered:
    print("Title: %s Rank: %s" % (link, rank))
#pageRanksOrderedRDD = sc.parallelize(pageRanksOrdered)
#pageRanksOrderedRDD.saveAsTextFile("pageRanks_wiki")

sc.stop()
