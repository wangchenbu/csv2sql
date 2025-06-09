from csv2sql import CSV2SQL

def test_convert_multiple_files():
    converter = CSV2SQL()
    # 可以是文件列表，也可以是通配符字符串
    input_files = ['custom.csv', 'test_data.csv']  # 或 input_files = '*.csv'
    output_file = 'multi_import.db'
    converter.convert_multiple_files(
        input_files=input_files,
        output_file=output_file,
        db_type='sqlite',  # 也可以用'mysql'等
        table_name_pattern='table_{filename}'  # 可选，表名格式
    )
    print("批量导入完成！")

if __name__ == '__main__':
    test_convert_multiple_files()