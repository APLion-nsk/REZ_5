# REZ_5
Решение тестового задания на практику REZ_5

1. После вызова 'objdump -d /bin/grep | grep "malloc" | wc -l' понимаем, что malloc содержится в 21 инструкции

2. Файл main.py получает на вход .class файл, дезассемблирует его, после чего методично ищет все имена классов во всех строках, содержащих invokevirtual.
На выходе получается множество всех упомянутых классов без повторений.
Применение 'python3 main.py Main.class'
