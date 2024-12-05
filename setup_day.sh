set -euo pipefail

if [ "$#" -ne 1 ]
then
  echo "One argument required"
  echo "Usage: ./setup_day.sh <DAY_NUMBER>"
  exit 1
fi

year="2024"
day=$1

echo "Creating files for day $day"

padded_day=$(printf "%02d" ${day})

sed -e "s/{{PADDED_DAY}}/${padded_day}/g" -e "s/{{YEAR}}/${year}/g" template/main_template.txt > main/year${year}/day_"${padded_day}".py

sed -e "s/{{PADDED_DAY}}/${padded_day}/g" -e "s/{{YEAR}}/${year}/g" template/test_template.txt > tests/year${year}/day_"${padded_day}"_test.py

touch tests/year${year}/resources/day"${padded_day}".txt

session=$(<.session)
curl --cookie "session=${session}" https://adventofcode.com/${year}/day/${day}/input -o main/year${year}/resources/day${padded_day}-01.txt

echo "Successfully created files"
