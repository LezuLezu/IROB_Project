#include "DEV_Config.h"
#include "LCD_Driver.h"
#include "LCD_GUI.h"

bool booleanReceived = false;
const byte numChars = 192;

char serialInput[numChars];

//Testing
char receivedChars[numChars];

boolean newData = false;

void setup() {
  System_Init();
  LCD_SCAN_DIR Lcd_ScanDir = SCAN_DIR_DFT;  
  LCD_Init( Lcd_ScanDir, 100);
  LCD_Clear(WHITE);
}

void loop(){
    booleanReceived = readSerial(serialInput); 
    if(newData == true && booleanReceived == true){
        LCD_Clear(WHITE);
        GUI_DisString_EN(50, 50, serialInput, &Font20, WHITE, BLACK);  
        newData = false; 
        booleanReceived = false;
        Serial.println(serialInput);
    }    
}

bool readSerial(char* serialInput){
  recvWithStartEndMarkers();
  strcpy(serialInput, receivedChars);
  if(serialInput != " "){return true;}
}

void recvWithStartEndMarkers(){
  static boolean recInProgress = false;
  static byte ndx = 0;
  char startMarker = '<';
  char endMarker = '>';
  char rc;
  while(Serial.available() > 0 && newData == false){
    rc = Serial.read();
    Serial.flush();
    if(recInProgress == true){
      if(rc != endMarker){
        receivedChars[ndx] = rc;
        ndx ++;
        if(ndx >= numChars){
          ndx = numChars -1;
        }
      }
      else{
        receivedChars[ndx] == '\0';
        recInProgress = false;
        ndx = 0;
        newData = true;
      }
    }
    else if (rc == startMarker){
      recInProgress = true;
    }
  }
}

void showData(){
  if(newData = true){
    Serial.println(receivedChars);
    newData = false;
  }
}
