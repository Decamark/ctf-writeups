#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import subprocess
import sys
import struct

from halo import Halo

class Obj:
  def __init__(self):
    self.iss = []

  def append(self, inst):
    if not self.iss:
      self.iss.append( inst )
      return

    p = self.iss[-1]
    inst.p = p
    p.f = inst
    self.iss.append( inst )

  def find_ret(self, inst, M):
    gadget = []
    curr = inst
    for i in range(M):
      gadget.append( curr )
      if not curr.asm: return []
      if curr.asm.mnem == 'ret':
        return gadget
      if curr.f: curr = curr.f
      else: return []
    return []

  def find_gadget_asm(self, asm, M=5, satisfies=None):
    for inst in self.iss:
      if not asm in repr(inst.asm): continue
      if satisfies and not satisfies(inst): continue
      gadget = self.find_ret(inst, M)
      if gadget: yield gadget

  def find_gadget_code(self, code, M=5, satisfies=None):
    for inst in self.iss:
      if not all(b in inst.code for b in code): continue
      if satisfies and not any(satisfies(inst, b) for b in code): continue
      gadget = self.find_ret(inst, M)
      if gadget: yield gadget

class Inst:
  def __init__(self, n, sec, sym, code, asm):
    self.n    = n
    self.sec  = sec
    self.sym  = sym
    self.code = code
    self.asm  = asm

  def __repr__(self):
    s  = '<Inst'
    s += ' ' + format(self.n, 'x')
    s += ' ' + self.sec
    s += ' ' + self.sym
    s += ' ' + '[' + ', '.join(map(lambda x: format(x, '02x'), self.code)) + ']'
    s += ' ' + repr(self.asm)
    s += '>'
    return s

class Asm:
  mnem = None
  opr1 = None
  opr2 = None
  opr3 = None
  hint = None

  def __init__(self, asm):
    if '<' in asm and '>' in asm:
      l,r = asm.find('<'),asm.find('>')
      self.hint = asm[l+1:r]
      asm = asm[:l]
    pos = asm.find(' ')
    if pos < 0:
      self.mnem = asm
      return
    self.mnem = asm[:pos]
    operands = asm[asm.find(' '):].strip().split(',')
    for opr in operands:
      if not self.opr1: self.opr1 = opr
      elif not self.opr2: self.opr2 = opr
      elif not self.opr3: self.opr3 = opr

  def __repr__(self):
    s = self.mnem
    if self.opr1: s += ' ' + self.opr1
    if self.opr2: s += ',' + self.opr2
    if self.opr3: s += ',' + self.opr3
    if self.hint: s += ' <' + self.hint + '>'
    return s

p = subprocess.run(['objdump', '-D', '-M', 'intel', sys.argv[1]], stdout=subprocess.PIPE)
dump = p.stdout

obj = Obj()
sec = ''
sym = ''

spinner = Halo(text='Parsing', spinner='dots')
spinner.start()
for line in dump.split(b'\n'):
  tabn = line.count(b'\t')
  if tabn == 0:
    if b'Disassembly of section' in line:
      sec = line.split()[-1][:-1].decode('utf-8')
    elif b'<' in line and b'>' in line:
      sym = line[ line.find(b'<')+1 : line.find(b'>') ].decode('utf-8')
    elif b'file format' in line:
      continue
    elif line == b'':
      continue
    else:
      raise Exception('Unknown pattern:\n  ' + str(line))
  if tabn > 0:
    if line == b'\t...': continue
    if tabn == 1:
      n,code = line.split(b'\t')
      asm = None
    elif tabn == 2:
      n,code,asm = line.split(b'\t')
      asm = asm.decode('utf-8')
      asm = Asm(asm)

    n = int(n.strip()[:-1], 16)
    code = [int(h, 16) for h in code.split()]
    inst = Inst(n, sec, sym, code, asm)
    obj.append(inst)
spinner.succeed()

spinner = Halo(text='Counting all the instructions', spinner='dots')
spinner.start()
cnt = len(obj.iss)
spinner.succeed()
print(cnt)

def isascii(inst):
  addr = 0x5555e000 + inst.n
  addr = struct.pack('<I', addr)
  return all(c>=0x20 and c<=0x7f for c in addr)

def isascii_(inst, code):
  addr  = 0x5555e000 + inst.n
  addr += inst.code.index(code)
  addr  = struct.pack('<I', addr)
  return all(c>=0x20 and c<=0x7f for c in addr)

# wanted = 'mov DWORD PTR [edx]'
wanted = 'add eax'
for gadget in obj.find_gadget_asm(wanted, 2, isascii):
  print('-----')
  for inst in gadget:
    print(inst)
# for gadget in obj.find_gadget_code([0xcd], 10, isascii_):
#   print('-----')
#   for inst in gadget:
#     print(inst)
