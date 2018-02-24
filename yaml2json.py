#!/usr/bin/env python3
# Copyright 2018 lastmind4

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# convert yaml to json
# pip3 install pyyaml
# http://pyyaml.org/wiki/PyYAMLDocumentation
# python3 yaml2json.py < ~/code/manpow/homeland/heartland/puphpet/config.yaml
# or just
# ./yaml2json.py < test.yaml
# original gist https://gist.github.com/noahcoad/51934724e0896184a2340217b383af73

import yaml, json, sys
sys.stdout.write(json.dumps(yaml.load(sys.stdin), sort_keys=True, indent=2, ensure_ascii=False))
