unalias -a

python3 -m unittest src/Config.py

test "$(python3 src/Config.py "Paths" "datad")" = "./data"
echo "CommandLine test result: $?"
