#!/usr/bin/env python

spacing = 0.1  # m
lines = []
for c in range(0, 8):
    rs = [range(11), reversed(range(11))][c % 2]
    for r in rs:
        lines.append('  {"point": [%.2f, %.2f, %.2f]}' %
                     (c*spacing, 0, (r)*spacing))
print '[\n' + ',\n'.join(lines) + '\n]'
