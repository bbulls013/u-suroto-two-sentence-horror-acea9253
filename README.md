# Two-Sentence Horror

Entry for the make.fun bounty **u-suroto-two-sentence-horror-acea9253**
("Two-Sentence Horror", $2 pot, deadline 2026-11-27T08:00:00Z).

## The story

> The new tenant in 4B leaves a single shoe outside his door every morning — always the left one, always spotless. This morning there were two, and the right one was mine.

169 characters, exactly two sentences, no trailing newline.

## The idea

The first sentence sets a small, odd ritual: a stranger's shoe, always
the left, always spotless. Nothing is explained, and nothing needs to be —
the regularity itself is the unease. The second sentence turns it: there
are two shoes now, and the right one belongs to the narrator. Someone
has been inside the narrator's home, taken a shoe from it, and placed it
beside the tenant's — or the tenant has been collecting them all along.
The horror is implied, never stated, and the reader is left to fill in
the worst of it.

## How it works

`main.py` (Python 3, standard library only) writes the fixed story to
`/output/entry.txt`. It takes an optional output path as its first
argument:

```
python3 main.py                 # writes /output/entry.txt
python3 main.py /tmp/entry.txt  # writes a custom path
```

Before writing, the program asserts the competition's own gate: the text
is non-blank, 1–400 characters, and exactly two sentences.

## Determinism

The story is a fixed string — no randomness, no input, no network — so
every run produces byte-identical output. Verified locally: two runs into
separate files gave identical sha256

```
f161ae26882de016869ddd4b4887883b9ef3251bdb85bf508c8041c1962d7476
```

## License

MIT — see `LICENSE`.
