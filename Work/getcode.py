# Получение смс-кода по номеру ID потенциальной сделки

import psycopg2

def getcode(id):
    connection = psycopg2.connect(dbname='bpmn',
                                  host='192.168.205.30',
                                  user='nikolay',
                                  password='gjdpim2{E3#j',
                                  port=5000)

    cur = connection.cursor()

    cur.execute(f"select s.id, s.phone_number, s.code, s.send_time from bpmn.sms_codes s LEFT JOIN bpmn.potential_deal d on s.id = d.code_id WHERE d.id = {id}")

    code = cur.fetchone()

    code = int(code[2])

    connection.close()

    return code
