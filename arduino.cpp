#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor1;
VL53L0X sensor2;

// the setup function runs once when you press reset or power the board

void setup() {
  int Led = 8;
  /*int 25cm = 9,4;
  int 75cm = 10, 5;
  int 125cm = 11, 7;
  int 175cm = 12, 8;*/
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  Wire.begin();

  sensor1.setTimeout(500);

}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
  if (sensor1.readRangeSingleMillimeters() >= 630 && sensor1.readRangeSingleMillimeters() <= 650)
    digitalWrite(10, HIGH);  // turn the LED on (HIGH is the voltage level)
  if (sensor1.readRangeSingleMillimeters() >= 130 && sensor2.readRangeSingleMillimeters() <= 150)
    digitalWrite(9, HIGH);  // turn the LED on (HIGH is the voltage level)
  if (sensor1.readRangeSingleMillimeters() >= 1130 && sensor2.readRangeSingleMillimeters() <= 1150)
    digitalWrite(11, HIGH);  // turn the LED on (HIGH is the voltage level)
  if (sensor1.readRangeSingleMillimeters() >= 1630 && sensor2.readRangeSingleMillimeters() <= 1660)
    digitalWrite(12, HIGH);  // turn the LED on (HIGH is the voltage level)
  if (sensor2.readRangeSingleMillimeters() >= 630 && sensor2.readRangeSingleMillimeters() <= 650)
    digitalWrite(5, HIGH);  // turn the LED on (HIGH is the voltage level)
  if (sensor2.readRangeSingleMillimeters() >= 130 && sensor2.readRangeSingleMillimeters() <= 150)
    digitalWrite(4, HIGH);  // turn the LED on (HIGH is the voltage level)
  if (sensor2.readRangeSingleMillimeters() >= 1130 && sensor2.readRangeSingleMillimeters() <= 1150)
    digitalWrite(6, HIGH);  // turn the LED on (HIGH is the voltage level)
  if (sensor2.readRangeSingleMillimeters() >= 1630 && sensor2.readRangeSingleMillimeters() <= 1660)
    digitalWrite(7, HIGH);  // turn the LED on (HIGH is the voltage level)
  digitalWrite(8, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(100);                      // wait for a second
  digitalWrite(8, LOW);   // turn the LED off by making the voltage LOW
  delay(100);                      // wait for a second
}
