# Exercise 1.4 from http://www.greenteapress.com/thinkpython/thinkpython.pdf
# Using Python to do simple arithmetic 
# Plus string output because I can

seconds_per_min = 60;
km_per_mile = 1.61;
distance_km = 10.0; 

# Establish distance & time base quantities 
print "10km in 43 minutes 30 seconds";
total_seconds = 43.0*seconds_per_min + 30; 

print "Total seconds =", total_seconds;
print "Total kilometers =", distance_km;

km_pace_s = total_seconds / distance_km ;
km_pace_m = (total_seconds / seconds_per_min) / distance_km; 
print "Seconds per kilometer =", km_pace_s ;
print "Fractional minutes per kilometer=", km_pace_m; 

remainder_secs = (km_pace_m - round(km_pace_m,0)) * seconds_per_min;
pace_minutes = round(km_pace_m,0);
print "Or ", pace_minutes, "minutes and ", remainder_secs, "seconds per km."; 
 
mile_pace_m = km_pace_m * km_per_mile;
remainder_secs = (mile_pace_m - round(mile_pace_m,0)) * seconds_per_min; 
pace_minutes = round(mile_pace_m,0); 
print "Or ", pace_minutes, "minutes and ", remainder_secs, "seconds per mile."; 
