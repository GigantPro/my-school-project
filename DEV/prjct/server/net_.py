import socket
from threading import Thread
from db import DB
import time
import random


class Net:
    def __init__(self, PORT=48555, HOST='') -> None:
        self._PORT = PORT
        if HOST:
            self._HOST = HOST
        else:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                try:
                    s.connect(("8.8.8.8", 80))
                    self._HOST = s.getsockname()[0]
                except:
                    print('ERROR: Нет подключение к интернету. Повторная попытка через 5 сек.')
                    time.sleep(5)
                    self.__init__(PORT=PORT, HOST=HOST)
                    return
        
        self.db = DB('db.db')

        self.start_server()

    
    def start_server(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self._HOST, self._PORT))
        Thread(target=self.get_requests).start()
        print('Прослушивание запущено:', f'{self._HOST}:{self._PORT}')
        # sock.listen()
        # conn, addr = sock.accept()

        # print('connected:', addr)

        # while True:
        #     data = conn.recv(1024)
        #     if not data:
        #         break
        #     conn.send(data.upper())

        # conn.close()
    
    # def _generate_person_key(self, _len=10, chars=True):
    #     symb = []
    #     if chars:
            

    '''
    Ключи обращений:
    I-init ()
    L-login ()
    '''

    def get_requests(self):
        self.stop_get_reguests = True
        while self.stop_get_reguests != False:
            person = {}
            a = self.sock.recvfrom(1024)
            a = (a[0].decode("utf-8"), a[1])
            # print(a, type(a))
            # print(str(a[0]), type(str(a[0])))
            if a[0][0] == 'I':
                person['macaddr'] = a[0].split('\r')[1]
                person['version'] = a[0].split('\r')[2]
                # person['temp_id'] = a[0].split('\r')[3]
                db_line = self.db.read_line('pc', 'macaddr', person['macaddr'])
                if not db_line:
                    self.db.add_value('pc', person['macaddr'], person['version'], None, None)
                elif db_line[1] != person['version']:
                    self.db.update_value('pc', 'macaddr', person['macaddr'], 'version', person['version'])
            elif a[0][0] == 'L':
                person['macaddr'] = a[0].split('\r')[1]
                accaunt = self.db.read_line('accaunts', 'login', person['accaunt'])

                if accaunt[2] == a[0].split('\r')[3]:
                    person['accaunt']   = a[0].split('\r')[2]
                    person['passhash']  = a[0].split('\r')[3]
                    self.sock.send(b'Ok')
                else:
                    self.sock.send(b'Err')

                db_line = self.db.read_line('pc', 'macaddr', person['macaddr'])

            print(person)

    
Net() #ldap