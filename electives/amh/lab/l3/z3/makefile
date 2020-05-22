
all:
	printf '#!/bin/bash\n\nif [ ! $$(command -v pypy3) ]; then\n  python3 ./main.py\nelse\n  pypy3 ./main.py\nfi\n' > ./main
	chmod +x ./main

python3:
	printf '#!/bin/bash\n\npython3 ./main.py\n' > ./main
	chmod +x ./main

clean:
	rm -rf ./main __pycache__
