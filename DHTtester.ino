#include "DHT.h"

#define DHTPIN 4         // Digital pin connected to the DHT sensor
#define DHTTYPE DHT22    // DHT 22  (AM2302), AM2321

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  delay(2000);  // Wait 1 second between measurements

  float humidity = dht.readHumidity();
  float temperatureC = dht.readTemperature();  // Read temperature in Celsius

  // Check if any reads failed and exit early
  if (isnan(humidity) || isnan(temperatureC)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }


  Serial.print(temperatureC);
  Serial.print(",");
  Serial.println(humidity);

  //delay(2000);  // Wait for 2 seconds before sending next reading
}
