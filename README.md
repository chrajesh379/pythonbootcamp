# pythonbootcamp

Installation steps:
Spark:
	Download Spark :https://spark.apache.org/downloads.html
	Extract to C:/spark folder and copy the Path to PATH variable in environment variables. Create this path as SPARK_HOME
	
	Add Environment Variables:
	PYTHON_HOME: C:\spark\python\
	SPARK_HOME: C:\spark
	PYSPARK_PYTHON: py
	Add below values into existing Path Variable:
	C:\Program Files\Java\jdk-1.8 ( SDK Location)
	%JAVA_HOME%\bin
	%SPARK_HOME%\bin
	%SPARK_HOME%\python
Python:
	Download and install Python: https://www.python.org/downloads/
	
Hadoop:
	Copy winutils.exe file to C:\winutils\bin (Create it)
	Add Environment Variables:
	HADOOP_HOME : C:\winutils

pip install pyspark

pip install pytz

pip install PyYaml

pip install urllib3

pip install requests
pip install google-cloud-bigquery
pip install google-cloud-storage
pip install google-cloud-secret-manager
pip install pandas
pip install -U scikit-learn
