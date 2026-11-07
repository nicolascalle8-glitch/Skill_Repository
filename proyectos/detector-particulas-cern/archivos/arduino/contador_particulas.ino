// Contador de partículas para el detector DIY de CERN (con TL074CN)
// Placa: Arduino Uno. La salida del comparador (U1C, pin 8, después del divisor R12/R13) entra por D2.
// Cada partícula = un flanco de subida en D2.
// Por el monitor serial (9600 baudios) sale una línea por intervalo: tiempo_ms,cuentas_intervalo,cuentas_total,cpm

// ---------------- Constantes ----------------
const byte PIN_PULSO = 2;                 // D2 = interrupción INT0 del Uno
const byte PIN_LED   = 13;                // LED de la placa, parpadea con cada cuenta
const unsigned long INTERVALO_MS = 10000; // cada cuánto se reportan las cuentas (10 s)
const unsigned long TIEMPO_MUERTO_US = 300; // ignora rebotes del comparador después de cada pulso

// ---------------- Variables compartidas con la interrupción ----------------
volatile unsigned long cuentasIntervalo = 0;
volatile unsigned long ultimoPulsoUs = 0;
volatile bool hayPulsoNuevo = false;

unsigned long cuentasTotal = 0;
unsigned long inicioIntervalo = 0;
unsigned long apagarLedEn = 0;

// ---------------- Interrupción: se ejecuta en cada flanco de subida en D2 ----------------
void alDetectarPulso() {
  unsigned long ahora = micros();
  if (ahora - ultimoPulsoUs > TIEMPO_MUERTO_US) {  // un pulso solo cuenta una vez
    cuentasIntervalo++;
    hayPulsoNuevo = true;
  }
  ultimoPulsoUs = ahora;
}

void setup() {
  Serial.begin(9600);
  pinMode(PIN_PULSO, INPUT);   // sin pull-up: el divisor R12/R13 ya fija el nivel
  pinMode(PIN_LED, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(PIN_PULSO), alDetectarPulso, RISING);
  Serial.println("tiempo_ms,cuentas_intervalo,cuentas_total,cpm");
  inicioIntervalo = millis();
}

void loop() {
  unsigned long ahora = millis();

  // LED: encender un momento con cada pulso
  if (hayPulsoNuevo) {
    hayPulsoNuevo = false;
    digitalWrite(PIN_LED, HIGH);
    apagarLedEn = ahora + 30;
  }
  if (digitalRead(PIN_LED) == HIGH && (long)(ahora - apagarLedEn) >= 0) {
    digitalWrite(PIN_LED, LOW);
  }

  // Reporte por serial cada INTERVALO_MS
  if (ahora - inicioIntervalo >= INTERVALO_MS) {
    noInterrupts();                       // copiar y reiniciar sin que entre otro pulso a la mitad
    unsigned long cuentas = cuentasIntervalo;
    cuentasIntervalo = 0;
    interrupts();

    cuentasTotal += cuentas;
    float cpm = cuentas * 60000.0 / (ahora - inicioIntervalo);

    Serial.print(ahora);           Serial.print(',');
    Serial.print(cuentas);         Serial.print(',');
    Serial.print(cuentasTotal);    Serial.print(',');
    Serial.println(cpm, 1);

    inicioIntervalo = ahora;
  }
}
