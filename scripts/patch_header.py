#!/usr/bin/env python3
from pathlib import Path

OLD = '''    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
      <div class="flex items-center gap-3 min-w-0">
        <div class="w-10 h-10 rounded-xl bg-amber-500/15 border border-amber-500/30 flex items-center justify-center text-2xl shrink-0">🚌</div>
        <div class="min-w-0">
          <h1 class="text-lg sm:text-xl font-bold tracking-tight truncate">巴士到站</h1>
          <p id="clockTime" class="text-2xl sm:text-3xl font-bold tabular-nums tracking-tight leading-tight">--:--:--</p>
          <p id="lastUpdated" class="text-slate-400 text-sm truncate">載入中…</p>
        </div>
      </div>

      <div id="weatherWidget" class="flex items-center gap-3 px-4 py-2 rounded-2xl bg-slate-800/60 border border-slate-600/40 shrink-0">
        <span id="weatherEmoji" class="text-3xl">—</span>
        <div class="text-right">
          <div class="flex items-baseline gap-1">
            <span id="weatherTemp" class="text-2xl sm:text-3xl font-bold tabular-nums">--</span>
            <span class="text-slate-400 text-sm">°C</span>
          </div>
          <p id="weatherFeels" class="text-slate-400 text-xs">體感 --°C</p>
        </div>
      </div>

      <div class="flex items-center gap-2 shrink-0">
        <button id="btnRefresh" type="button" class="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-slate-700/80 hover:bg-slate-600 border border-slate-500/50 text-base font-medium transition active:scale-95" aria-label="手動更新">
          <svg id="refreshIcon" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
          <span class="hidden sm:inline">更新</span>
        </button>
        <button id="btnAddStop" type="button" class="px-4 py-2.5 rounded-xl bg-amber-600/90 hover:bg-amber-500 text-base font-semibold transition active:scale-95">+ 巴士</button>
      </div>
    </div>'''

NEW = '''    <div class="max-w-7xl mx-auto grid grid-cols-3 items-center gap-2 sm:gap-4">
      <!-- 左上：天氣 -->
      <div id="weatherWidget" class="justify-self-start flex items-center gap-2 sm:gap-3 px-2 sm:px-4 py-1.5 sm:py-2 rounded-2xl bg-slate-800/60 border border-slate-600/40 min-w-0">
        <span id="weatherEmoji" class="text-2xl sm:text-3xl shrink-0">—</span>
        <div class="min-w-0">
          <div class="flex items-baseline gap-0.5">
            <span id="weatherTemp" class="text-xl sm:text-2xl font-bold tabular-nums">--</span>
            <span class="text-slate-400 text-xs sm:text-sm">°C</span>
          </div>
          <p id="weatherFeels" class="text-slate-400 text-[10px] sm:text-xs truncate">體感 --°C</p>
        </div>
      </div>

      <!-- 中間：App 名 -->
      <div class="justify-self-center text-center min-w-0 px-1">
        <h1 class="text-lg sm:text-2xl font-bold tracking-tight whitespace-nowrap">🚌 巴士到站</h1>
      </div>

      <!-- 右上：時間 + 操作 -->
      <div class="justify-self-end text-right min-w-0">
        <p id="clockTime" class="text-xl sm:text-3xl font-bold tabular-nums tracking-tight leading-tight">--:--:--</p>
        <p id="lastUpdated" class="text-slate-400 text-[10px] sm:text-xs truncate max-w-[9rem] sm:max-w-none ml-auto">載入中…</p>
        <div class="flex items-center justify-end gap-1.5 sm:gap-2 mt-1.5">
          <button id="btnRefresh" type="button" class="flex items-center gap-1 px-2.5 sm:px-4 py-1.5 sm:py-2 rounded-xl bg-slate-700/80 hover:bg-slate-600 border border-slate-500/50 text-sm sm:text-base font-medium transition active:scale-95" aria-label="手動更新">
            <svg id="refreshIcon" class="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
            <span class="hidden sm:inline">更新</span>
          </button>
          <button id="btnAddStop" type="button" class="px-2.5 sm:px-4 py-1.5 sm:py-2 rounded-xl bg-amber-600/90 hover:bg-amber-500 text-sm sm:text-base font-semibold transition active:scale-95 whitespace-nowrap">+ 巴士</button>
        </div>
      </div>
    </div>'''


def main():
    path = Path('index.html')
    html = path.read_text(encoding='utf-8')
    if OLD not in html:
        if 'grid grid-cols-3' in html:
            print('header already patched')
            return
        raise SystemExit('header block not found')
    path.write_text(html.replace(OLD, NEW), encoding='utf-8')
    print('patched', path.stat().st_size)


if __name__ == '__main__':
    main()
