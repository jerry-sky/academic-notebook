
all:
	printf '#!/bin/bash\nif [ ! $$(command -v pypy3) ]; then\n >&2 printf "\\033[0;31mpypy3 not installed! \\033[7m Performance is greatly decreased! \\033[0;31m Consider installing pypy3.\\033[0m\\n"\n fi\n pypy3 ./main.py 2> /dev/null || python3 ./main.py\n' > ./main
	chmod +x ./main

python3:
	printf 'python3 ./main.py' > ./main
	chmod +x ./main

clean:
	rm -rf ./main
