mkdir osint
cd osint
git clone https://github.com/osintcrawler.git .
python3 --version
pip3 install aiodns
pip3 install aiohttp
pip3 install shodan
pip3 install aiosqlite
pip3 install netaddr
pip3 install uvloop
pip3 install aiomultiprocess
pip3 install -r requirements/dev.txt
