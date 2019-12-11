Ссылка на курс "Автоматизация UI-тестирования на Python" - https://stepik.org/course/58297/syllabus


==============================Linux_OS_Settings==============================
1. Установить python 3.7:

	```bash
	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get install python3.7
	```

2. Установить pip:

	```bash
	python3 -m pip install pip
	```

3. Создать виртуальное окружение:

	```bash
	sudo apt-get install -y python3.7-venv
	mkdir ~/env
	cd ~/env
	python3 -m venv py3
	```

4. Активировать виртуальное окружение:

	```bash
	cd ~/env
	source py3/bin/activate
	```

5. Установить необходимые библиотеки:

	```bash
	pip install -r requirements.txt
	```
	
6. Запуск автотестов из консоли:

	```bash
	pytest -v --tb=line <test_file_name.py>
	```
	
	параметр `--tb=line` - сокращает лог с результатами теста;
	Можно также указать параметр `--reruns N` для перезапуска упавших тестов, где N - количество перезапусков упавших тестов.
	
	В проекте инициализированы следующие маркировки тестов:
	login_guest
	need_review
	need_review_custom_scenarios
	
	Маркировки регистрируются в файле pytest.ini.
	
	Чтобы запустить только тесты с заданной маркировкой, нужно при запуске добавить параметр:
	
	```bash
	-m <marking name>
	```
	
   - Для запуска отдельных тестов добавляется ключ `-k`

	```bash
	-k <test_name>
	```

7. После завершения работы можно деактировать виртуальное окружение:

	```bash
	deactivate
	```

	