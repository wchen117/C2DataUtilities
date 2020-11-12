import data

d = data.Data()
d.con.read(sys.argv[1])
d.inl.read(sys.argv[2])
d.raw.read(sys.argv[3])
d.rop.read(sys.argv[4])

tls = sys.argv[5]

'''case identification data from raw'''
stilde = d.raw.case_identification.sbase
stilde_inverse = 1.0/stilde

'''buse data from raw'''
Is = len(d.raw.buses)
vover = np.zeros(Is)
vunder = np.zeros(Is)
for iter_I, r in enumerate(d.raw.buses.values()):
    I.append(r.i)
    A.append(r.area)
    vover[iter_I] = r.nvhi
    vunder[iter_I] = r.nvlo





