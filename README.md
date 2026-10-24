# cpy compiler

A compiler for cpy, a small Python-like language, written in Python. I made it together with Michalis Galanakis for the Compilers course (Μεταφραστές) at the Department of Computer Science and Engineering, University of Ioannina, in 2024.

It has all the usual parts:

- lexical analyzer, an automaton with a state transition table
- syntax analyzer
- intermediate code (quads)
- symbol table with scopes and nesting levels
- final code in RISC-V assembly

## Running it

The compiler reads `programmaCPY.cpy` from the folder you run it in:

```bash
python3 Compiler.py
```

It writes the intermediate code to `endiamesos.int`, the symbol table to `pinakas_symvolwn.sym` and the assembly to `assembly.asm`. `programmaCPY.cpy` is a test program with a few functions (fibonacci, a prime check and so on), change it to compile something else.

The report (in Greek) is in [report.pdf](report.pdf).
