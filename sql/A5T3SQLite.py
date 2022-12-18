 
import csv, sqlite3


def main():
    conn = sqlite3.connect("A5.db")
    cur = conn.cursor()
    cur.execute("select count(listings.id),host_id from listings group by host_id order by host_id DESC")

    print(cur.fetchmany(10))

if __name__ == '__main__':
    main() 
