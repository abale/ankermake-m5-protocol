## ------------------------------------------
## Generated by Transwarp
##
## THIS FILE IS AUTOMATICALLY GENERATED.
## DO NOT EDIT. ALL CHANGES WILL BE LOST.
## ------------------------------------------

import enum
from dataclasses import dataclass
from .amtypes import *

class MqttMsgType(enum.IntEnum):
    Single      = 0xc0 # Whole message in a single packet. No further packets in this stream
    MultiBegin  = 0xc1 # Reallocate buffer memory, *then* append to message. Unless this is used
    MultiAppend = 0xc2 # Append to existing message buffer.
    MultiFinish = 0xc3 # Append data, then handle complete message.

class MqttMsgType(enum.IntEnum):
    ZZ_MQTT_CMD_EVENT_NOTIFY           = 0x03e8 # 
    ZZ_MQTT_CMD_PRINT_SCHEDULE         = 0x03a9 # 
    ZZ_MQTT_CMD_FIRMWARE_VERSION       = 0x03ea # Not implemented?
    ZZ_MQTT_CMD_NOZZLE_TEMP            = 0x03eb # Set nozzle temperature in units of 1/100th deg C (i.e.31337 is 313.37C)
    ZZ_MQTT_CMD_HOTBED_TEMP            = 0x03ec # Set hotbed temperature in units of 1/100th deg C (i.e. 1337 is 13.37C)
    ZZ_MQTT_CMD_FAN_SPEED              = 0x03ed # Set fan speed
    ZZ_MQTT_CMD_PRINT_SPEED            = 0x03ee # ? Set print speed
    ZZ_MQTT_CMD_AUTO_LEVELING          = 0x03ef # (probably) Perform auto-levelling procedure
    ZZ_MQTT_CMD_PRINT_CONTROL          = 0x03f0 # 
    ZZ_MQTT_CMD_FILE_LIST_REQUEST      = 0x03f1 # Request on-board file list (value == 1) or usb file list (value != 1)
    ZZ_MQTT_CMD_GCODE_FILE_REQUEST     = 0x03f2 # 
    ZZ_MQTT_CMD_ALLOW_FIRMWARE_UPDATE  = 0x03f3 # 
    ZZ_MQTT_CMD_GCODE_FILE_DOWNLOAD    = 0x03fc # 
    ZZ_MQTT_CMD_Z_AXIS_RECOUP          = 0x03fd # ?
    ZZ_MQTT_CMD_EXTRUSION_STEP         = 0x03fe # (probably) run the extrusion stepper
    ZZ_MQTT_CMD_ENTER_OR_QUIT_MATERIEL = 0x03ff # maybe related to filament change?
    ZZ_MQTT_CMD_MOVE_STEP              = 0x0400 # 
    ZZ_MQTT_CMD_MOVE_DIRECTION         = 0x0401 # 
    ZZ_MQTT_CMD_MOVE_ZERO              = 0x0402 # (probably) Move to home position
    ZZ_MQTT_CMD_APP_QUERY_STATUS       = 0x0403 # 
    ZZ_MQTT_CMD_ONLINE_NOTIFY          = 0x0404 # 
    ZZ_MQTT_CMD_APP_RECOVER_FACTORY    = 0x0405 # 
    ZZ_MQTT_CMD_BLE_ONOFF              = 0x0407 # (probably) Enable/disable Bluetooth Low Energy ("ble") radio
    ZZ_MQTT_CMD_DELETE_GCODE_FILE      = 0x0408 # (probably) Delete specified gcode file
    ZZ_MQTT_CMD_RESET_GCODE_PARAM      = 0x0409 # ?
    ZZ_MQTT_CMD_DEVICE_NAME_SET        = 0x040a # 
    ZZ_MQTT_CMD_DEVICE_LOG_UPLOAD      = 0x040b # 
    ZZ_MQTT_CMD_ONOFF_MODAL            = 0x040c # ?
    ZZ_MQTT_CMD_MOTOR_LOCK             = 0x040d # ?
    ZZ_MQTT_CMD_PREHEAT_CONFIG         = 0x040e # ?
    ZZ_MQTT_CMD_BREAK_POINT            = 0x040f # 
    ZZ_MQTT_CMD_AI_CALIB               = 0x0410 # 
    ZZ_MQTT_CMD_VIDEO_ONOFF            = 0x0411 # ?
    ZZ_MQTT_CMD_ADVANCED_PARAMETERS    = 0x0412 # ?
    ZZ_MQTT_CMD_GCODE_COMMAND          = 0x0413 # Run custom GCode command
    ZZ_MQTT_CMD_PREVIEW_IMAGE_URL      = 0x0414 # 
    ZZ_MQTT_CMD_SYSTEM_CHECK           = 0x0419 # ?
    ZZ_MQTT_CMD_AI_SWITCH              = 0x041a # ?
    ZZ_STEST_CMD_GCODE_TRANSPOR        = 0x07e2 # ?
    ZZ_MQTT_CMD_ALEXA_MSG              = 0x0bb8 # 

@dataclass
class MqttMsg:
    m1         : u8 # Magic constant: 'M'
    m2         : u8 # Magic constant: 'A'
    size       : u16 # length of packet, including header and checksum (minimum 65).
    m3         : u8 # Magic constant: 5
    m4         : u8 # Magic constant: 1
    m5         : u8 # Magic constant: 2
    m6         : u8 # Magic constant: 5
    m7         : u8 # Magic constant: 'F'
    packet_type: MqttMsgType # Packet type. Only seen as 0xc0
    packet_num : u16 # maybe for fragmented messages?set to 1 for unfragmented messages.
    time       : u32 # `gettimeofday()` in whole seconds
    device_guid: bytes # device guid, as hex string
    padding    : bytes = field(repr=False) # padding bytes, allways zero

    @classmethod
    def parse(cls, p):
        m1, p = u8.parse(p)
        m2, p = u8.parse(p)
        size, p = u16.parse(p)
        m3, p = u8.parse(p)
        m4, p = u8.parse(p)
        m5, p = u8.parse(p)
        m6, p = u8.parse(p)
        m7, p = u8.parse(p)
        packet_type, p = MqttMsgType.parse(p)
        packet_num, p = u16.parse(p)
        time, p = u32.parse(p)
        device_guid, p = String.parse(p, 40)
        padding, p = Zeroes.parse(p, 8)
        return cls(m1, m2, size, m3, m4, m5, m6, m7, packet_type, packet_num, time, device_guid, padding), p

    def pack(self):
        p  = self.m1.pack()
        p += self.m2.pack()
        p += self.size.pack()
        p += self.m3.pack()
        p += self.m4.pack()
        p += self.m5.pack()
        p += self.m6.pack()
        p += self.m7.pack()
        p += self.packet_type.pack()
        p += self.packet_num.pack()
        p += self.time.pack()
        p += String.pack(self.device_guid, 40)
        p += Zeroes.pack(self.padding, 8)
        return p

