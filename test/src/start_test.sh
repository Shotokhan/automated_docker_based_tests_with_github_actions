#!/bin/bash
output=$(pytest test.py)
status=$?
echo "$output" | tee log/test.log
exit $status
