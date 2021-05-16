CC = g++-10
CFLAGS = -std=c++20 -O1 -DLOCAL -fsplit-stack
CFLAGS_RELEASE = -std=c++20 -O2
PYTHON = python3.9
DIR = $(shell basename $(CURDIR))

debug: task$(DIR).cc
	$(CC) $(CFLAGS) task$(DIR).cc -o task$(DIR)

release: task$(DIR).cc
	$(CC) $(CFLAGS_RELEASE) task$(DIR).cc -o task$(DIR)

test:
	@make -s debug
	@$(PYTHON) ./../../sample_checker.py

submit:
	@$(PYTHON) ./../../submit.py

bsubmit:
	@make -s clean
	@make -s release
	@$(PYTHON) ./../../bin.py task$(DIR).cc
	@$(PYTHON) ./../../binary_submit.py

status:
	@$(PYTHON) ./../../status.py

clean:
	@rm -f task$(DIR)