def calc_j ( k , u ):
    return round( k*u*9.81 , 2)

def Average_speed(distance, time):    
    speed = distance / time
    return round(speed, 2)

def Braketrails_speed(Sc , Sr, t3 , k , u):
    j = calc_j(k, u)
    Ss = 0.5 * (Sc + Sr)
    Vbt = 0.5 * t3 * j + (2*j*Ss) ** 0.5 
    return round(Vbt, 2)

def Brake_distance (V , t1 , t2 , t3 , k , u):
    j = calc_j(k, u)
    Sbd = V * (t1 + t2 + 0.5*t3) + (V**2)/(2*j)
    return Sbd

def check_collision (S_collision , Sbd ):
    if S_collision > Sbd:
        return False
    else: 
        return True