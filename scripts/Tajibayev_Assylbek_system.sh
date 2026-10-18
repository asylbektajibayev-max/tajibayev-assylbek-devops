#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
printf '==============================\nStudent Information\n==============================\n'
printf 'Name: Assylbek\nSurname: Tajibayev\nGroup: IT2-2310\nStudent ID: 38288\n'
printf '\n==============================\nSystem Information\n==============================\n'
printf 'Username: '; whoami
printf 'Hostname: '; hostname
printf 'Current Date: '; date -Is
printf 'Operating System: '; uname -a
printf 'Disk Usage:\n'; df -h /
printf 'Memory Usage:\n'; free -h
if [[ -f "$ROOT/Tajibayev_Assylbek_info.txt" ]]; then
    echo 'Student information file exists.'
else
    echo 'Student information file does not exist.'
fi
