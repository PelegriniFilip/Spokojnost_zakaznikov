spokojni = [0] * 24
nespokojni = [0] * 24

subor = open('subory/spokojnost_2.txt', 'r')
for riadok in subor:
    riadok = riadok.strip()
    info = riadok.split()
    spokojnost = info[1]
    cas = info[0].split(':')
    hodina = int(cas[0])
    minuta = int(cas[1])
    if spokojnost == 'ano':
        spokojni [hodina] += 1
    else:
        nespokojni [hodina] += 1
pocet_spokojnych = sum(spokojni)
pocet_nespokojnych = sum(nespokojni)
spolu = pocet_spokojnych + pocet_nespokojnych
print('Vyjadrilo sa { } zakaznikov.'.format(spolu))
pocet_ok = max(spokojni)
hodina = spokojni.index(pocet_ok)
print('Najviac spokojnych zak. ({ }) je cez hodinu: { }'.format(pocet_ok,hodina))
nespokojni2 = []
for pocet in nespokojni:
    if pocet > 0:
        nespokojni2.append(pocet)
pocet_zle = min(nespokojni2)
hodina = nespokojni.index(pocet_zle)
print('Najmenej spokojnych zak. ({ }) je cez hodinu:{}'.format(pocet_zle,hodina))

percenta_spokojnosti = [0] * 24
for i in range(24):
    pocet = spokojni[i] + nespokojni[i]
    if pocet > 0:
        percenta_spokojnosti[i] / pocet * 100
for i in range(24):
    if percenta_spokojnosti[i] > 0:
        print('V { }. hodine je spokojnych {:5.2f}%'.format(i,percenta_spokojnosti[i]))
