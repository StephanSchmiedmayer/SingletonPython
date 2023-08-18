# WIP Singleton

## About the project

A clean, transparent and easy to use python singleton wrapper.

## Installation

`pip install better-singleton`

## Usage

Singleton definition:

```python
from better_singleton import singleton

@singleton
class Counter:
    def __init__(self, initial_counter):
        self.counter = initial_counter

    def inc(self):
        self.counter += 1
```

Usage:

```python
counter1 = Counter(1)
counter1.inc()
counter2 = Counter(1)
print(counter2.counter)
# >>> 2
```

Ensures that at most only one instance of the class exists at any point in time.
`__init__` and `__new__` of the original class get called only once: the first time
an instance is created. This instance will from then on be the singleton instance.
Every following call to the constructor of the wrapped class returns the singleton instance.

The wrapped class cannot have a class variable called `_singleton` as that stores
the singleton instance. This will throw an error before execution begins.

Not thread safe during first initialization.

## Roadmap

## Contributing

### Publish

1. Bump version in [pyproject.toml](pyproject.toml)
2. `poetry update`
3. `poetry build`
4. `poetry publish`

## License

See [License.md](LICENSE.md).

## Contributors

[Stephan Schmiedmayer](https://github.com/stephanschmiedmayer)

## Acknowledgments

Team Incentive Mechanism App Cluster of "Advanced Python Programming Spring 2022"
Nour Bouzid, Yanjie Li, Stephan Schmiedmayer and Leonhard Zirus under supervision of Valentin Zieglmeier
