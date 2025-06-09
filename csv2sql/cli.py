import click
from .converter import CSV2SQL

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--db-type', '-d', default='mysql',
              type=click.Choice(['mysql', 'postgresql', 'sqlite', 'oracle', 'mssql']),
              help='目标数据库类型')
@click.option('--table-name', '-t', help='表名（默认使用输入文件名）')
@click.option('--charset', '-c', help='字符集（仅 MySQL 和 PostgreSQL 支持）')
def main(input_file: str, output_file: str, db_type: str, 
         table_name: str = None, charset: str = None):
    """将 CSV 文件转换为 SQL 建表语句和插入语句"""
    try:
        converter = CSV2SQL()
        converter.convert_file(
            input_file=input_file,
            output_file=output_file,
            db_type=db_type,
            table_name=table_name,
            charset=charset
        )
        click.echo(f"转换完成！SQL 文件已保存到: {output_file}")
    except Exception as e:
        click.echo(f"错误: {str(e)}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    main() 