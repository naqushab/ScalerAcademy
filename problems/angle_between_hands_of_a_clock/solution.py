class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle_per_tick = 6
        min_angle = minutes*min_angle_per_tick
        
        hour = hour%12
        hour_angle_per_tick = 0.5
        hour_angle = hour*30 + 0.5*minutes
        
        if hour_angle >= min_angle:
            angle = hour_angle-min_angle
        else:
            angle = min_angle-hour_angle
        
        return angle if angle <= 180 else 360-angle