
import csv
import sqlite3


def main():
    conn = sqlite3.connect("A5.db")
    cur = conn.cursor()
    listid = input()
    cur.execute("select host_name,price,max(date) from listings join reviews where listings.id = reviews.listing_id and listing_id = "+ listid)

    print(cur.fetchmany(10))

if __name__ == '__main__':
    main()
