import Adafruit_MCP3008
#import Adafruit_GPIO.SPI as SPI

# Create MCP3008 object

def init_adc():
    mcp = Adafruit_MCP3008.MCP3008(clk = 11, cs = 8, miso = 9, mosi = 10)
    return mcp

def read_adc(channel,mcp):
    return mcp.read_adc(channel)
