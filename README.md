# Spam Bot

![PyPI](https://img.shields.io/pypi/v/spam-bot?color=blue)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/spam-bot)
![PyPI - License](https://img.shields.io/pypi/l/spam-bot)

Spam anything!

### Installation

Run this command on terminal
`$ pip install spam-bot`

### How to use

```python
from spam_bot import spam

msg = "Hello World"
msg_count = 500

spam(msg, msg_count)
```

This is is a simple spam-bot program.

If you want to spam things in a specific .txt file, You should use following way

```python
from spam_bot import ReadFile

file = ReadFile("filename.txt")

file.spam()
```

Then, run the program and quickly switch tabs to whatever app you want to spam and select the box to type in.

Then wait 5 senconds.. 5..4..3..2..1

Boom!
