'''
● Копирование файлов
Для копирования файлов лучше всего подходит модуль shutil, который предоставляет ряд высокоуровневых операций.
'''

import shutil

shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir/one_more.txt')
