# concurrency-in-python-with-asyncio
Изучаем как работает библиотека asyncio, как написать реальное приложение и как использовать функции веб-API 
для повышения производительности, пропускной способности и отзывчивости приложений на языке Python. 
Рассматриваем широкий круг вопросов: от модели однопоточной конкурентности до многопроцессорной обработки.

# Concurrency in Python with Asyncio

Source code to the Manning book *Concurrency in Python with Asyncio*.
https://github.com/concurrency-in-python-with-asyncio

## Running
This code ran successfully with Python version 3.10.2. Using a different version may give you different results or may not work.

**Steps to Run Code Listing**

1. Install Python 3.10.2, installers available at the bottom of the page at: https://www.python.org/downloads/release/python-3102/

2. Create a virtual environment and activate it. Instructions available [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).

3. Install the dependencies for the project by running `pip install -r requirements.txt` within your virtual environment.

3. Several functions are in the `util` module - for this to import properly you need to include this module in your `PYTHONPATH`. You can do this by running `export PYTHONPATH=${PYTHONPATH}:concurrency-in-python-with-asyncio/util` within your terminal, changing `concurrency-in-python-with-asyncio` to whichever path you have cloned this repository on your local machine.

5. You should now be able to run any code listing successfully with `python3 scriptname.py`, for example, `python3 chapter_01/listing_1_1.py` will run the first code listing from the first chapter.


Для импорта функции async_timed из файла async_timer.py, расположенного в папке concurrency-in-python-with-asyncio/util, вам нужно добавить путь к папке concurrency-in-python-with-asyncio в переменную окружения PYTHONPATH в Linux. Это позволит Python найти модуль util.async_timer при выполнении сценария listing_2_18.py.
Вы можете добавить путь к PYTHONPATH перед запуском сценария следующим образом:
bash
	$ export PYTHONPATH=/полный/путь/к/concurrency-in-python-with-asyncio:$PYTHONPATH
	$python3 chapter_2/listing_2_18.py

Замените /полный/путь/к/concurrency-in-python-with-asyncio на фактический полный путь к папке concurrency-in-python-with-asyncio, где находится папка util.
После добавления пути к PYTHONPATH Python сможет корректно импортировать функцию async_timed из async_timer.py в вашем сценарии listing_2_18.py.