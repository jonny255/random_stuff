#!/usr/bin/env python3
# compression_curses_final.py

import curses
import os
import subprocess
import re
from pathlib import Path

SOURCE_DIR = Path("./Downloads 11,209F 125GB")
MAX_DEPTH = 3
LOGFILE = "compress.log"
DRY_RUN = False
DELETE_AFTER = False

progress_re = re.compile(r'(\d+)%')  # matches "12%" etc.

def list_dirs(base_path, max_depth):
    dirs = []
    for root, subdirs, _ in os.walk(base_path):
        depth = len(Path(root).relative_to(base_path).parts)
        if 1 <= depth <= max_depth:
            dirs.append((depth, Path(root)))
    dirs.sort(reverse=True)
    return [d for _, d in dirs]

def draw_progress(win, y, label, percent, width):
    n_hash = int(percent * width / 100)
    bar = "#" * n_hash + "." * (width - n_hash)
    try:
        win.addstr(y, 0, f"{label:7}: [{percent:3}%] [{bar}]")
        win.clrtoeol()
        win.refresh()
    except curses.error:
        pass

def safe_addstr(win, y, x, text, max_width):
    if len(text) > max_width:
        text = "…" + text[-(max_width-1):]
    try:
        win.addstr(y, x, text)
        win.clrtoeol()
    except curses.error:
        pass

def run_7z_with_progress(cmd, stdscr, bar_y, max_x, processed_bytes_all, total_bytes_all, total_bytes_dir):
    percent_dir = 0
    percent_global = int(processed_bytes_all * 100 / total_bytes_all)

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    for line in proc.stdout:
        m = progress_re.search(line)
        if m:
            percent_dir = int(m.group(1))
            percent_global = int((processed_bytes_all + percent_dir/100 * total_bytes_dir) / total_bytes_all * 100)
            draw_progress(stdscr, bar_y, "Dir", percent_dir, max_x-20)
            draw_progress(stdscr, bar_y+1, "Global", percent_global, max_x-20)
    proc.wait()

    # Final update
    draw_progress(stdscr, bar_y, "Dir", 100, max_x-20)
    percent_global = int((processed_bytes_all + total_bytes_dir) / total_bytes_all * 100)
    draw_progress(stdscr, bar_y+1, "Global", percent_global, max_x-20)

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    log_height = max_y - 3
    log_win = curses.newwin(log_height, max_x, 0, 0)
    bar_y = log_height
    log_lines = []

    dirs = list_dirs(SOURCE_DIR, MAX_DEPTH)
    total_dirs = len(dirs)
    total_bytes_all = sum(sum(f.stat().st_size for f in d.glob('**/*') if f.is_file()) for d in dirs)
    processed_bytes_all = 0

    for idx, dir_path in enumerate(dirs, start=1):
        dir_name = dir_path.name
        out_file = dir_path.with_suffix(".7z")
        total_bytes_dir = sum(f.stat().st_size for f in dir_path.glob('**/*') if f.is_file())

        display_str = f"🔹 Compressing ({idx}/{total_dirs}): {dir_path} → {out_file}"
        log_lines.append(display_str)
        if len(log_lines) > log_height:
            log_lines = log_lines[-log_height:]
        log_win.erase()
        for i, line in enumerate(log_lines):
            safe_addstr(log_win, i, 0, line, max_x)
        log_win.refresh()

        if DRY_RUN:
            percent_dir = 0
            for f in dir_path.glob('**/*'):
                if f.is_file():
                    percent_dir += int(f.stat().st_size * 100 / total_bytes_dir)
                    percent_global = int((processed_bytes_all + percent_dir/100 * total_bytes_dir) / total_bytes_all * 100)
                    draw_progress(stdscr, bar_y, "Dir", min(percent_dir, 100), max_x-20)
                    draw_progress(stdscr, bar_y+1, "Global", percent_global, max_x-20)
            log_lines.append(f"[DRY RUN] Would compress from {dir_path}")
        else:
            cmd = ["7z", "a", "-t7z", "-mx=9", "-mmt", "-bb1", str(out_file), str(dir_path)]
            run_7z_with_progress(cmd, stdscr, bar_y, max_x, processed_bytes_all, total_bytes_all, total_bytes_dir)

        processed_bytes_all += total_bytes_dir
        log_lines.append(f"✅ Done: {out_file}")
        if DELETE_AFTER and not DRY_RUN:
            subprocess.run(["rm", "-rf", str(dir_path)])

        log_win.erase()
        for i, line in enumerate(log_lines[-log_height:]):
            safe_addstr(log_win, i, 0, line, max_x)
        log_win.refresh()

    stdscr.addstr(bar_y+2, 0, f"Compression complete. Log written to '{LOGFILE}'")
    stdscr.clrtoeol()
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
