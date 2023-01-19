#include "DEV_Config.h"
#include "LCD_Driver.h"
#include "LCD_GUI.h"

bool booleanReceived = false;
const byte numChars = 192;

char serialInput[numChars];



void setup() {
  System_Init();
  LCD_SCAN_DIR Lcd_ScanDir = SCAN_DIR_DFT;  
  LCD_Init( Lcd_ScanDir, 100);
  LCD_Clear(WHITE);
}

void loop(){
    booleanReceived = readSerial(serialInput); 
    if(booleanReceived == true){
        LCD_Clear(WHITE);
        GUI_DisString_EN(50, 50, serialInput, &Font20, WHITE, BLACK);  
        booleanReceived = false;
//        Serial.println(serialInput);
    }    
}

bool readSerial(char* serialInput){
  if(Serial.available()){  
    String serialRead;
//    delay(50);
    serialRead = Serial.readString();
    if(serialRead != " "){
//      Serial.println("in serialRead");
      serialRead.trim();   
      Serial.flush();
//      Serial.println(serialRead);
      strcpy(serialInput, serialRead.c_str());
      return true;
    }else{
      return false;
    }
  }else{
    return false;
  }
}
