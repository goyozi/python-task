### Setup

The project uses Python 3.7 and [Pipenv](https://pipenv.readthedocs.io/en/latest/) for dependency management. If you don't have Pipenv installed, you can use:

```
pip install pipenv [--user]
```

Once Pipenv is installed, you can install all project dependencies by running:

```
pipenv install --dev
```

To enter a virtualenv shell for the project run:

```
pipenv shell
```

### Running the project

As specified in the "use case", the project can be run by executing:

```
./load.py <some-csv-file>
```

Example using one of the provided files:

```
./load.py examples/people1.csv
```

### Testing the project

Tests are written using [pytest](https://docs.pytest.org/en/latest/contents.html), which you should have already installed if you went through the setup process. To run the tests you just have to run `pytest` in the virtualenv's shell.

### Implementation notes

As (in my experience) this kind of scripts are more often developer utilities than mission critical tools, I opted for the simplest working implementation. In a real world scenario, with known context and constraints, both the implementation and test might look quite different.
