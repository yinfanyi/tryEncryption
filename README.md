# tryEncryption
使用需要先安装相关的库
```python
pip install pycryptodome
```
这个库如果用不了，需要更改库所在的文件夹名字，小写改为大写

参考网址：
https://blog.csdn.net/zhinian1204/article/details/124112512?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-124112512-blog-128645685.235%5Ev38%5Epc_relevant_anti_vip_base&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-124112512-blog-128645685.235%5Ev38%5Epc_relevant_anti_vip_base

生成密钥命令：
```python
python script.py generate public_key.pem private_key.pem
```

加密文件：
```python
python script.py encrypt 要加密的文件.txt 加密后的文件.txt
```

解密文件：
```python
python script.py encrypt 加密后的文件.txt 解密后的文件.txt
```
