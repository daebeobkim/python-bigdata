import os
from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
"""
SparkConf() : 클래스의 인스턴스를 생성
setMaster("local") : 애플리케이션을 실행할 spark 클러스터의 url을 설정, spark클러스터를 사용하지 않고
로컬 모드로 설정하겠다는 의미
setAppName("RatingsHistogram") : 애플리케이션의 이름설정
"""
sc = SparkContext(conf = conf)

lines = sc.textFile("file:///SparkCourse/ml-100k/u.data")
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue() #데이터분할

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))