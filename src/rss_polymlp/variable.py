def atom_variable(element):
    atomic_lengths = {
        "Ag": 2.93,
        "Al": 2.86,
        "Au": 2.94,
        "Ba": 4.35,
        "Be": 2.20,
        "Bi": 3.067,
        "Ca": 3.90,
        "Cd": 3.05,
        "Cr": 2.45,
        "Cs": 5.48,
        "Cu": 2.57,
        "Ga": 2.75,
        "Ge": 2.503,
        "Hf": 3.10,
        "Hg": 3.37,
        "In": 3.39,
        "Ir": 2.74,
        "K": 4.71,
        "La": 3.703,
        "Li": 3.05,
        "Mg": 2.557,
        "Mo": 2.727,
        "Na": 3.73,
        "Nb": 2.802,
        "Os": 2.686,
        "Pb": 3.5,
        "Pd": 2.786,
        "Pt": 2.81,
        "Rb": 5.06,
        "Re": 2.745,
        "Rh": 2.705,
        "Ru": 2.642,
        "Sc": 3.196,
        "Si": 2.368,
        "Sn": 2.81,
        "Sr": 4.268,
        "Ta": 2.869,
        "Ti": 2.87,
        "Tl": 3.453,
        "V": 2.642,
        "W": 2.746,
        "Y": 3.53,
        "Zn": 2.655,
        "Zr": 3.176,
    }

    _atomic_length = atomic_lengths.get(element)

    if _atomic_length is None:
        raise ValueError(f"Invalid element: {element}. Atomic length not found.")

    return _atomic_length
