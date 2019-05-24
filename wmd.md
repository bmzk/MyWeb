@[toc](Choice控件)

# 概述
A choice item is used to select one of a list of strings.
一个包含多个item的下拉列表

# 构造函数
TextCtrl类的构造函数形式如下 :
```Choice(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, choices=[], style=0, validator=DefaultValidator, name=ChoiceNameStr)```

#  修改列表内容
```Choice.SetItems(newItems)```
# 设置选择项
```Choice.Selection=0```

=号后面是1个整数,代表选择项在items中的序号,0为第一个,-1为无选择项
