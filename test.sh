#!/bin/bash

set -ex
python test.py
python family_tree.py test-input > /tmp/tmp-output
diff test-output /tmp/tmp-output || exit -1