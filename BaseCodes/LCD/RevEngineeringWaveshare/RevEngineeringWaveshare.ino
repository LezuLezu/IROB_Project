#include "DEV_Config.h"
#include "LCD_Driver.h"
#include "LCD_GUI.h"

char* hello = "Hellow Worlds";
bool booleanReceived = false;
char serialInput[64];

void setup() {
  System_Init();
//  Serial.println("4inch　TFT　Touch Shiled LCD Show...");  
//  Serial.println("LCD Init...");
  LCD_SCAN_DIR Lcd_ScanDir = SCAN_DIR_DFT;  
  LCD_Init( Lcd_ScanDir, 100);
//  Serial.println("LCD_Clear...");
  LCD_Clear(WHITE);
//  Serial.println("LCD_Show...");
}

void loop() {
  Serial.println("in loop");
  booleanReceived = readSerial(serialInput); 
  if(booleanReceived == true){
    Serial.println("Bool IF true");
    LCD_Clear(BLACK);
    GUI_DisString_EN(50, 75, serialInput, &Font24, BLUE, RED);    
  }
  delay(500);
}

bool readSerial(char* serialInput){
  if(Serial.available()){  
    String serialRead;
//    delay(50);
    serialRead = Serial.readString();
    if(serialRead != " "){
      Serial.println("in serialRead");
      serialRead.trim();   
      Serial.flush();
      Serial.println(serialRead);
      strcpy(serialInput, serialRead.c_str());
      return true;
    }else{
      return false;
    }
  }else{
    return false;
  }
}
