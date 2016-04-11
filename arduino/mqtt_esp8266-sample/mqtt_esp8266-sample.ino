
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* ssid = "";
const char* password = "";

const char* mClient_id = "cliennt-arduino-1234";

//byte localserver[] = {192, 168, 30, 106 };
const char* mqtt_server = "test.mosquitto.org";

char mTopicIn[]="item-1234-ABC/device-1/matrix_sample";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;
int mMaxMatrix=20;

//
void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
//  Serial.begin(115200);
  Serial.begin(9600);
  
  setup_wifi();
  client.setServer(mqtt_server, 1883);
//  client.setServer(localserver, 1883);
  client.setCallback(callback);
}

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  //Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  //Serial.println("IP address: ");
  //Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  //Serial.print("Message arrived [");
  //Serial.print(topic);
  //Serial.print("] ");
  String sTopi=String( mTopicIn );
  String sTopi_in =String( topic );
  String sLine="";
  String sCRLF="\r\n";
  if( sTopi.equals( sTopi_in ) ){
    Serial.print("011");
    int iCt=0;
    for (int i=0;i<length;i++) {
//Serial.print((char)payload[i]);
//      String sPay= String( (char)payload[i] );
//      sLine +=sPay;
      char sTmp[4+1];
      sprintf(sTmp, "%02x", (char *)payload[i]);
Serial.print(sTmp);
      iCt++;
      if(iCt>=  6){
          delay(100);
          iCt=0;
      }
    }
//Serial.print("sLine=");
//Serial.println(sLine);
//    send_matrix(sLine);
   }
  Serial.println();
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect( mClient_id )) {
      Serial.println("connected");
      client.subscribe(mTopicIn);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}



