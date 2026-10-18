#!/usr/bin/env bash
# Run inside the dedicated Linux lab container; no unrelated files are touched.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
set -x
pwd
ls -la
mkdir -p app scripts config logs backup
touch logs/application.log
cat > logs/application.log <<'LOG'
INFO Application started
INFO User logged in
WARNING Configuration file missing
INFO Database connected
ERROR Database connection failed
INFO Application restarted
WARNING Memory usage is high
INFO Request received
ERROR Request failed
INFO Application stopped
LOG
cp Tajibayev_Assylbek_info.txt backup/student_copy.txt
mv backup/student_copy.txt backup/student_moved.txt
cat backup/student_moved.txt
rm backup/student_moved.txt
head -n 3 logs/application.log
tail -n 5 logs/application.log
find . -name application.log
grep ERROR logs/application.log
grep WARNING logs/application.log
grep -c ERROR logs/application.log
printf 'Owner-only lab sample\n' > private.txt
chmod 600 private.txt
chmod 644 public.txt
ls -l private.txt public.txt
chmod +x scripts/Tajibayev_Assylbek_system.sh
./scripts/Tajibayev_Assylbek_system.sh
ps
ps aux
top -b -n 1 | head -n 15
