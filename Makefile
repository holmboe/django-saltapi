help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean           remove temporary files created by build tools"
	@echo "  dist            make a source distribution"

clean:
	find . -type f -name MANIFEST -delete
	find . -path "./dist/*" -delete
	find . -path "./build/*" -delete
	find . -path "./*.egg-info" -print0 | xargs -0 rm -rf 
	find . -name '*.py[co]' -delete

dist:
	python setup.py sdist

install:
	python setup.py install

editable:
	pip install -e .
