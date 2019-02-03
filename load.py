#! /usr/bin/env python

import csv
import sqlite3
import sys

config = {'database': 'example.db'}


def execute_query(query, params=dict()):
    with sqlite3.connect(config['database']) as connection:
        cursor = connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()


def create_table():
    execute_query('''
        CREATE TABLE IF NOT EXISTS people
        (name TEXT, age INT, zipcode TEXT)
    ''')


def save_entry(entry):
    execute_query('''
        INSERT INTO people (name, age, zipcode)
        VALUES (:name, :age, :zipcode)
    ''', entry)


def save_entries(file_path, output):
    inserted = 0

    with open(file_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            save_entry(row)
            inserted += 1

    output.write('Records inserted: ' + str(inserted) + '\n')


def print_total(output):
    total = execute_query('SELECT COUNT(*) FROM people')[0][0]
    output.write('Total records: ' + str(total) + '\n')


def load(file, output=sys.stdout):
    create_table()
    save_entries(file, output)
    print_total(output)


if __name__ == '__main__':
    load(sys.argv[1])
