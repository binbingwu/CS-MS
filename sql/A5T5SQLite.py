
import csv
import sqlite3


def main():
    conn = sqlite3.connect("A5.db")
    cur = conn.cursor()
    neighbourname = input()
    cur.execute("select avg(price) from listings where neighbourhood = " +neighbourname+"group by neighbourhood")

    print(cur.fetchmany(10))

if __name__ == '__main__':
    main()
