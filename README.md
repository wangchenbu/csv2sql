# CSV to SQL Converter

一个强大的工具，用于将 CSV 文件转换为 SQL 建表语句和插入语句。支持多种数据库系统。

## 安装

基本安装：
```bash
pip install csv2sql
```

安装特定数据库支持：
```bash
# MySQL 支持
pip install csv2sql[mysql]

# PostgreSQL 支持
pip install csv2sql[postgresql]

# SQLite 支持（默认包含）
pip install csv2sql[sqlite]

# Oracle 支持
pip install csv2sql[oracle]

# Microsoft SQL Server 支持
pip install csv2sql[mssql]
```

## 使用方法

### 命令行使用

```bash
# 基本用法
csv2sql input.csv output.sql

# 指定数据库类型
csv2sql input.csv output.sql --db-type mysql

# 指定表名
csv2sql input.csv output.sql --table-name my_table

# 指定字符集
csv2sql input.csv output.sql --charset utf8mb4
```

### Python API 使用

```python
from csv2sql import CSV2SQL

# 创建转换器实例
converter = CSV2SQL()

# 转换文件
converter.convert_file('input.csv', 'output.sql', 
                      db_type='mysql',
                      table_name='my_table',
                      charset='utf8mb4')

# 或者直接转换字符串
sql = converter.convert_string(csv_content, 
                             db_type='mysql',
                             table_name='my_table',
                             charset='utf8mb4')
```

## 支持的数据库

- MySQL
- PostgreSQL
- SQLite
- Oracle
- Microsoft SQL Server

## 特性

- 自动检测列类型
- 支持多种数据库系统
- 命令行和 Python API 支持
- 可自定义表名和字符集
- 支持大文件处理
- 自动处理特殊字符和转义

## 许可证

MIT License 