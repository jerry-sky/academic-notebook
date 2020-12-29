
all:
	printf '#!/bin/bash\n\nif [ ! $$(command -v pypy3) ]; then\n  >&2 printf "\\033[0;31mpypy3 not installed! \\033[7m Performance is greatly decreased! \\033[0;31m Consider installing pypy3.\\033[0m\\n"\n  python3 ./main.py\nelse\n  pypy3 ./main.py\nfi\n' > ./main
	chmod +x ./main

python3:
	printf '#!/bin/bash\n\npython3 ./main.py\n' > ./main
	chmod +x ./main

clean:
	rm -rf ./main
