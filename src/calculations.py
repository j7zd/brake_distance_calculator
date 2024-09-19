def ms_to_kmh(speed_ms):
    return round(speed_ms * 3.6, 2)

def kmh_to_ms(speed_kmh):
    return round(speed_kmh / 3.6, 2)

def calc_j ( k , u ):
    return round( k*u*9.81 , 2)

def Average_speed(distance, time):    
    Vavg = distance / time
    return round(Vavg, 2)

def Braketrails_speed(Sc , Sr, t3 , k , u):
    j = calc_j(k, u)
    Ss = 0.5 * (Sc + Sr)
    Vbt = 0.5 * t3 * j + (2*j*Ss) ** 0.5 
    return round(Vbt, 2)

def Brake_distance (V , t1 , t2 , t3 , k , u):
    j = calc_j(k, u)
    Sbd = V * (t1 + t2 + 0.5*t3) + (V**2)/(2*j)
    return round(Sbd , 2)

def check_collision (S_collision , Sbd ):
    return S_collision <= Sbd

def Vmax(S_collision, t1, t2, t3, k, u):
    j = calc_j(k, u)
    a = 1 / (2 * j)  
    b = t1 + t2 + 0.5 * t3 
    c = -S_collision 
    D = b**2 - 4 * a * c

    if D < 0:
        return None 
    
    sqrt_D = D ** 0.5
    Vmax_1 = (-b + sqrt_D) / (2 * a)
    Vmax_2 = (-b - sqrt_D) / (2 * a)

    if Vmax_1 > 0:
        return ms_to_kmh(Vmax_1)
    elif Vmax_2 > 0:
        return ms_to_kmh(Vmax_2)
    else:
        return None
