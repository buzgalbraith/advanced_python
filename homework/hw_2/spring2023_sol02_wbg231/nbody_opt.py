"""
    N-body simulation.
"""



def offset_momentum(ref,boddies, px=0.0, py=0.0, pz=0.0):
    '''
        ref is the body in the center of the system
        offset values from this reference
    '''
    d=set(boddies.keys())
    for body in  d:
        (r, [vx, vy, vz], m) = boddies[body]
        px -= vx * m
        py -= vy * m
        pz -= vz * m
        
    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m


def nbody(loops, reference, iterations,boddies,dt):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    # Set up global state
    offset_momentum(boddies[reference], boddies)

    for _ in range(loops):
        e=0
        seenit = set()
        d=set(boddies.keys())
        for body1 in d:
            for body2 in d:
                if (body1 != body2) and not (body2 in seenit):
                    ((x1, y1, z1), v1, m1) = boddies[body1]
                    ((x2, y2, z2), v2, m2) = boddies[body2]
                    (dx, dy, dz) =  (x1-x2, y1-y2, z1-z2)
                    e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)
                    seenit.add(body1)
            
        for body in d:
            (r, [vx, vy, vz], m) = boddies[body]
            e += m * (vx * vx + vy * vy + vz * vz) / 2.
        for _ in range(iterations):
            e=0
            seenit = set()
            d=set(boddies.keys())
            for body1 in d:
                for body2 in d:
                    if (body1 != body2) and not (body2 in seenit):
                        ([x1, y1, z1], v1, m1) = boddies[body1]
                        ([x2, y2, z2], v2, m2) = boddies[body2]
                        (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)
                        v1[0] -= dx * m2  * dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
                        v1[1] -= dy * m2 * dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
                        v1[2] -= dz * m2 * dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
                        v2[0] += dx * m1 * dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
                        v2[1] += dy * m1 * dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
                        v2[2] += dz * m1 * dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
                        seenit.add(body1)
                
            for body in d:
                (r, [vx, vy, vz], m) = boddies[body]
                r[0] += dt * vx
                r[1] += dt * vy
                r[2] += dt * vz
        seenit = set()
        d=set(boddies.keys())
        for body1 in d:
            for body2 in d:
                if (body1 != body2) and not (body2 in seenit):
                    ((x1, y1, z1), v1, m1) = boddies[body1]
                    ((x2, y2, z2), v2, m2) = boddies[body2]
                    (dx, dy, dz) =  (x1-x2, y1-y2, z1-z2)
                    e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)
                    seenit.add(body1)
            
        for body in d:
            (r, [vx, vy, vz], m) = boddies[body]
            e += m * (vx * vx + vy * vy + vz * vz) / 2.
        print(e)
if __name__ == '__main__':
    pi = 3.14159265358979323
    solar_mass = 4 * pi * pi
    days_per_year = 365.24
    boddies = {
        'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], solar_mass),

        'jupiter': ([4.84143144246472090e+00,
                    -1.16032004402742839e+00,
                    -1.03622044471123109e-01],
                    [1.66007664274403694e-03 * days_per_year,
                    7.69901118419740425e-03 * days_per_year,
                    -6.90460016972063023e-05 * days_per_year],
                    9.54791938424326609e-04 * solar_mass),

        'saturn': ([8.34336671824457987e+00,
                    4.12479856412430479e+00,
                    -4.03523417114321381e-01],
                [-2.76742510726862411e-03 * days_per_year,
                    4.99852801234917238e-03 * days_per_year,
                    2.30417297573763929e-05 * days_per_year],
                2.85885980666130812e-04 * solar_mass),

        'uranus': ([1.28943695621391310e+01,
                    -1.51111514016986312e+01,
                    -2.23307578892655734e-01],
                [2.96460137564761618e-03 * days_per_year,
                    2.37847173959480950e-03 * days_per_year,
                    -2.96589568540237556e-05 * days_per_year],
                4.36624404335156298e-05 * solar_mass),

        'neptune': ([1.53796971148509165e+01,
                    -2.59193146099879641e+01,
                    1.79258772950371181e-01],
                    [2.68067772490389322e-03 * days_per_year,
                    1.62824170038242295e-03 * days_per_year,
                    -9.51592254519715870e-05 * days_per_year],
                    5.15138902046611451e-05 * solar_mass)}
    nbody(100, 'sun', 20000, boddies,0.01)
