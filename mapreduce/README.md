### access namenode on ```http://namenode:9870```
### access resoucemanager on ```http://resourcemanager:8088```


### Task 1

- add to /etc/hosts
```
#hadoop
127.0.5.1	namenode
127.0.6.1	datanode1
127.0.6.2	datanode2
127.0.6.3	datanode3
127.0.5.2	resourcemanager
127.0.5.3	historyserver
127.0.5.4	nodemanager
```
- ```docker-compose up -d```


### Task 2

- ```docker exec -it datanode1 bash```
- ```hdfs dfs -put <local_data_path> <remote_data_path>```
- ```chmod +x <python_script>``` if needed
- test python scripts
-- ```cat <local_input_path> | <local_python_mapper_path> | <local_python_reducer_path>```
- ```hadoop jar hadoop-streaming-3.3.6.jar -file <local_python_mapper_path> -mapper <local_python_mapper_path> -file <python_reducer> -reducer <local_python_reducer_path> -input <remote_input_path> -output <remote_output_path>```
