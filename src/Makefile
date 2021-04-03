CC = g++-10
CFLAGS = -std=c++20 -O1 -DLOCAL -fsplit-stack
PYTHON = python3.9
DIR = $(shell basename $(CURDIR))

run: task$(DIR).cc
	$(CC) $(CFLAGS) task$(DIR).cc -o task$(DIR)

test:
	@make -s run
	@$(PYTHON) ./../../sample_checker.py

submit:
	@$(PYTHON) ./../../submit.py