class Validator(object):
    @classmethod
    def __convertFromStr(cls, input: str, type: str):
        try:
            if type == "float":
                number = round(float(input), 2)
            elif type == "int":
                number = int(input)
            return number
        
        except ValueError:
            return "error"

    @classmethod
    def checkTime(cls, time: str):
        if not isinstance(time, float):
            time = cls.__convertFromStr(time, "float")
            
        if time == "error":
            return time

        return .0 < time

    @classmethod
    def checkCorrectionFactor(cls, factor: str):
        if not isinstance(factor, float):
            factor = cls.__convertFromStr(factor, "float")

        if factor == "error":
            return factor
        
        return factor == .0 or .7 <= factor and factor <= 1.0

    @classmethod
    def checkTractionCoef(cls, coef: str):
        if not isinstance(coef, float):
            coef = cls.__convertFromStr(coef, "float")

        if coef == "error":
            return coef
        
        return .05 <= coef and coef <= 1.5
    
    @classmethod
    def checkDistance(cls, dist: str):
        if not isinstance(dist, float):
            dist = cls.__convertFromStr(dist, "float")
        
        if dist == "error":
            return dist

        return .0 <= dist

    @classmethod
    def checkVelocity(cls, velocity: str):
        if not isinstance(velocity, int):
            velocity = cls.__convertFromStr(velocity, "int")

        if velocity == "error":
            return velocity

        return 0 < velocity and velocity % 10 == 0
    