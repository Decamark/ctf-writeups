
class Hoge:
  def __init__(self, p):
    self.p = p
    print(id(p))
    print(id(self.p))

print('-----')
p = Hoge(1)
print(id(p))
print('-----')
Hoge(p)
