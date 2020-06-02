#!/bin/bash

wget --load-cookies /tmp/cookies-gdrive-download-tmp.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies-gdrive-download-tmp --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1DXsej1M3grZCo9l5O41Jh2jUGpnmCOR5' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1DXsej1M3grZCo9l5O41Jh2jUGpnmCOR5" -O c3725-adventerprisek9-mz.124-15.T14.bin && rm -rf /tmp/cookies-gdrive-download-tmp
