#coding:utf8
#! /usr/bin/env python
# 注释说明：shape表示一个俄罗斯方块形状 cell表示一个小方块
import sys
from random import choice
import pygame
from pygame.locals import *
from block import O, I, S, Z, L, J, T

COLS = 16
ROWS = 20
CELLS = COLS * ROWS
CELLPX = 32  # 每个cell的像素宽度
POS_FIRST_APPEAR = COLS / 2
SCREEN_SIZE = (COLS * CELLPX, ROWS * CELLPX)
COLOR_BG = (0, 0, 0)


def draw(grid, pos=None):
    # grid是一个list，要么值为None，要么值为'Block'
    # 非空值在eval（）的作用下，用于配置颜色
    if pos:  # 6x5
        s = pos - 3 - 2 * COLS  # upper left position
        for p in range(0, COLS):
            q = s + p * COLS
            for i in range(q, q + 6):
                if 0 <= i < CELLS:
                    # 0 <=i < CELLS:表示i这个cell在board内部。
                    c = eval(grid[i] + ".color") if grid[i] else COLOR_BG
                    # 执行着色。shape的cell涂对应的class设定好的颜色，否则涂黑（背景色）
                    a = i % COLS * CELLPX
                    b = i / COLS * CELLPX
                    screen.fill(c, (a, b, CELLPX, CELLPX))
    else:  # all
        screen.fill(COLOR_BG)
        for i, occupied in enumerate(grid):
            if occupied:
                c = eval(grid[i] + ".color")  # 获取方块对应的颜色
                a = i % COLS * CELLPX  # 横向长度
                b = i / COLS * CELLPX  # 纵向长度
                screen.fill(c, (a, b, CELLPX, CELLPX))
                # fill:为cell上色, 第二个参数表示rect
    pygame.display.flip()
    # 刷新屏幕


def phi(grid1, grid2, pos):  # 4x4
# 两个grid之4*4区域内是否会相撞（冲突）
    s = pos - 2 - 1 * COLS  # upper left position
    for p in range(0, 4):
        q = s + p * COLS
        for i in range(q, q + 4):
            try:
                if grid1[i] and grid2[i]:
                    return False
            except:
                pass
    return True


def merge(grid1, grid2):
    # 合并两个grid
    grid = grid1[:]
    for i, c in enumerate(grid2):
        if c:
            grid[i] = c
    return grid


def complete(grid):
    # 减去满行
    n = 0
    for i in range(0, CELLS, COLS):
        # 步长为一行。
        if not None in grid[i:i + COLS]:
        #这一句很容易理解错误。
        #实际含义是：如果grid[i:i + COLS]都不是None,那么执行下面的语句
            grid = [None] * COLS + grid[:i] + grid[i + COLS:]
            n += 1
    return grid, n
#n表示减去的行数，用作统计分数

pygame.init()
pygame.event.set_blocked(None)
pygame.event.set_allowed((KEYDOWN, QUIT))
pygame.key.set_repeat(75, 0)
pygame.display.set_caption('Tetris')
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.update()

grid = [None] * CELLS
speed = 500
screen.fill(COLOR_BG)
while True: # spawn a block
    block = choice([O, I, S, Z, L, J, T])()
    pos = POS_FIRST_APPEAR
    if not phi(grid, block.grid(pos), pos): break # you lose
    pygame.time.set_timer(KEYDOWN, speed)
    # repeatedly create an event on the event queue
    # speed是时间间隔。。。speed越小，方块下落的速度越快。。。speed应该换为其他名字

    while True: # move the block
        draw(merge(grid, block.grid(pos)), pos)
        event = pygame.event.wait()
        if event.type == QUIT: sys.exit()
        try:
            aim = {
                K_UNKNOWN: pos+COLS,
                K_UP: pos,
                K_DOWN: pos+COLS,
                K_LEFT: pos-1,
                K_RIGHT: pos+1,
            }[event.key]
        except KeyError:
            continue
        if event.key == K_UP:
            # 变形
            block.rotate()

        elif event.key in (K_LEFT, K_RIGHT) and pos / COLS != aim / COLS:
            # pos/COLS表示当前位置所在行
            # aim/COLS表示目标位置所在行
            # 此判断表示，当shape在左边界时，不允许再向左移动（越界。。）,在最右边时向右也禁止
            continue

        grid_aim = block.grid(aim)
        if grid_aim and phi(grid, grid_aim, aim):
            pos = aim
        else:
            if event.key == K_UP:
                block.rotate(times=3)
            elif not event.key in (K_LEFT, K_RIGHT):
                break

    grid = merge(grid, block.grid(pos))
    grid, n = complete(grid)
    if n:
        draw(grid)
        speed -= 5 * n
        if speed < 75: speed = 75
