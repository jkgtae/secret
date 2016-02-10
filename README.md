
## Programming Exercise

You are given a function 'secret()' that accepts a single integer parameter and returns an integer. In your favorite programming language, write a command-line program that takes one command-line argument (a number) and determines if the secret() function is additive [secret(x+y) = secret(x) + secret(y)], for all combinations x and y, where x and y are all prime numbers less than the number passed via the command-line argument. Describe how to run your examples. Please generate the list of primes without using built-in functionality.


## Running the Command Line Program

Built in Python 2.7.

To run the command line program:

`$ python secret.py`

To run tests:

`$ python test_secret.py`


## Versions of secret()

Two examples of a secret() function are provided: one which is additive (`secret(n) = n`), and one which is non-additive (`secret(n) = n^2`). You can toggle between these two functions by commenting/uncommenting lines 98-99 in secret.py:

```python
is_secret_additive(secret_additive)
# is_secret_additive(secret_non_additive)
```

## Examples

The following examples assume you are using the additive version of secret. Each of the examples is also included as a test case.

### Integer or Float Input

```bash
$ python secret.py
Please input a number: 20
Secret is additive
```

```bash
$ python secret.py
Please input a number: 7.6
Secret is additive
```

### Invalid Input

```bash
$ python secret.py
Please input a number: foo
You must input a number
```

### Valid Input, but Number is Too Small

```bash
$ python secret.py
Please input a number: 3
Cannot determine if secret is additive; there is only one prime less than 3
```

```bash
$ python secret.py
Please input a number: -10
Cannot determine if secret is additive; there are no primes less than -10
```

## Viewing Primes Being Checked

To view which combinations of primes are checked to determine whether secret is additive or non-additive, uncomment line 88 in secret.py:

```python
print 'Checking primes %s and %s' % (x, y)
```

which will result in:

```bash
$ python secret.py
Please input a number: 10
Checking primes 2 and 3
Checking primes 2 and 5
Checking primes 2 and 7
Checking primes 3 and 5
Checking primes 3 and 7
Checking primes 5 and 7
Secret is additive
```