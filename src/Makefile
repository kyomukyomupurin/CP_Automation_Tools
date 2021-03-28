CC = g++-10
CFLAGS = -std=c++20 -O1 -DLOCAL -fsplit-stack
PYTHON = python3.9
DIR = $(shell basename $(CURDIR))

task$(DIR): task$(DIR).cc
	$(CC) $(CFLAGS) task$(DIR).cc -o task$(DIR)

test:
	@make -s task$(DIR)
	@$(PYTHON) ./../../sample_checker.py