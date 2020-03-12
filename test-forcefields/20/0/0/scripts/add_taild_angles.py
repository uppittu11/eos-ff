import pickle

filename = "cg-bond-coeffs-v4.p"

with open(filename, "rb") as f:
    data = pickle.load(f)

data['angles'].update(
        {'tail-taild-taild' : [152.4742,
                               9.395]
        })
data['angles'].update(
        {'tail-tail-taild-a' : [170.2064,
                                54.061]
        })
data['angles'].update(
        {'tail-tail-taild-b' : [149.2265,
                                21.693]
        })
data['angles'].update(
        {'ter2-tail-taild' : [148.3690,
                              9.284]
        })

data['bonds'].update(
        {'tail-taild' : [3.920,
                         20.928]
        })
data['bonds'].update(
        {'taild-taild' : [3.920,
                          20.928]
        })

with open("cg-bond-coeffs-v5.p", "wb") as f:
    pickle.dump(data, f)
