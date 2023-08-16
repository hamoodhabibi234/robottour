#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;

// the setup function runs once when you press reset or power the board

void setup() {
int led = 9;
  pinMode(Led, OUTPUT);
  {
  Serial.begin(9600);
  Wire.begin();

  sensor.setTimeout(500);
  if (!sensor.init())
  {
    Serial.println("Failed to detect and initialize sensor!");
    while (1) {}
  }

}

}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(Led, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(Led, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);                      // wait for a second
}
