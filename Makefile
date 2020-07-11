query:
	cat generate_query.py | \
	python3 -c "import sys, re; print('\n'.join(re.findall(r'^query ([a-zA-Z]+)[ \(]', sys.stdin.read(), flags=re.M)))" | \
	peco | xargs python3 generate_query.py | \
	curl -X POST -H "Authorization: bearer `cat .secrets`" https://api.github.com/graphql -d @- | \
	python3 -m json.tool

