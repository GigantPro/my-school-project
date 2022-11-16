import sqlite3


class DB:
    def __init__(self, base_name: str) -> None:
        self.base = sqlite3.connect(base_name, check_same_thread=False)
        self.cur = self.base.cursor()
        if not self.base:
            raise ConnectionError('Error to connection DB')
 
    def add_value(self, tabl_n: str, *args) -> None:
        self.cur.execute('INSERT INTO {} VALUES({})'.format(tabl_n, ', '.join(['?' for _ in range(len(args))])), tuple(args))
        self.base.commit()
    
    def create_table(self, name: str, *arg) -> None:
        self.base.execute('CREATE TABLE IF NOT EXISTS {}({})'.format(name, ', '.join(arg)))
        self.base.commit()
 
    def read_all_from_table(self, tabl_n: str) -> list:
        return self.base.execute(f"SELECT * FROM {tabl_n}").fetchall()
 
    def read_lines(self, tabl_n: str, colum_name: str, value: str):
        return self.base.execute("SELECT * FROM {} WHERE {} == ?".format(tabl_n, colum_name), (value,)).fetchall()
 
    def read_line(self, tabl_n: str, colum_name: str, value: str):
        return self.base.execute("SELECT * FROM {} WHERE {} == ?".format(tabl_n, colum_name), (value,)).fetchone()
    
    def delete_line(self, tabl_n: str, fl_colum_name: str, fl_value: str) -> None:
        self.cur.execute('DELETE FROM {} WHERE {} == ?'.format(tabl_n, fl_colum_name), (fl_value,))
        self.base.commit()
    
    def update_value(self, tabl_n: str, fl_value: str, colum_fl_name: str, new_value: str, colum_new_name: str) -> None:
        self.cur.execute('UPDATE {} SET {} == ? WHERE {} == ?'.format(tabl_n, colum_new_name, colum_fl_name), (new_value, fl_value))
        self.base.commit()

db = DB('ex.db')
# db.create_table('mouse', 'id INTEGER', 'value', 'PRIMARY KEY("id" AUTOINCREMENT)')
db.create_table('mouse', 'value')
for i in range(10):
    db.add_value('mouse', None, i)

