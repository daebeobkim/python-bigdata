from pyspark import SparkContext

sc = SparkContext("local", "WordCount")
data = ["Hello Spark", "Hello PySpark", "Spark is awesome"]
rdd = sc.parallelize(data)

word_counts = rdd.flatMap(lambda x: x.split()) \
                .map(lambda word: (word, 1)) \
                .reduceByKey(lambda a, b: a + b)

word_counts.collect()