import nlu
import os
import findspark as fs
fs.init()

os.environ["JAVA_HOME"] = "C:/'Program Files'/Java/jdk-19"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]
os.environ['HADOOP_HOME'] = "C:/winutils"
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = "--master mymaster --total-executor 2 --conf" \
                                    " spark.driver.extraJavaOptions=-Dhttp.proxyHost=proxy.mycorp.com-Dhttp.proxyPort=1234 -Dhttp.nonProxyHosts=localhost|.mycorp.com|127.0.0.1 -Dhttps.proxyHost=proxy.mycorp.com -Dhttps.proxyPort=1234 -Dhttps.nonProxyHosts=localhost|.mycorp.com|127.0.0.1 pyspark-shell"

def embedding(query):
    embeddings_df = nlu.load('en.embed_sentence.bert_base_uncased').predict(query, output_level='sentence')
    return embeddings_df


print(embedding("breast cancer"))
