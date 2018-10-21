
#define CMDBUFFER_SIZE 32
const int sensorfpin = A0;
const int sensoripin = A1;

void setup()
{
Serial.begin(9600); 
}

void loop()
{
 
}
void serialEvent()
{
 static char cmdBuffer[CMDBUFFER_SIZE] = "";
 char c;
 while(Serial.available()) 
 {
   c = processCharInput(cmdBuffer, Serial.read());
   Serial.print(c);
   if (c == '\n') 
   {
     Serial.println();
     //Full command received. Do your stuff here!			
     if (strcmp("humedadf", cmdBuffer) == 0)
     {
        Serial.println("\r\nYou typed Humedad Tierra!"); 
        Serial.println(sensorfpin);
     }
     else if (strcmp("humedadr", cmdBuffer) == 0)
     {
        Serial.println("\r\nYou typed Humedad Relativa!"); 
        Serial.println(sensoripin);
     }
     else
     {
        Serial.println("\r\nError!"); 
     }
     cmdBuffer[0] = 0;
   }
 }
 delay(1);
}

char processCharInput(char* cmdBuffer, const char c)
{
 //Store the character in the input buffer
 if (c >= 32 && c <= 126) //Ignore control characters and special ascii characters
 {
   if (strlen(cmdBuffer) < CMDBUFFER_SIZE) 
   { 
     strncat(cmdBuffer, &c, 1);   //Add it to the buffer
   }
   else  
   {   
     return '\n';
   }
 }
 else if ((c == 8 || c == 127) && cmdBuffer[0] != 0) //Backspace
 {

   cmdBuffer[strlen(cmdBuffer)-1] = 0;
 }

 return c;
}

