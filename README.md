# cpy compiler

A compiler for cpy, a small Python-like language, written in Python. I made it together with Michalis Galanakis for the Compilers course (Μεταφραστές) at the Department of Computer Science and Engineering, University of Ioannina, in 2024.

It has the usual phases. The lexer is an automaton with a state transition table. The syntax analyzer asks it for one token at a time, and while it parses it generates the intermediate code (quads) and fills the symbol table (scopes, nesting levels, offsets). There's also the start of a RISC-V back end (`telikos()`), but it isn't finished or called yet, so `assembly.asm` comes out empty.

## Example

One of the functions in the test program:

```python
def fibonacci(x):
#{  global counterFunctionCalls
    counterFunctionCalls = counterFunctionCalls + 1
    if x<=1:
        return x
    else:
        return fibonacci(x-1)+fibonacci(x-2)
#}
```

and the quads the compiler makes for it:

```
1 :  begin_block  fibonacci  _  _
2 :  +  counterFunctionCalls  1  T_1
3 :  :=  T_1  _  counterFunctionCalls
4 :  <=  x  1  6
5 :  jump  _  _  8
6 :  retv  x  _  _
7 :  jump  _  _  18
8 :  -  x  1  T_2
9 :  par  T_2  CV  _
10 :  par  T_3  RET  _
11 :  call  fibonacci  _  _
12 :  -  x  2  T_4
13 :  par  T_4  CV  _
14 :  par  T_5  RET  _
15 :  call  fibonacci  _  _
16 :  +  T_3  T_5  T_6
17 :  retv  T_6  _  _
18 :  end_block  fibonacci  _  _
```

## Running it

The compiler reads `programmaCPY.cpy` from the folder you run it in:

```bash
python3 Compiler.py
```

It writes the quads to `endiamesos.int` and the symbol table to `pinakas_symvolwn.sym`. `programmaCPY.cpy` is a test program with a few functions (fibonacci, a prime check and so on), change it to compile something else.

The report (in Greek) is in [report.pdf](report.pdf).
