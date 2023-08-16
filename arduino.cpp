#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;

// the setup function runs once when you press reset or power the board

void setup() {
  /*int Led = 8;
  int 25cm = 9;
  int 75cm = 10;
  int 125cm = 11;
  int 175cm = 12;*/
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  Wire.begin();

  sensor.setTimeout(500);

}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
  if (sensor.readRangeSingleMillimeters() >= 740 && sensor.readRangeSingleMillimeters() <= 760)
    digitalWrite(10, HIGH);  // turn the LED on (HIGH is the voltage level)
  if (sensor.readRangeSingleMillimeters() >= 240 && sensor.readRangeSingleMillimeters() <= 260)
    digitalWrite(9, HIGH);  // turn the LED on (HIGH is the voltage level)
  if (sensor.readRangeSingleMillimeters() >= 1240 && sensor.readRangeSingleMillimeters() <= 1260)
    digitalWrite(11, HIGH);  // turn the LED on (HIGH is the voltage level)
  if (sensor.readRangeSingleMillimeters() >= 1740 && sensor.readRangeSingleMillimeters() <= 1760)
    digitalWrite(12, HIGH);  // turn the LED on (HIGH is the voltage level)
  digitalWrite(8, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(100);                      // wait for a second
  digitalWrite(8, LOW);   // turn the LED off by making the voltage LOW
  delay(100);                      // wait for a second
}
