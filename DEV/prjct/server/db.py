import sqlite3


class DB:
    def __init__(self, base_name: str) -> None:
        self.base = sqlite3.connect(base_name, check_same_thread=False)
        self.cur = self.base.cursor()
        if not self.base:
            raise ConnectionError('Error to connection DB')
    

    def create_table(self, name: str, *arg) -> None:
        self.base.execute('CREATE TABLE IF NOT EXISTS {}({})'.format(name, ', '.join(arg)))
        self.base.commit()

    
    def add_value(self, tabel_name: str, *values) -> None:
        self.cur.execute('INSERT INTO {} VALUES({})'.format(tabel_name, ', '.join(['?' for _ in range(len(values))])), tuple(values))
        self.base.commit()


    def read_all_from_table(self, tabel_name: str) -> list:
        return self.base.execute(f"SELECT * FROM {tabel_name}").fetchall()


    def read_line(self, tabel_name: str, colum_name: str, value: str):
        return self.base.execute("SELECT * FROM {} WHERE {} == ?".format(tabel_name, colum_name), (value,)).fetchone()

    
    def read_lines(self, tabel_name: str, colum_name: str, value: str):
        return self.base.execute("SELECT * FROM {} WHERE {} == ?".format(tabel_name, colum_name), (value,)).fetchall()

    
    def update_value(self, tabel_name: str, flag_value: str, colum_flag_name: str, new_value: str, colum_new_name: str) -> None:
        self.cur.execute('UPDATE {} SET {} == ? WHERE {} == ?'.format(tabel_name, colum_new_name, colum_flag_name), (new_value, flag_value))
        self.base.commit()

    
    def delete_line(self, table_name: str, flag_colum_name: str, flag_value: str) -> None:
        self.cur.execute('DELETE FROM {} WHERE {} == ?'.format(table_name, flag_colum_name), (flag_value,))
        self.base.commit()