# phonenumber-to-roman
Commandline tool to convert phone number to roman and vice versa

## Installation
You must have `python3` installed.

```
$ git clone https://github.com/sandipbgt/phonenumber-to-roman.git
$ cd phonenumber-to-roman
$ sudo pip3 install -r requirements.txt
```

## Screenshot
![https://raw.githubusercontent.com/sandipbgt/phonenumber-to-roman/master/screenshot.png](https://raw.githubusercontent.com/sandipbgt/phonenumber-to-roman/master/screenshot.png)

## Usage

#### To convert to roman number
```
$ ./main.py "9842397364" --roman
IX VIII IV II III IX VII III VI IV    
```

#### To convert to normal number
```
$ ./main.py "IX VIII IV II III IX VII III VI IV" --natural
9842397364
```

## Advanced Usage
```
usage: main.py [-h] [-r | -n] phone

Utility tool to convert phone number to roman and vice versa.

positional arguments:
  phone          Phone number.

optional arguments:
  -h, --help     show this help message and exit
  -r, --roman    Convert phone number to roman number.
  -n, --natural  Convert phone number to natural number.
```

## Contribution
Feel free to create a Github issue. Also, you are more than welcome to submit a pull request for a bug fix or additional feature.