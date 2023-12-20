
ex = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

ex2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

actual = """%jb -> fz
%xz -> ck, bg
%xm -> qt, cs
%df -> hc, lq
%mt -> sx
%fr -> ks, hc
%tn -> pf
%gt -> pp, kb
%jn -> ck, nz
%td -> kz
&rd -> vd
%pp -> gv, kb
&qt -> jb, vx, bt, gh, td, gb
%ms -> xz
%vx -> fp
%rb -> ck, mt
%nz -> hh
%fp -> rp, qt
%gd -> gc
%gv -> kb
%nl -> cc, hc
%cs -> qt
%kz -> jb, qt
%vg -> fr, hc
%zq -> qt, xm
%pv -> ps
&bt -> vd
%ps -> kb, rf
%hh -> ck, ms
broadcaster -> gn, gb, rb, df
%gh -> td
%rf -> kb, nm
%rp -> qt, gh
%gc -> kb, pv
%gb -> vx, qt
%rq -> ck, ts
%nm -> gt
%gn -> kb, tn
&ck -> nz, fv, rb, sx, ms, mt
&fv -> vd
%cc -> vg
%bg -> ck, rq
&hc -> qr, ch, df, dj, cc, rd
%qr -> dj
%gq -> hc, ch
&pr -> vd
%ks -> lc, hc
%dj -> nl
%fz -> qt, zq
%lq -> gq, hc
&kb -> pv, pr, tn, nm, pf, gn, gd
%ts -> ck
%lc -> hc
%jl -> ck, jn
%sx -> jl
%pf -> gd
&vd -> rx
%ch -> qr"""

from collections import defaultdict

class FlipFlops():

    def __init__(self, dests):
        self.on = False
        self.dests = dests

    def pulse(self, src, signal):
        if signal == 'high':
            return None
        self.on = not self.on
        if self.on:
            return 'high'
        return 'low'

class Conjunction():

    def __init__(self, dests):
        self.memo = {}
        self.dests = dests

    def add_key(self, key):
        self.memo[key] = 'low'


    def pulse(self, src, signal):
        self.memo[src] = signal
        for state in self.memo.values():
            if state == 'low':
                return 'high'
        return 'low'

class Broadcaster():

    def __init__(self, dests):
        self.dests = dests

    def pulse(self, src, signal):
        return signal

class Button():
    def __init__(self, dests):
        self.dests = dests

    def pulse(self, src, signal):
        return signal

lines = actual.split('\n')
modules = defaultdict(lambda: None)
conjunctions = []
for line in lines:
    elems = line.split(' -> ')
    key = elems[0]
    dests = elems[1].split(', ')
    if key == 'broadcaster':
        modules[key] = Broadcaster(dests)
    if key[0] == '%':
        modules[key[1:]] = FlipFlops(dests)
    if key[0] == '&':
        modules[key[1:]] = Conjunction(dests)
        conjunctions.append(key[1:])
modules['button'] = Button(['broadcaster'])

for conjunction_key in conjunctions:
    conjunction = modules[conjunction_key]
    for key, module in modules.items():
        if key != conjunction_key:
            for dest in module.dests:
                if dest == conjunction_key:
                    conjunction.add_key(key)
                
low = 0
high = 0
i = 0
while True:
    pulses = [('button', 'broadcaster', 'low')]
    # print(f'====== round {i} ========')
    i += 1
    while len(pulses) != 0:
        src, mod, signal = pulses.pop(0)
        if signal == 'low':
            low += 1
        if signal == 'high':
            high += 1
        if mod == 'vd' and src == 'bt' and signal == 'high':
            print(i)
        if mod == 'vd' and src == 'rd' and signal == 'high':
            print(i)
        if mod == 'vd' and src == 'fv' and signal == 'high':
            print(i)
        if mod == 'vd' and src == 'pr' and signal == 'high':
            print(i)


        # print(src, signal, mod)
        module = modules[mod]
        if module:
            next_signal = module.pulse(src, signal)
            if next_signal:
                for dest in module.dests:
                    pulses.append((mod, dest, next_signal))
    else:
        continue
    break
    # print('\n\n')

#print('low', low)
#print('high', high)    
#print('total', low * high)

# 7 8 8 8 
