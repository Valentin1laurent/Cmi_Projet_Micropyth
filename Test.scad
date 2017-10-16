$fn=300;
difference () {
cube([80,55,10],center=true);
cube([60,40,10] , center=true) ;
    linear_extrude (2) offset(r=2) cube ([80,55,10]);
}