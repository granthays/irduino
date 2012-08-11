
#include <IRremote.h>

int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
decode_results results;

void setup()
{
  irrecv.enableIRIn(); // Start the receiver
  Serial.begin(9600);
}

// Compare two tick values, returning 0 if newval is shorter,
// 1 if newval is equal, and 2 if newval is longer
// Use a tolerance of 20%
int compare(unsigned int oldval, unsigned int newval) {
  if (newval < oldval * .8) {
    return 0;
  } 
  else if (oldval < newval * .8) {
    return 2;
  } 
  else {
    return 1;
  }
}

// Use FNV hash algorithm: http://isthe.com/chongo/tech/comp/fnv/#FNV-param
#define FNV_PRIME_32 16777619
#define FNV_BASIS_32 2166136261

/* Converts the raw code values into a 32-bit hash code.
 * Hopefully this code is unique for each button.
 */
unsigned long decodeHash(decode_results *results) {
  unsigned long hash = FNV_BASIS_32;
  for (int i = 1; i+2 < results->rawlen; i++) {
    int value =  compare(results->rawbuf[i], results->rawbuf[i+2]);
    // Add value into the hash
    hash = (hash * FNV_PRIME_32) ^ value;
  }
  return hash;
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(decodeHash(&results), HEX); // Do something interesting with this value
    delay(200);
    irrecv.resume(); // Resume decoding (necessary!)
  }
}
