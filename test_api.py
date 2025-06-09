from csv2sql import CSV2SQL

def test_convert_file():
    converter = CSV2SQL()
    converter.convert_file(
        input_file='custom.csv',
        output_file='employees.db',
        db_type='sqlite',
        table_name='employees'
    )
    print("文件转换完成！")

def test_convert_string():
    converter = CSV2SQL()
    # 从文件读取 CSV 内容
    with open('custom.csv', 'r', encoding='utf-8') as f:
        csv_content = f.read()
    
    sql = converter.convert_string(
        csv_content=csv_content,
        db_type='sqlite',
        table_name='employees'
    )
    print("SQL 输出：")
    print(sql)

if __name__ == '__main__':
    print("测试文件转换...")
    test_convert_file()
    print("\n测试字符串转换...")
    test_convert_string() 