mkdir osint
cd osint
git clone https://github.com/0xbyt3z/osintcrawler.git .
python --version
pip install aiodns
pip install aiohttp
pip install shodan
pip install aiosqlite
pip install netaddr
pip install uvloop
pip install aiomultiprocess
pip install -r requirements/dev.txt
