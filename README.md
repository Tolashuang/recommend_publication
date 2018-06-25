# recommend_publication
recommend_publication_project
基于知识图谱的出版物检索推荐系统设计思路及使用说明
    1.【系统的框架及查询库】
       Apache
             http://www.apache.org/
       SPASPARQL Wrapper (Python)
	     https://rdflib.github.io/sparqlwrapper/
       FLASK
	     https://pypi.org/project/Flask/1.0.2/
       lasticsearch
	     https://www.elastic.co/products/elasticsearch
    2.【系统设计思路】
        -->通过框架搭建一个轻型WEB表单
        -->调用SPASPARQL Wrapper 库，通过SPARQL查询语句在DBpedia进行出版物查询
        -->将查询结果结构化写入html文件
        -->打开html结果文件完成出版物信息显示及相关出版物的推荐
    3.【使用说明】
        运行程序后，输入想要检索的出版物，提交后，将会返回从知识图谱中查找到的结果并显示。
        同时推荐的出版物也将一同在浏览器中打开显示。

