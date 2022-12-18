import nlu
import os
import findspark as fs
import pyspark
import sys

from pyspark.sql import SparkSession

sc = pyspark.SparkContext(appName="medical_studies")
fs.init('C:/Users/chant/anaconda3/envs/medical_studies/Lib/site-packages/pyspark/',edit_rc=True, edit_profile=True)
fs.find()

os.environ["JAVA_HOME"] = "C:/'Program Files'/Java/jdk-19"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]
os.environ['HADOOP_HOME'] = "C:/winutils"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
os.environ['PYSPARK_SUBMIT_ARGS'] = "--master mymaster --total-executor 2 --conf" \
                                    " spark.driver.extraJavaOptions=-Dhttp.proxyHost=proxy.mycorp.com-Dhttp.proxyPort=1234 -Dhttp.nonProxyHosts=localhost|.mycorp.com|127.0.0.1 -Dhttps.proxyHost=proxy.mycorp.com -Dhttps.proxyPort=1234 -Dhttps.nonProxyHosts=localhost|.mycorp.com|127.0.0.1 pyspark-shell"

spark = SparkSession.builder \
    .master("local[2]") \
    .appName("Helper Functions Unit Testing") \
    .getOrCreate()

def embedding(query):
    embeddings_df = nlu.load('en.embed_sentence.bert_base_uncased').predict(query, output_level='sentence')
    return embeddings_df


print(embedding("breast cancer"))
