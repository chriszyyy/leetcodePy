#coding:utf-8
#! /usr/bin/env python
COLS = 16
ROWS = 20

class Block():
    color = (255,255,255)
    def __init__(self):
        self._state = 0
    def __str__(self):
        return self.__class__.__name__
    def _orientations(self):
        raise NotImplementedError()
    def rotate(self, times=1):
        for i in range(times):
            if len(self._orientations())-1 == self._state:
                self._state = 0
                #只要_state比_orientations长度-1还要小，就让_state加1

            else:
                self._state += 1
    def blades(self):
        # 返回对应形状的一种旋转形状。(返回一个list,list中每个元素是一个(x,y))
        return self._orientations()[self._state]

    def grid(self, pos, cols=COLS, rows=ROWS):
        # grid()函数：对于一个形状，从它的cell中的pos位置，按照orientations的位置提示，把所有cell涂色
        # pos表示的是shape中的一个cell，也就是(0,0)
        if cols*rows <= pos:
            return None
        # 这种情况应该不可能出现吧。如果出现<=的情况
        # 那么，pos都跑到界外了。。

        grid = [None] * cols * rows
        grid[pos] = str(self)
        for b in self.blades():
            x, y = b
            # pos/cols表示pos处于board的第几行
            if pos/cols != (pos+x)/cols:
                return None
            i = pos + x + y * cols
            if i < 0:
                continue
            elif cols*rows <= i:
                return None
            grid[i] = str(self)
            # 给相应的其他位置都“涂色”,比如对于方块，是O型的，那么pos肯定是有值的，pos位于有上角。。
        return grid

# 以下每个形状class，_orientations（）都返回形状的列表。(0,0)一定被包含在其中，为了省略空间所以都没有写出.
class O(Block):
    color = (207,247,0)
    def _orientations(self):
        return (
            [(-1,0), (-1,1), (0,1)],
            )
class I(Block):
    color = (135,240,60)
    def _orientations(self):
        return (
            [(-2,0), (-1,0), (1,0)],
            [(0,-1), (0,1), (0,2)],
            )
class S(Block):
    color = (171,252,113)
    def _orientations(self):
        return (
            [(1,0), (-1,1), (0,1)],
            [(0,-1), (1,0), (1,1)],
            )
class Z(Block):
    color = (243,61,110)
    def _orientations(self):
        return (
            [(-1,0), (0,1), (1,1)],
            [(1,-1), (1,0), (0,1)],
            )
class L(Block):
    color = (253,205,217)
    def _orientations(self):
        return (
            [(-1,1), (-1,0), (1,0)],
            [(0,-1), (0,1), (1,1)],
            [(-1,0), (1,0), (1,-1)],
            [(-1,-1), (0,-1), (0,1)],
            )
class J(Block):
    color = (140,180,225)
    def _orientations(self):
        return (
            [(-1,0), (1,0), (1,1)],
            [(0,1), (0,-1), (1,-1)],
            [(-1,-1), (-1,0), (1,0)],
            [(-1,1), (0,1), (0,-1)],
            )
class T(Block):
    color = (229,251,113)
    def _orientations(self):
        return (
            [(-1,0), (0,1), (1,0)],
            [(0,-1), (0,1), (1,0)],
            [(-1,0), (0,-1), (1,0)],
            [(-1,0), (0,-1), (0,1)],
            )
