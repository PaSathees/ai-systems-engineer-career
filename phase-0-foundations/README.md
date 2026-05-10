# Phase 0 — Foundations Refresh

A 1–2 week speed-refresh of Python, TypeScript, Git, SQL, Linux/shell, and DS&A before starting the advanced backend work. The goal isn't to re-learn — it's to shake the rust off the parts I'll lean on daily.

---

## Checklist

### Python
- [ ] Skim modern Python idioms — comprehensions, walrus, unpacking, dataclasses, type hints
- [ ] Write a small async script (fetch 3 APIs concurrently with `asyncio.gather`)
- [ ] Set up a clean project skeleton — `uv` or `poetry` + `ruff` + `mypy --strict`

### TypeScript
- [ ] Generics + utility types — `Partial`, `Pick`, `Omit`, `Record`, `ReturnType`, `Awaited`
- [ ] Discriminated unions and narrowing
- [ ] Async patterns — `Promise.all`, `Promise.allSettled`, async iterators
- [ ] Build a typed `fetchJson<T>` helper

### Git
- [ ] Interactive rebase — squash, fixup, reorder
- [ ] Cherry-pick + reflog
- [ ] Stash, worktrees, partial commits (`git add -p`)

### SQL / PostgreSQL
- [ ] Joins — INNER, LEFT, FULL, lateral
- [ ] Indexes — B-tree, GIN, GiST, partial, covering
- [ ] Transactions + isolation levels
- [ ] `EXPLAIN ANALYZE` — read query plans, fix a slow query with the right index
- [ ] CTEs + window functions

### Linux & shell
- [ ] Processes, signals, file descriptors — `ps`, `kill`, `/proc/<pid>/fd`, SIGTERM vs SIGKILL
- [ ] Defensive bash — `set -euo pipefail`, `trap`, exit codes, pipes & redirection
- [ ] `awk` / `sed` / `xargs` / `jq` one-liners on real log files
- [ ] Networking — TCP vs UDP, DNS lookup chain, `curl -v`, `dig`, `ss -tnp`
- [ ] Daily tools — `htop`, `lsof`, `find`, `rsync`, `~/.ssh/config`

### DS&A (light pass)
- [ ] Arrays + hashmaps (NeetCode 75 — Arrays section)
- [ ] Two pointers + sliding window
- [ ] Trees + graphs (BFS / DFS templates)
- [ ] Big-O sanity refresher

---

## Resources I'm using

**Books (O'Reilly):**
- *Fluent Python, 2nd ed.* — Luciano Ramalho (selective: Ch 5, 8, 9, 15, 17, 21)
- *Learning TypeScript* — Josh Goldberg

**Free:**
- [Real Python — async crash course](https://realpython.com/async-io-python/)
- [TypeScript Handbook — utility types](https://www.typescriptlang.org/docs/handbook/utility-types.html)
- [learngitbranching.js.org](https://learngitbranching.js.org)
- [use-the-index-luke.com](https://use-the-index-luke.com)
- [NeetCode 75](https://neetcode.io/practice)

---

## Folders (filled as I go)

- `notes/` — short write-ups on what clicked or surprised me
- `code/` — small scripts and skeletons (async fetch, typed fetch helper, slow-query fix)
- `posts.md` — index of the blog + LinkedIn posts I publish from this phase

---

## Exit criteria

I move to Phase 1 when, in this same week, I have:
1. Written async Python comfortably
2. Written a typed TS function with generics
3. Squashed and rebased a real branch
4. Run `EXPLAIN ANALYZE` on a real query and fixed it with an index
5. Written a defensive bash script and used `strace` / `lsof` / `ss` to inspect a real process
6. Solved a medium DS&A problem from memory
