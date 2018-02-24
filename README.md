# prepare env
```
# Use python 3.x
pyenv local 3.6.1

# http://pyyaml.org/wiki/PyYAMLDocumentation
pip3 install pyyaml
```

# usage
## yaml to json
`./yaml2json.py < test/a.yaml`
## json to yaml
`./yaml2json.py < test/a.yaml | ./json2yaml.py -`

# Test case
`./test/run_test.sh`

# Change history
* `yaml2json.py` is forked from gist https://gist.github.com/noahcoad/51934724e0896184a2340217b383af73
* Add json to yaml converting: `json2yaml.py`
* Disable escaping non-ASCII characters, refer https://stackoverflow.com/a/15942362/1145798
