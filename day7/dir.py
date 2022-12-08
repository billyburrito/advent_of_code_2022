class Dir:
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent
    self.files = {}
    self.dirs = {}
    self.size = 0

  def add_file(self, name, size):
    self.files[name] = size
    self.size += int(size)

  def add_dir(self, name):
    self.dirs[name] = Dir(name, self)

  def calc_size(self):
    amount = 0
    for i in self.dirs.keys():
      amount += self.dirs[i].calc_size()
    amount += self.size
    return amount

  def __repr__(self) -> str:
    return self.name + " dirs: " + str(self.dirs) + " files: " + str(self.files) + " size: " + str(self.size)