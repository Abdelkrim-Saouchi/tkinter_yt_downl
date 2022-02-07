# Simple Youtube Downloader by Tkinter:
This is a simple youtube's videos downloader by using python, tkinter and "pytube" library.

## Install pytube:
to use this code, you need to install pytube libray in your local machine by typing these commands in your terminal:

`pip install pytube`

Or

`pip install git+https://github.com/pytube/pytube`

## Something important you need to known:
Recently there is a major issue with pytube. When you run this code you will may be face this Error:
`'NoneType: object has no attribute span'`
It has a temporary fix by modefying 'cipher.py' file, go to the folder where you installed python (x for python version release) :

`PATH to python folder...\Python\Python3x\Lib\site-packages\pytube` 

then open the file "cipher.py" and on the line 293 change this code: `'name = re.escape(get_throttling_function_name(js))'` to this code: `'name = "hha"'`.

Remember! this is a temporary fix, it will stop working at anytime so try find a fix on github or stuckoverflow if this solution did not work for you.
