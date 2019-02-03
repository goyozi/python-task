from io import StringIO
from os import remove

from pytest import fixture

from load import config, execute_query, load


config['database'] = 'test.db'


@fixture(autouse=True)
def cleanup():
    yield
    remove('test.db')


def test_output_for_empty_file():
    io = StringIO()

    load('examples/empty.csv', io)

    assert io.getvalue() == ('Records inserted: 0\n'
                             'Total records: 0\n')


def test_rows_after_empty_file():
    load('examples/empty.csv')

    rows = execute_query('SELECT * FROM people')

    assert rows == []


def test_output_for_first_file():
    io = StringIO()

    load('examples/people1.csv', io)

    assert io.getvalue() == ('Records inserted: 2\n'
                             'Total records: 2\n')


def test_rows_after_first_file():
    load('examples/people1.csv')

    rows = execute_query('SELECT * FROM people')

    assert rows == [('John Doe', 22, '34523'),
                    ('Jane Doe', 20, '34523')]


def test_output_for_subsequent_file():
    io = StringIO()

    load('examples/people1.csv', StringIO())
    load('examples/people2.csv', io)

    assert io.getvalue() == ('Records inserted: 3\n'
                             'Total records: 5\n')


def test_rows_after_subsequent_file():
    load('examples/people1.csv')
    load('examples/people2.csv')

    rows = execute_query('SELECT * FROM people')

    assert rows == [('John Doe', 22, '34523'),
                    ('Jane Doe', 20, '34523'),
                    ('Mike Bike', 33, '54435'),
                    ('Max Fax', 45, '54663'),
                    ('Roy Ploy', 23, '34551')]
